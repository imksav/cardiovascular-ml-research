# Research Protocol — Completed Analytical Specification

**Study:** Cardiovascular Machine Learning Research: BRFSS-Based Classification of Prevalent Self-Reported Myocardial Infarction and Coronary Heart Disease with Temporal Validation

**Status:** Records the completed experimental implementation. This is an analytical specification for reproducibility, **not** a claim of a preregistered protocol or an independent clinical validation study.

## Design and Scope

Retrospective, cross-sectional machine-learning classification using CDC BRFSS annual survey samples. Models were developed on **2023** data and evaluated on an untouched 2023 test sample, followed by **cross-year evaluation on 2025 data**. BRFSS 2024 was inspected but excluded from the locked six-feature transfer because `BPHIGH6` was not compatible in the required form.

**Outcome:** binary `_MICHD`, mapped `1` → reported MI/CHD, `2` → no reported MI/CHD; other/unknown outcome records excluded. The task is classification of **prevalent self-reported MI/CHD**, not prospective risk prediction.

## Analytical Population and Predictors

- BRFSS 2023: **433,323** respondent records; **428,738** known outcomes.
- BRFSS 2025: **356,158** respondent records; **352,145** known outcomes.
- Six model predictors: `AGE_GROUP`, `PHYSICAL_ACTIVITY`, `SMOKING_STATUS`, `BLOOD_PRESSURE`, `DIABETES_STATUS` and `BMI`.
- Source fields: `_AGEG5YR`, `EXERANY2`, `_SMOKER3`, `BPHIGH6`, `DIABETE4`, `_BMI5`.
- `CVDINFR4` and `CVDCRHD4` are used to inspect outcome construction **only**; they are excluded from all predictor matrices.
- Survey weight (`_LLCPWT`), stratum (`_STSTR`), PSU (`_PSU`), reporting area and record-identification metadata are **not model predictors**.

## Cleaning and Leakage Controls

1. Preserve the source XPT data and create separate analytical copies.
2. Interpret BRFSS questionnaire special codes before constructing predictors. Convert `_BMI5` to kg/m² by dividing by 100.
3. Treat five predictors as categorical; map their nonresponse to an explicit missing category (`-1`) and one-hot encode. Use **training-derived median imputation** and scaling for continuous BMI.
4. Fit data-dependent preprocessing **inside the training/CV pipelines**. Reuse the locked fitted transformations for validation, test and 2025 evaluation.
5. Use a unique **DataFrame row index** to verify disjoint internal splits. BRFSS `SEQNO` alone is not globally unique and is not a valid sole split key.

## Model Development

| Item | Locked analytical choice |
|---|---|
| Known-outcome 2023 split | Stratified **70% train / 15% validation / 15% test** |
| Internal sample counts | Train **300,116**; validation **64,311**; test **64,311** |
| Reproducibility seed | `42` |
| Candidate classifiers | Logistic Regression, Gaussian Naive Bayes, Decision Tree, Random Forest, Gradient Boosting |
| Hyperparameter search | **3-fold stratified cross-validation** on the training subset; ROC-AUC used to refit search |
| Primary locked classifier | `GradientBoostingClassifier`: `n_estimators=150`, `learning_rate=0.10`, `max_depth=3` |
| Secondary benchmark | Tuned L2 Logistic Regression |
| Decision threshold | **0.152913** (approximately), maximising F1 on the **validation** subset |

Candidate comparison, hyperparameter selection, primary-model choice and threshold selection were completed **before** the held-out test and temporal evaluation. The test or 2025 samples were not used to change the primary classifier, feature set or operating threshold.

## Evaluation

- **2023 held-out:** 64,311 records; report ROC-AUC, Average Precision (AP), Brier score, precision, sensitivity, specificity, F1, accuracy, confusion matrix and calibration.
- **2025 temporal:** Apply the **frozen 2023 pipeline and fixed threshold** to 352,145 known-outcome records. No refitting, 2025-specific imputation, threshold tuning or probability recalibration.
- **Calibration and distribution shift:** Compare calibration intercept/slope, mean predicted versus observed outcome rate, Brier skill, predictor-distribution changes and missingness.
- **Survey-weighted sensitivity:** Use `_LLCPWT` for **evaluation metric point estimates only**; do not claim design-corrected confidence intervals or population-level inference without appropriate complex-survey methods.
- **Importance and robustness:** Held-out permutation importance of the six original model inputs (ROC-AUC, five repetitions), age/predictor subgroup comparisons, missingness profiles and ±20% local threshold sensitivity checks. Importance is **model reliance**, not a causal estimate.

## Recorded Primary Results

| Metric | 2023 held-out | 2025 temporal |
|---|---:|---:|
| ROC-AUC | 0.80115 | 0.79486 |
| Average Precision | 0.24486 | 0.24877 |
| Brier score | 0.06969 | 0.07382 |
| Sensitivity, locked threshold | 0.56280 | 0.56181 |
| Specificity, locked threshold | 0.82954 | 0.81994 |
| F1, locked threshold | 0.33055 | 0.33215 |

The AP comparison is affected by changing outcome prevalence; a higher AP in 2025 is **not** proof of improved discrimination. These are descriptive performance results, not evidence of clinical effectiveness.

## Reproducibility and Interpretation

The primary executable record is [`../notebooks/03_brfss_2023_first_look_optimised.ipynb`](../notebooks/03_brfss_2023_first_look_optimised.ipynb). Saved tables, models, software versions, dataset provenance and research manifest belong under `artifacts/` at the **repository root**.

Important limitations: cross-sectional and self-reported variables, uncertain temporal ordering of predictors versus earlier diagnoses, six-predictor restriction, nonuniform sensitivity across age bands, incomplete-data effects and no cross-dataset clinical validation. Model revisions after this locked experiment require a separately documented analysis, not silent alteration of the final results.

The earlier MSc dissertation may be referenced for historical context, but its old experiments and near-perfect results are **not empirical evidence** for this BRFSS study.
