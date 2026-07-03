-- =====================================================================
-- Incremental fact model template (dbt)
-- Grain: one row per <business event, e.g. completed order line>
-- Owner: <team>  |  SLA: <freshness, e.g. hourly by :15>
-- =====================================================================
-- Conventions enforced by this template:
--   * merge on a surrogate key, partition-pruned by event_date
--   * 3-day lookback to absorb late-arriving events
--   * staging -> logic -> final CTE structure, one concern per CTE
-- =====================================================================

{{
    config(
        materialized='incremental',
        incremental_strategy='merge',
        unique_key='order_line_sk',
        partition_by={'field': 'event_date', 'data_type': 'date'},
        cluster_by=['customer_id'],
        on_schema_change='append_new_columns',
        tags=['hourly', 'finance']
    )
}}

with

-- 1. Source data: only ref() staging models, never raw sources here
orders as (

    select * from {{ ref('stg_shop__orders') }}

    {% if is_incremental() %}
    -- Lookback window: reprocess trailing 3 days every run so
    -- late-arriving and updated events are picked up idempotently.
    where event_date >= dateadd('day', -3, (select max(event_date) from {{ this }}))
    {% endif %}

),

customers as (

    select * from {{ ref('dim_customer') }}
    where is_current  -- SCD2: join current version only; use
                      -- valid_from/valid_to range join for point-in-time

),

-- 2. Business logic: one transformation concern per CTE, no nesting
order_lines_enriched as (

    select
        {{ dbt_utils.generate_surrogate_key(['orders.order_id', 'orders.line_number']) }}
            as order_line_sk,
        orders.order_id,
        orders.line_number,
        orders.event_date,
        orders.event_at,                          -- UTC, event time
        customers.customer_sk,
        orders.customer_id,
        orders.product_id,
        orders.quantity,
        orders.unit_price_usd,
        orders.quantity * orders.unit_price_usd   as gross_revenue_usd,
        orders.loaded_at                          -- lineage watermark

    from orders
    left join customers
        on orders.customer_id = customers.customer_id

),

-- 3. Final select: column order matches YAML docs, no logic here
final as (

    select * from order_lines_enriched

)

select * from final

-- =====================================================================
-- Companion schema.yml (required):
--   * unique + not_null on order_line_sk        (severity: error)
--   * relationships customer_sk -> dim_customer (severity: error)
--   * row-count vs 7-day average +/-30%         (severity: warn)
-- =====================================================================
