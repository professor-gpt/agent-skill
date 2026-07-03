"""
Airflow DAG patterns for idempotent, backfill-safe pipelines.

Key principles demonstrated:
  1. Logical-date-driven processing (never wall-clock)
  2. DELETE+INSERT partition writes (safe reruns)
  3. Dataset-driven scheduling (no timing-based coupling)
  4. Sane defaults: retries, timeouts, no surprise catchup
"""

from datetime import datetime, timedelta

from airflow.datasets import Dataset
from airflow.decorators import dag, task

# Datasets make dependencies explicit: downstream DAGs trigger when this
# is updated, instead of guessing "upstream is usually done by 6am".
ORDERS_MART = Dataset("warehouse://analytics/fct_orders")

DEFAULT_ARGS = {
    "owner": "data-platform",
    "retries": 3,                                  # transient failures happen
    "retry_delay": timedelta(minutes=5),
    "retry_exponential_backoff": True,
    "execution_timeout": timedelta(minutes=45),    # ~2x p95 runtime
}


@dag(
    dag_id="orders_daily",
    schedule="0 4 * * *",             # 04:00 UTC daily
    start_date=datetime(2026, 1, 1),
    catchup=False,                    # explicit choice: backfill on demand,
    default_args=DEFAULT_ARGS,        # via `airflow dags backfill`
    max_active_runs=1,                # avoid overlapping partition writes
    tags=["orders", "daily", "tier-1"],
)
def orders_daily():

    @task
    def extract_orders(data_interval_start=None, data_interval_end=None) -> str:
        """PATTERN 1 — logical date, not wall-clock.

        A rerun (or backfill) of 2026-06-01 extracts exactly 2026-06-01,
        no matter when it actually executes.
        """
        query = f"""
            SELECT * FROM source.orders
            WHERE updated_at >= '{data_interval_start}'
              AND updated_at <  '{data_interval_end}'
        """
        # run query, land to s3://lake/raw/orders/dt={ds}/ ... (untouched raw)
        return f"s3://lake/raw/orders/dt={data_interval_start:%Y-%m-%d}/"

    @task(outlets=[ORDERS_MART])
    def load_partition(raw_path: str, ds=None) -> None:
        """PATTERN 2 — idempotent partition overwrite.

        DELETE the logical partition, then INSERT, inside one transaction.
        Running this twice yields identical results — no dedup jobs needed.
        """
        sql = f"""
            BEGIN;
            DELETE FROM analytics.fct_orders WHERE event_date = '{ds}';
            INSERT INTO analytics.fct_orders
            SELECT * FROM staging.load_orders('{raw_path}');
            COMMIT;
        """
        # execute sql against the warehouse

    @task
    def quality_gate(ds=None) -> None:
        """PATTERN 3 — hard quality gate before publishing.

        Raise (fail the task) so downstream consumers never see bad data.
        """
        checks = {
            "pk_unique": "SELECT COUNT(*) - COUNT(DISTINCT order_line_sk) FROM ...",
            "row_count_sane": "-- fail if outside +/-30% of 7-day average",
        }
        for name, _sql in checks.items():
            # result = run(_sql); if failed: raise ValueError(f"{name} failed for {ds}")
            pass

    load = load_partition(extract_orders())
    load >> quality_gate()


orders_daily()


# PATTERN 4 — downstream DAG triggered by data, not by clock:
#
# @dag(schedule=[ORDERS_MART], start_date=datetime(2026, 1, 1), catchup=False)
# def orders_reporting():
#     ...runs whenever fct_orders is updated, including backfills.
