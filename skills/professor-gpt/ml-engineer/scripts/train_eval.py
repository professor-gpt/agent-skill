#!/usr/bin/env python3
"""
Reference tabular ML pipeline: baseline -> leak-proof preprocessing ->
cross-validated model -> single final test evaluation.

Usage:
    python train_eval.py --csv data.csv --target churned
    python train_eval.py                      # runs on a synthetic demo dataset

Requires: scikit-learn >= 1.3, pandas, numpy
"""
import argparse

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import (average_precision_score, classification_report,
                             roc_auc_score)
from sklearn.model_selection import StratifiedKFold, cross_val_score, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

RANDOM_STATE = 42  # pin seeds: reproducibility is non-negotiable


def load_data(csv_path: str | None, target: str):
    if csv_path:
        df = pd.read_csv(csv_path)
        y = df.pop(target)
        return df, y
    # Synthetic demo: 5k rows, mixed types, mild class imbalance (~20% positive)
    rng = np.random.default_rng(RANDOM_STATE)
    n = 5000
    df = pd.DataFrame({
        "tenure_months": rng.integers(0, 72, n),
        "monthly_spend": rng.gamma(2.0, 30.0, n),
        "support_tickets": rng.poisson(1.5, n),
        "plan": rng.choice(["basic", "pro", "enterprise"], n, p=[0.6, 0.3, 0.1]),
    })
    logit = -2.2 + 0.5 * df["support_tickets"] - 0.03 * df["tenure_months"]
    y = pd.Series(rng.random(n) < 1 / (1 + np.exp(-logit)), name="churned").astype(int)
    return df, y


def build_pipeline(df: pd.DataFrame) -> Pipeline:
    """Preprocessing lives INSIDE the pipeline so it is fit only on training
    folds -- this is what prevents leakage during cross-validation."""
    num_cols = df.select_dtypes(include="number").columns.tolist()
    cat_cols = df.select_dtypes(exclude="number").columns.tolist()
    pre = ColumnTransformer([
        ("num", Pipeline([("impute", SimpleImputer(strategy="median")),
                          ("scale", StandardScaler())]), num_cols),
        ("cat", Pipeline([("impute", SimpleImputer(strategy="most_frequent")),
                          ("ohe", OneHotEncoder(handle_unknown="ignore"))]), cat_cols),
    ])
    model = HistGradientBoostingClassifier(random_state=RANDOM_STATE)
    return Pipeline([("pre", pre), ("model", model)])


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", default=None, help="Path to CSV (default: synthetic demo)")
    ap.add_argument("--target", default="churned", help="Target column name")
    args = ap.parse_args()

    X, y = load_data(args.csv, args.target)

    # 1) Split FIRST, before any analysis or fitting. Stratify to preserve
    #    class balance. NOTE: use a time-based split for temporal data and
    #    GroupKFold when the same entity can appear in multiple rows.
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=RANDOM_STATE)

    # 2) Dumb baseline -- the number every model must beat meaningfully.
    baseline = DummyClassifier(strategy="prior").fit(X_train, y_train)
    base_ap = average_precision_score(y_test, baseline.predict_proba(X_test)[:, 1])
    print(f"[baseline] PR-AUC = {base_ap:.4f}  (positive rate = {y.mean():.3f})")

    # 3) Cross-validate on TRAIN ONLY. Report mean +/- std: an "improvement"
    #    inside the noise band is not an improvement.
    pipe = build_pipeline(X)
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)
    scores = cross_val_score(pipe, X_train, y_train, cv=cv,
                             scoring="average_precision", n_jobs=-1)
    print(f"[cv] PR-AUC = {scores.mean():.4f} +/- {scores.std():.4f}  {np.round(scores, 4)}")

    # 4) Fit on full training set, evaluate ONCE on the held-out test set.
    pipe.fit(X_train, y_train)
    proba = pipe.predict_proba(X_test)[:, 1]
    print("\n[test] final held-out evaluation (touch this set exactly once):")
    print(f"  PR-AUC : {average_precision_score(y_test, proba):.4f}  (baseline {base_ap:.4f})")
    print(f"  ROC-AUC: {roc_auc_score(y_test, proba):.4f}")
    print(classification_report(y_test, (proba >= 0.5).astype(int), digits=3))
    print("Next steps: error analysis on false negatives, per-segment slices,")
    print("calibration check before thresholding, log run to experiment tracker.")


if __name__ == "__main__":
    main()
