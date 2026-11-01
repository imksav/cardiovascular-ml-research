# Phase 3 – Work Package 1: BRFSS Data Provenance and Dataset Integrity Audit

**Project:** Cardiovascular Disease Prediction Using Machine Learning: A BRFSS-Based Study with Temporal Validation

**Deliverable ID:** PHASE-03-WP1

**Document type:** Technical Audit Record

**Document version:** 1.0.0

**Audit date:** 1 November 2026

**Work package status:** Completed with documented limitations

**Working branch:** `phase/03-data-provenance-audit`

---

## 1. Purpose and position within Phase 3

This document records the data provenance, dataset integrity, schema compatibility and outcome-consistency audit conducted for the BRFSS datasets used in the cardiovascular disease prediction research.

The audit is a supporting technical deliverable within Phase 3. It establishes a traceable record of the source datasets and verifies that the locally stored outcome variable is consistent with the documented CDC calculation rule.

It is not the final report for Phase 3.

Phase 3 contains separate research activities:

| Work package | Description | Status |
|---|---|---|
| WP1 | BRFSS data provenance and dataset integrity audit | Completed with documented limitations |
| WP2 | Scientific manuscript development | Separate ongoing activity |

The completion of this audit does not indicate that manuscript development, journal selection or submission preparation has been completed.

### 1.1 Audit objectives

The audit was conducted to:

1. Record the provenance and integrity of the local BRFSS source files.
2. Calculate and preserve SHA-256 checksums for the inspected datasets.
3. Inspect respondent counts and variable schemas.
4. Verify the availability of the six locked model predictors.
5. Identify annual differences affecting dataset compatibility.
6. Verify the local `_MICHD` outcome against the CDC calculation rule.
7. Profile missingness in the outcome and core predictors.
8. Preserve the original Phase 1 model specification and historical results.
9. Produce reproducible audit artefacts for subsequent manuscript development.

### 1.2 Audit boundaries

The audit was designed as a read-only verification activity.

It did not:

- Retrain or refit the primary Gradient Boosting model.
- Change the six locked predictors.
- Change the outcome definition.
- Modify the historical train, validation or test results.
- Introduce substitute predictors for annual compatibility.
- Replace the Phase 1 computational baseline.
- Claim clinical validation or prospective predictive performance.

---

## 2. Audit outcome at a glance

**Overall audit outcome: `PASS_WITH_DOCUMENTED_LIMITATIONS`**

| Audit area | Finding | Outcome |
|---|---|---|
| Local source-file integrity | File sizes and SHA-256 checksums recorded | Passed |
| Dataset respondent counts | Local counts recorded for all three years | Passed |
| Local schema inspection | No duplicate variable names identified | Passed |
| Predictor availability | All six predictors available in 2023 and 2025 | Passed |
| 2024 compatibility | `BPHIGH6` unavailable | Compatibility audit only |
| `_MICHD` target consistency | Zero mismatches across 1,247,151 records | Passed |
| Missingness profiling | Core-variable profile generated | Completed |
| CDC variable-count reconciliation | Differences remain across official documentation and local files | Open limitation |
| Phase 1 model preservation | No retraining or modification performed | Preserved |

The audit successfully verifies the recorded local dataset properties and `_MICHD` calculation consistency. However, differences in the variable counts reported by CDC documentation and the inspected local files remain documented and require source-version reconciliation before the manuscript is finalised.

---

## 3. Dataset provenance and file integrity

Three annual BRFSS combined landline and cellular telephone datasets were inspected.

### 3.1 Local source files

| Survey year | Repository-relative source file | File size (bytes) | SHA-256 |
|---|---|---:|---|
| 2023 | `data/raw/brfss/2023/LLCP2023.XPT` | 1,205,554,400 | `3d3bf8ef5195bde227828ddc4c90745b76e8b304f8f5b9a043b6d99895fd1615` |
| 2024 | `data/raw/brfss/2024/LLCP2024.XPT` | 1,093,874,240 | `7d53cf088f858e02bcc029a51cf0408cc68f40a0ebeb02a3c0f73058aab36b1c` |
| 2025 | `data/raw/brfss/2025/LLCP2025.XPT` | 799,971,280 | `d99262f8854f018a600c3538ee78e4308569af700abe6b92b36180336c24dec2` |

The SHA-256 values provide local integrity identifiers for the inspected files. They can be used to determine whether the files change during subsequent research activities.

These are locally calculated checksums, not CDC-published checksums.

### 3.2 Raw-data version-control policy

The raw BRFSS XPT files are excluded from Git because of their large file sizes.

The repository retains:

- Dataset provenance metadata.
- File sizes and SHA-256 checksums.
- Audit scripts.
- Machine-readable audit results.
- Relevant archived CDC documentation.

The original raw datasets remain local research inputs and are not committed to the GitHub repository.

---

## 4. Dataset structure and annual compatibility

### 4.1 Local schema inspection

The local XPT files were inspected for respondent counts, variable counts, duplicate variable names and the availability of the required research variables.

| Survey year | Respondents | Variables in local XPT | Required predictors available | Local audit interpretation |
|---|---:|---:|---:|---|
| 2023 | 433,323 | 350 | 6 of 6 | Suitable for model development |
| 2024 | 457,670 | 301 | 5 of 6 | Compatibility audit only |
| 2025 | 356,158 | 283 | 6 of 6 | Suitable for temporal evaluation |

No duplicate variable names were identified in the inspected local schemas.

### 4.2 Predictor availability

The 2023 and 2025 local datasets contain all six locked predictors.

The 2024 local dataset does not contain `BPHIGH6`, the blood-pressure predictor used in the locked model specification.

Consequently:

- 2024 is retained for compatibility and variable-availability assessment only.
- It is not used as a replacement development or temporal evaluation dataset.
- No alternative blood-pressure variable is introduced.
- The six-predictor model specification remains unchanged.

### 4.3 CDC variable-count reconciliation

A source-documentation discrepancy was identified when comparing the local XPT files with CDC's published annual documentation.

| Survey year | Local XPT count | CDC annual data page | CDC cross-year summary table |
|---|---:|---:|---:|
| 2023 | 350 | 345 | 350 |
| 2024 | 301 | 345 | 301 |
| 2025 | 283 | 284 | 284 |

The CDC annual data pages and the CDC cross-year summary table do not report identical counts for every year.

For 2023 and 2024, the local XPT counts agree with the CDC cross-year summary table, but differ from the counts stated on the respective annual data pages.

For 2025, the local XPT contains 283 variables. The archived detailed CDC variable layout also identifies 283 variables, and the local XPT and archived layout have an exact variable-name match. However, the CDC annual data page and cross-year summary table report 284 variables.

These differences are recorded as unresolved documentation and source-version discrepancies.

They must not be silently corrected or interpreted as proof that the local files are identical to every currently published CDC data package.

### 4.4 Source-version verification still required

Before finalising the manuscript's data-source description, the following should be reconciled:

1. The exact CDC release or file version represented by each locally stored XPT file.
2. The difference between the 2023 and 2024 annual-page variable counts and the cross-year summary counts.
3. The one-variable difference between the 2025 local XPT/detailed layout and the CDC annual summary.
4. The variable-name lists associated with the relevant CDC releases.

The existing local audit results are retained as observations of the files actually inspected.

---

## 5. Locked outcome and predictor definitions

The audit preserved the outcome and predictor definitions used in the original Phase 1 experiment.

### 5.1 Outcome variable

The target variable is:

`_MICHD`

It represents prevalent self-reported history of myocardial infarction or coronary heart disease.

The source variables used in its derivation are:

- `CVDINFR4`
- `CVDCRHD4`

These source variables are used to calculate the outcome and must not be included as model predictors.

### 5.2 Locked predictor set

| BRFSS source variable | Research variable | Role |
|---|---|---|
| `_AGEG5YR` | `AGE_GROUP` | Age group |
| `EXERANY2` | `PHYSICAL_ACTIVITY` | Physical activity |
| `_SMOKER3` | `SMOKING_STATUS` | Smoking status |
| `BPHIGH6` | `BLOOD_PRESSURE` | Blood-pressure status |
| `DIABETE4` | `DIABETES_STATUS` | Diabetes status |
| `_BMI5` | `BMI` | Body mass index |

The six predictors remain fixed.

### 5.3 Excluded variables

The following variables are explicitly excluded from the ordinary model predictor set:

| Variable | Reason for exclusion |
|---|---|
| `_MICHD` | Target variable |
| `CVDINFR4` | Source variable used to derive the target |
| `CVDCRHD4` | Source variable used to derive the target |
| `_LLCPWT` | Survey weight |
| `_STSTR` | Survey stratum |
| `_PSU` | Primary sampling unit |

Survey-design variables may be retained for appropriately labelled survey-weighted analyses. They are not treated as ordinary model predictors.

---

## 6. `_MICHD` target-consistency verification

### 6.1 CDC calculation rule

The CDC calculated-variable documentation defines `_MICHD` using `CVDINFR4` and `CVDCRHD4`.

The documented logic is:

- `_MICHD = 1` when either source variable indicates a reported heart attack or angina/coronary heart disease.
- `_MICHD = 2` when both source variables indicate that the respondent did not report either condition.
- Otherwise, `_MICHD` is missing.

The audit reapplied this rule to the local annual datasets and compared the expected values with the stored `_MICHD` values.

### 6.2 Verification results

| Survey year | Records checked | Expected defined outcomes | Expected missing outcomes | Observed missing outcomes | Mismatches |
|---|---:|---:|---:|---:|---:|
| 2023 | 433,323 | 428,738 | 4,585 | 4,585 | 0 |
| 2024 | 457,670 | 452,464 | 5,206 | 5,206 | 0 |
| 2025 | 356,158 | 352,145 | 4,013 | 4,013 | 0 |
| **Total** | **1,247,151** | **1,233,347** | **13,804** | **13,804** | **0** |

**Result: Zero mismatches across 1,247,151 inspected records.**

The stored `_MICHD` values agree with the documented CDC derivation rule for all three local datasets.

### 6.3 Interpretation

This verification establishes consistency between the locally stored outcome and the documented CDC calculation rule.

It does not:

- Independently verify the truth of respondents' original survey answers.
- Establish clinical diagnostic accuracy.
- Validate the outcome against medical records.
- Establish prospective disease risk.

The target remains a survey-derived indicator of self-reported prevalent disease history.

---

## 7. Core-variable profile and missingness

A core-variable profile was generated for the outcome, its two source variables and the six locked predictors.

The profile records variable labels and missing-value counts for each survey year.

### 7.1 Key missingness observations

| Variable | 2023 missing values | 2024 missing values | 2025 missing values |
|---|---:|---:|---:|
| `_MICHD` | 4,585 | 5,206 | 4,013 |
| `_BMI5` | 40,535 | 43,037 | 32,562 |
| `BPHIGH6` | Available | Not present in local schema | 2,617 |

The main observations are:

1. `_BMI5` has the highest missingness among the six predictors in each inspected annual dataset.
2. `BPHIGH6` is absent from the local 2024 dataset.
3. `BPHIGH6` has 2,617 missing values in the local 2025 dataset.
4. The missing outcome counts agree with the target-consistency audit.
5. Other core predictors have comparatively low missingness in the inspected files.

### 7.2 Missing predictors in the evaluation samples

The existing evaluation evidence also identifies records with at least one missing predictor.

| Evaluation sample | Records with at least one missing predictor | Total evaluation records | Proportion |
|---|---:|---:|---:|
| 2023 held-out | 8,200 | 64,311 | 12.75% |
| 2025 temporal | 47,595 | 352,145 | 13.52% |

Performance differed between records with complete predictors and records with at least one missing predictor.

This should be considered during manuscript reporting. Missingness should not be treated as inconsequential simply because the existing preprocessing pipeline can process incomplete records.

The detailed profile is retained in:

`artifacts/provenance/phase3_core_variable_profile.csv`

---

## 8. Relationship to the locked Phase 1 experiment

The provenance audit did not retrain or modify the primary Gradient Boosting model.

The following Phase 1 decisions remain unchanged:

- Development dataset: BRFSS 2023.
- Temporal evaluation dataset: BRFSS 2025.
- Secondary compatibility dataset: BRFSS 2024.
- Predictor set: six locked predictors.
- Primary model: Gradient Boosting.
- Secondary model: L2 Logistic Regression.
- Existing preprocessing pipeline.
- Existing classification threshold.
- Historical train, validation, test and temporal evaluation results.

The 2025 dataset remains a temporal evaluation sample. It was not used to refit the model or select a new threshold.

### 8.1 Interpretation safeguards

The audit does not establish that the model is clinically validated or suitable for deployment.

The following limitations remain relevant to the manuscript:

- BRFSS is based on self-reported survey information.
- The datasets are cross-sectional annual survey samples.
- Missingness may affect observed performance.
- Survey-weighted point estimates are not equivalent to full design-based inference.
- Confidence intervals and full complex-survey variance estimation have not been established for the retained weighted results.
- Subgroup performance varies and should not be represented as uniform.

The audit therefore supports data-provenance transparency, not a claim of clinical validity.

---

## 9. Audit implementation and reproducibility

### 9.1 Audit script

The audit was implemented through:

`scripts/audit_brfss_provenance.py`

The script performs read-only checks of the local BRFSS files and supports an optional profile mode.

The profile mode generates the core-variable profile and target-consistency results.

### 9.2 Reproducibility command

From the dedicated audit Python environment containing `pandas` and `pyreadstat`, run:

```bash
python scripts/audit_brfss_provenance.py --profile