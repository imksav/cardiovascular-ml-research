# Research Questions

**Study:** Cardiovascular Machine Learning Research: BRFSS-Based Classification of Prevalent Self-Reported Myocardial Infarction and Coronary Heart Disease with Temporal Validation

**Status:** Aligned with the completed BRFSS 2023 development and BRFSS 2025 temporal-evaluation analysis. Questions describe analyses already performed; journal framing and literature positioning remain subject to manuscript review.

## Main Research Question

How consistently do machine-learning classifiers developed using BRFSS 2023 identify **prevalent self-reported myocardial infarction and/or coronary heart disease (MI/CHD)** when applied, without refitting, to an independent BRFSS 2025 survey-year sample?

## Secondary Research Questions

**RQ1 — Model comparison.** How do Gradient Boosting and a Logistic Regression benchmark compare in discrimination and probability performance, and what do the training–validation gaps of alternative classifiers reveal?

**RQ2 — Temporal generalisation.** How do ROC-AUC, Average Precision, Brier score and locked-threshold classification metrics change between the 2023 held-out test sample and the 2025 sample?

**RQ3 — Calibration.** How similar are probability calibration diagnostics across the two evaluation years?

**RQ4 — Predictor reliance.** Which of the six selected predictors most affect held-out discrimination, and how stable is their permutation-importance ranking across years?

**RQ5 — Survey weighting.** How do the evaluation metrics change when BRFSS sampling weights are applied as sensitivity-analysis weights?

**RQ6 — Robustness.** How does performance vary with age bands, predictor-defined subgroups, incomplete predictor information and local changes to the fixed classification threshold?

## Interpretation Boundary

- `_MICHD` describes **prevalent, self-reported MI/CHD**, not incident or future disease.
- The independent 2025 BRFSS sample provides **cross-year temporal evaluation** within the same survey programme, not prospective follow-up of the 2023 respondents or independent clinical validation.
- Feature importance and exploratory associations are **not causal effects**.
- Survey-weighted evaluation results are **point estimates**; full complex-survey uncertainty intervals were not established for model performance.

**Primary implementation:** [`../notebooks/03_brfss_2023_first_look_optimised.ipynb`](../notebooks/03_brfss_2023_first_look_optimised.ipynb).
