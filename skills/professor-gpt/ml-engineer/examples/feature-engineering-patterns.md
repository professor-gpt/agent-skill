# Feature Engineering Patterns (and Their Leakage Guards)

Feature work usually moves the metric more than model swaps. Every pattern
below comes with the leakage trap that most often accompanies it.

## 1. Aggregation features (the workhorse)

For each entity, aggregate its history: counts, sums, means, ratios.

```
user_orders_30d, user_avg_basket_90d, user_refund_ratio,
merchant_chargeback_rate_7d, category_purchase_share
```

**Leakage guard**: aggregate strictly over data BEFORE the prediction
timestamp of each row (point-in-time correctness). `groupby().mean()` over the
whole table computes the answer with future data — the classic silent killer.

## 2. Recency / frequency / tenure

```
days_since_last_purchase, days_since_signup,
purchases_last_7d / purchases_last_90d   (short/long ratio = trend signal)
```

Trend ratios often outrank raw counts in GBM feature importance. Cap extreme
values (e.g., days_since at 365) so cold-start entities don't dominate splits.

## 3. Target encoding for high-cardinality categoricals

Replace category with the historical target mean (city, merchant_id, SKU).
Powerful and dangerous:

- **Always** compute out-of-fold (each row's encoding excludes its own fold).
- Smooth toward the global mean: `enc = (n * cat_mean + k * global_mean) / (n + k)`
  with k ~ 20, so rare categories don't memorize their few labels.
- For temporal data, encode using only past data per row.

If this feels like too much machinery: native categorical support in
LightGBM/CatBoost/HistGradientBoosting is a safer first move.

## 4. Datetime decomposition

```
hour_of_day, day_of_week, is_weekend, is_month_end, days_to_holiday
hour_sin = sin(2*pi*hour/24), hour_cos = cos(2*pi*hour/24)   # cyclic encoding
```

Cyclic encoding matters for linear models and neural nets; tree models can
split raw integers fine. Always store and decompose in UTC, convert to the
user's local timezone only when the behavior being modeled is local (meals,
commutes, store hours).

## 5. Interaction and ratio features

Trees learn interactions, but explicit ratios help even GBMs and are gold for
linear models:

```
spend_per_order = total_spend / (order_count + 1)     # +1 guards div-by-zero
price_vs_category_median = price / category_median_price
support_tickets_per_month = tickets / max(tenure_months, 1)
```

Domain-driven ratios (per-unit, vs-peer-group, share-of-total) beat blind
polynomial expansion — expand the 3–5 you can explain to a stakeholder.

## 6. Missingness as signal

Before imputing, add `feature_is_missing` indicator columns. Whether a user
filled in a phone number is often more predictive than the number itself.
Then impute (median for numeric, "MISSING" category for categoricals) inside
the pipeline so statistics come from training folds only.

## Leakage red-flag review list

- [ ] Any feature that could not be computed at prediction time in production?
- [ ] Any aggregate computed over the full dataset instead of point-in-time?
- [ ] Any scaler/encoder/imputer fit outside the CV pipeline?
- [ ] Any feature derived from the target or from post-outcome events
      (e.g., `account_closed_date` when predicting churn)?
- [ ] Any join that can pull in rows dated after the label timestamp?
- [ ] Feature importance dominated by one suspicious feature (> 50%)? That is
      leakage until proven innocent — check it first.
