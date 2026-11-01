# Project Status

**Research title:** Cardiovascular Machine Learning Research: BRFSS-Based Classification of Prevalent Self-Reported Myocardial Infarction and Coronary Heart Disease with Temporal Validation

**Current milestone:** Phase 3 completed — BRFSS data provenance and dataset integrity audit (WP1), followed by development of the first full scientific manuscript draft (WP2). Completed on 1 November 2026. Phase 4 scientific and reproducibility review is next.

**Release version:** `v0.1.0`

**Release date:** 9 October 2026

**Release status:** Published as a GitHub pre-release.

**Current research stage:** Phase 1 remains locked and complete; Phase 2 is complete for the stated targeted critical narrative/scoping review scope; Phase 3 WP1 and WP2 are complete as research-development deliverables. The first full manuscript draft has been prepared but is not yet submission-ready. Phase 4 will focus on investigating documented data-provenance discrepancies, verifying the manuscript against the locked computational implementation, and completing scientific and reporting-quality checks.

**GitHub Release:** [v0.1.0 — Phase 1: Completed Experimental Analysis](https://github.com/imksav/cardiovascular-ml-research/releases/tag/v0.1.0)

---

## 1. Completed: Phase 1 — Research Implementation

Phase 1 established a reproducible machine-learning workflow for classifying prevalent self-reported myocardial infarction (MI) and/or coronary heart disease (CHD) using CDC Behavioral Risk Factor Surveillance System (BRFSS) survey data.

The primary objective was to develop and evaluate a machine-learning classification model using BRFSS 2023, followed by unchanged-model temporal evaluation using BRFSS 2025.

**Status:** Completed and locked.

### Data Preparation and Research Design

- [x] Inspect BRFSS 2023 source data and variable coding.
- [x] Validate the cardiovascular outcome `_MICHD`.
- [x] Identify and exclude direct target-construction variables to prevent target leakage.
- [x] Establish the final six-predictor analytical specification.
- [x] Apply documented missing-value handling and preprocessing.
- [x] Establish a stratified 70/15/15 training, validation and held-out test split.
- [x] Document dataset selection and cross-year variable compatibility.
- [x] Establish the distinction between model-development data and temporal evaluation data.
- [x] Preserve the original research design and computational decisions.

### Machine-Learning Development

- [x] Compare five candidate machine-learning algorithms.
- [x] Establish Logistic Regression as a comparative benchmark.
- [x] Select and tune the primary Gradient Boosting model.
- [x] Select the classification threshold using validation data.
- [x] Freeze the final model, preprocessing configuration and classification threshold.
- [x] Preserve trained models and reproducibility artefacts.
- [x] Document the final model configuration and analytical specification.

### Model Evaluation

- [x] Evaluate the frozen model on the independent BRFSS 2023 held-out test set.
- [x] Assess BRFSS 2024 variable compatibility.
- [x] Conduct unchanged-model temporal evaluation using BRFSS 2025.
- [x] Evaluate ROC-AUC, average precision, Brier score and classification metrics.
- [x] Examine probability calibration.
- [x] Conduct survey-weighted evaluation sensitivity analyses.
- [x] Evaluate permutation feature importance.
- [x] Assess missing-data robustness and threshold behaviour.
- [x] Examine performance differences across relevant population subgroups.
- [x] Preserve the original results for subsequent manuscript development.

### Final Computational Results

| Evaluation Metric | BRFSS 2023 Held-Out | BRFSS 2025 Temporal |
|---|---:|---:|
| Respondents | 64,311 | 352,145 |
| Outcome prevalence | 8.47% | 9.00% |
| ROC-AUC | **0.8012** | **0.7949** |
| Average Precision | 0.2449 | 0.2488 |
| Brier Score | 0.0697 | 0.0738 |
| Accuracy | 0.8070 | 0.7967 |
| Precision | 0.2340 | 0.2358 |
| Sensitivity | 0.5628 | 0.5618 |
| Specificity | 0.8295 | 0.8199 |
| F1 Score | 0.3305 | 0.3322 |

The approximately 0.0063 decrease in ROC-AUC indicates broadly stable discrimination between the evaluated survey years.

The results demonstrate the performance of the frozen classifier on the selected evaluation samples. They do not establish clinical validity, prospective cardiovascular risk prediction or clinical utility.

### Candidate Model Comparison

Five candidate algorithms were evaluated during the initial model-development process.

| Model | Training ROC-AUC | Validation ROC-AUC |
|---|---:|---:|
| Gradient Boosting | 0.8000 | 0.8017 |
| Logistic Regression | 0.7976 | 0.8011 |
| Gaussian Naive Bayes | 0.7794 | 0.7836 |
| Random Forest | 0.9596 | 0.6830 |
| Decision Tree | 0.9684 | 0.6023 |

The substantial training-to-validation performance differences for Random Forest and Decision Tree indicate overfitting in those candidate configurations. Gradient Boosting was retained as the primary model, with Logistic Regression as a comparative benchmark.

The tuned Logistic Regression model achieved a BRFSS 2025 temporal ROC-AUC of approximately 0.79389, compared with 0.794859 for Gradient Boosting.

### Calibration Results

| Calibration Metric | BRFSS 2023 Held-Out | BRFSS 2025 Temporal |
|---|---:|---:|
| Observed prevalence | 0.084682 | 0.089983 |
| Mean predicted probability | 0.085095 | 0.087874 |
| Observed/expected ratio | 0.99514 | 1.02400 |
| Calibration intercept | 0.05090 | 0.03653 |
| Calibration slope | 1.03032 | 1.00403 |
| Brier skill score | 0.10091 | 0.09856 |

These results describe calibration in the evaluated datasets and should not be interpreted as evidence of clinical calibration or suitability for individual clinical decisions.

### Survey-Weighted Evaluation

Survey-weighted performance estimates were calculated as additional sensitivity analyses.

| Evaluation Metric | BRFSS 2023 | BRFSS 2025 |
|---|---:|---:|
| Weighted prevalence | 0.064299 | 0.067504 |
| ROC-AUC | 0.815409 | 0.822815 |
| Average Precision | 0.211950 | 0.231756 |
| Brier Score | 0.054637 | 0.056374 |
| Accuracy | 0.855872 | 0.858539 |
| Precision | 0.215325 | 0.236242 |
| Sensitivity | 0.469537 | 0.490651 |
| Specificity | 0.882420 | 0.885171 |
| F1 Score | 0.295251 | 0.318926 |

These are survey-weighted point estimates. They do not constitute full complex-survey design-based inference or provide design-based confidence intervals.

### Subgroup Evaluation

Subgroup analysis identified differences in classification performance across age and diabetes groups.

| Subgroup | BRFSS 2023 Finding | BRFSS 2025 Finding |
|---|---|---|
| Age 18–39 | ROC-AUC 0.7123; sensitivity 0 | ROC-AUC 0.7170; sensitivity 0 |
| Age 65–74 | Sensitivity 0.5424; specificity 0.7209 | Sensitivity 0.5420; specificity 0.7140 |
| Age 75+ | ROC-AUC 0.6475; sensitivity 0.8005; specificity 0.4034 | ROC-AUC 0.6397; sensitivity 0.7799; specificity 0.4069 |
| Diabetes subgroup | Evaluated | 2025 sensitivity 0.8296; specificity 0.3831 |

The zero sensitivity in the 18–39 subgroup and comparatively low specificity in the 75+ subgroup are important limitations. The results do not demonstrate uniform subgroup performance or establish fairness.

### Permutation Feature Importance

| Predictor | BRFSS 2023 | BRFSS 2025 |
|---|---:|---:|
| Age group | 0.12832 | 0.13120 |
| Blood pressure | 0.04004 | 0.03867 |
| Diabetes | 0.01882 | 0.01790 |
| Smoking | 0.01485 | 0.01496 |
| Physical activity | 0.00399 | 0.00381 |
| BMI | 0.00162 | 0.00156 |

Age group had the highest permutation importance in both evaluation years, followed by blood pressure and diabetes.

These values describe predictive importance under the implemented evaluation procedure. They must not be interpreted as causal effects.

### Phase 1 Preservation

The Phase 1 experimental specification and results remain locked.

Subsequent literature review, provenance auditing and manuscript development must not silently change the original predictors, outcome, model, preprocessing configuration, threshold or reported computational results.

Any substantive change must be documented as a new analysis or research extension.

---

## 2. Completed: GitHub Repository Establishment

The repository was established with a new Git history and a professional structure for scientific research development.

**Repository:** [cardiovascular-ml-research](https://github.com/imksav/cardiovascular-ml-research)

### Repository Management

- [x] Initialise a fresh Git repository.
- [x] Establish `main` as the stable branch.
- [x] Create the initial Phase 1 research commit.
- [x] Push the completed research snapshot to GitHub.
- [x] Configure `.gitignore` to exclude raw BRFSS datasets, the virtual environment and the local PDF export.
- [x] Establish repository documentation and contribution guidelines.
- [x] Configure GitHub Actions repository-integrity checks.
- [x] Verify successful execution of the initial GitHub Actions workflow.
- [x] Create and push the annotated `v0.1.0` Git tag.
- [x] Publish the Phase 1 GitHub pre-release.

### Included Research Materials

- Final optimised Jupyter notebook.
- HTML research report.
- Frozen Gradient Boosting and Logistic Regression model artefacts.
- Machine-readable experimental results.
- Research figures and visualisations.
- Dataset, model and software provenance records.
- Research methodology and supporting documentation.
- GitHub workflow, issue templates and pull-request guidance.

**Primary notebook:** [03_brfss_2023_first_look_optimised.ipynb](../notebooks/03_brfss_2023_first_look_optimised.ipynb)

**HTML report:** [03_brfss_2023_first_look_optimised.html](../reports/03_brfss_2023_first_look_optimised.html)

**Permanent Phase 1 reference:** [v0.1.0](https://github.com/imksav/cardiovascular-ml-research/releases/tag/v0.1.0)

### Reproducibility Status

The initial repository audit and GitHub Actions checks passed.

These checks validate repository structure and selected file integrity. They do **not** independently demonstrate complete clean-kernel notebook execution, full experimental replication or clinical validation.

The released `v0.1.0` tag preserves the computational baseline for subsequent research development.

---

## 3. Completed: Phase 2 — Literature Review and Research Positioning

**Status:** Completed on 25 October 2026 as a targeted critical narrative/scoping review. This is not an exhaustive systematic review.

**Working branch:** `phase/02-literature-review` (as supplied by the project owner; the ZIP snapshot does not include `.git` metadata).

**Objective:** Establish a verified scientific literature foundation, identify relevant research gaps, and develop a defensible positioning of the completed BRFSS analysis.

### Completed Deliverables

- [x] Review the existing literature files and preserve their established paths.
- [x] Populate `literature/literature_matrix.csv` with 16 core evidence records.
- [x] Add `literature/screening_log.csv`; retain `screening_log_template.csv` as a blank template.
- [x] Update `literature/search_strategy.md` with exploratory queries, accessed source types, access limitations and explicit non-systematic-review status.
- [x] Verify the closest direct comparator, Noh et al. (2026), using BRFSS 2023 and prevalent self-reported MI/CHD.
- [x] Identify Kung et al. (2026) as a temporal-validation analogue for a different cross-sectional outcome.
- [x] Update `docs/PHASE2_RESEARCH_POSITIONING.md`, `docs/PHASE2_FINAL_REPORT.md`, `README.md`, `CHANGELOG.md` and this research log without changing locked Phase 1 results.
- [x] Produce `literature/related_work_synthesis.md` and `literature/references.bib`.
- [x] Deduplicate the seed source list and update source-level verification notes.
- [x] Complete a provisional domain-level PROBAST+AI appraisal and a 52-subitem TRIPOD+AI pre-manuscript audit.
- [x] Identify and preserve unresolved source-version and survey-inference limitations.
- [x] Establish the research-positioning boundaries for the manuscript.

### Scope Boundary (Not a Hidden Unfinished Task)

- The review is **not systematic**: direct Scopus/Web of Science/Embase/IEEE subscription exports, complete result counts, dual independent screening and a PRISMA flow were not performed.
- Some sources were available only through abstracts/indexed publisher results. Those limitations are marked in the matrix and screening log.
- The CDC source-file/column-count discrepancy and author-confirmation items in the TRIPOD+AI audit were carried forward into Phase 3 and Phase 4.
- The existing literature review scope must not be retrospectively described as an exhaustive systematic review.

### Closest Direct Comparator

Noh et al. (2026) was identified as the closest direct comparator because it examined occupational and socioeconomic predictors of prevalent self-reported myocardial infarction and coronary heart disease using BRFSS data.

Its reported Gradient Boosting performance included:

- ROC-AUC 0.867 and PR-AUC 0.389 in the inclusive analysis.
- ROC-AUC 0.858 and PR-AUC 0.372 after removing selected post-diagnosis variables.

These figures are not directly comparable with the present research because predictor sets and analytical methods differ.

### Temporal-Validation Analogue

Kung et al. (2026) was identified as a relevant methodological analogue. The study used BRFSS 2023 for development and BRFSS 2024 for temporal validation, but examined cross-sectional diabetes classification rather than MI/CHD.

### Final Research-Positioning Decision

No “first study” claim is supported.

The candidate contribution is the exact locked six-predictor prevalent MI/CHD application and combined evaluation package, subject to broader searching.

The closest comparator means BRFSS 2023 `_MICHD` classification and leakage awareness are not unique. A separate BRFSS 2023-to-2024 diabetes study also means annual-sample temporal validation is not novel in itself.

### Reporting and Appraisal Frameworks

The review identified two separate frameworks for subsequent manuscript work:

- **TRIPOD+AI:** A reporting guideline for prediction-model studies. Its official checklist contains 27 items. The project's earlier 52-subitem mapping is an expanded internal mapping, not the official checklist item count.
- **PROBAST+AI:** A methodological quality, risk-of-bias and applicability assessment tool. It is distinct from TRIPOD+AI.

### Research Integrity

The completed Phase 1 experimental specification is preserved. Literature findings may refine manuscript framing and interpretation. Any substantive change to the locked predictors, model, outcome, preprocessing or experimental results must be documented as a new analysis or research extension.

---

## 4. Completed: Phase 3 — Data Provenance Audit and Manuscript Development

**Status:** WP1 and WP2 completed as research-development deliverables.

**Completion date:** 1 November 2026.

**Objective:** Establish the provenance and integrity of the BRFSS datasets used in the research, then develop a complete scientific manuscript draft using the locked computational results and verified literature.

Phase 3 consists of two work packages:

- **WP1:** BRFSS data provenance and dataset integrity audit.
- **WP2:** Scientific manuscript development.

Phase 3 did not retrain the Phase 1 model or change the locked experimental specification.

### 4.1. Completed: WP1 — BRFSS Data Provenance and Dataset Integrity Audit

**Audit status:** `PASS_WITH_DOCUMENTED_LIMITATIONS`

**Audit approach:** Read-only verification. The work was designed to assess source integrity, annual compatibility, target consistency and missingness without changing the original computational experiment.

#### Audit Objectives

- [x] Verify the provenance of the local BRFSS 2023, 2024 and 2025 XPT files.
- [x] Record source-file sizes and SHA-256 checksums.
- [x] Verify annual respondent counts against official CDC documentation.
- [x] Compare local variable counts with the official published XPT variable counts.
- [x] Check for duplicate records.
- [x] Verify the availability of the six locked predictors, outcome and survey-design variables.
- [x] Reassess `_MICHD` construction against CDC calculated-variable documentation.
- [x] Profile missingness in the core analytical variables.
- [x] Document annual compatibility limitations.
- [x] Generate machine-readable provenance and audit outputs.
- [x] Preserve the audit as a read-only activity without modifying Phase 1 model artefacts.

#### Source Dataset Integrity Summary

| BRFSS Year | Local Respondents | Local Variables | Official CDC XPT Variables | Duplicate Records | Audit Status |
|---|---:|---:|---:|---:|---|
| 2023 | 433,323 | 350 | 345 | 0 | PASS |
| 2024 | 457,670 | 301 | 345 | 0 | COMPATIBILITY_AUDIT_ONLY |
| 2025 | 356,158 | 283 | 284 | 0 | PASS_WITH_DOCUMENTED_COUNT_DISCREPANCY |

The local respondent counts match the official CDC annual documentation.

However, the local variable counts do not match the official published counts:

- BRFSS 2023: local 350 versus official 345.
- BRFSS 2024: local 301 versus official 345.
- BRFSS 2025: local 283 versus official 284.

These differences remain unresolved. They must be investigated during Phase 4 and must not be described as resolved or silently corrected in the manuscript.

Official CDC annual data documentation:

- [BRFSS 2023 Annual Data](https://www.cdc.gov/brfss/annual_data/annual_2023.html)
- [BRFSS 2024 Annual Data](https://www.cdc.gov/brfss/annual_data/annual_2024.html)
- [BRFSS 2025 Annual Data](https://www.cdc.gov/brfss/annual_data/annual_2025.html)

#### Local XPT File Provenance

| Dataset | File Size (Bytes) | SHA-256 |
|---|---:|---|
| `LLCP2023.XPT` | 1,205,554,400 | `3d3bf8ef5195bde227828ddc4c90745b76e8b304f8f5b9a043b6d99895fd1615` |
| `LLCP2024.XPT` | 1,093,874,240 | `7d53cf088f858e02bcc029a51cf0408cc68f40a0ebeb02a3c0f73058aab36b1c` |
| `LLCP2025.XPT` | 799,971,280 | `d99262f8854f018a600c3538ee78e4308569af700abe6b92b36180336c24dec2` |

Raw BRFSS XPT files remain excluded from Git.

#### Annual Variable Compatibility

The 2024 local dataset does not contain `BPHIGH6`, one of the six locked predictors.

Consequently:

- BRFSS 2024 is retained for compatibility auditing.
- It is not treated as an equivalent six-predictor evaluation dataset.
- No substitute blood-pressure variable has been introduced.
- The locked Phase 1 temporal evaluation remains based on BRFSS 2025.

The 2025 local XPT and archived detailed layout both contain 283 variables, whereas the official annual page reports 284. This remains a documented discrepancy.

#### `_MICHD` Target Consistency

The CDC construction rule was checked against the local datasets:

- `_MICHD = 1` when `CVDINFR4 = 1` or `CVDCRHD4 = 1`.
- `_MICHD = 2` when both source variables equal 2.
- Otherwise, `_MICHD` is missing.

| BRFSS Year | Records Checked | Expected Defined | Expected Missing | Observed Missing | Mismatches |
|---|---:|---:|---:|---:|---:|
| 2023 | 433,323 | 428,738 | 4,585 | 4,585 | 0 |
| 2024 | 457,670 | 452,464 | 5,206 | 5,206 | 0 |
| 2025 | 356,158 | 352,145 | 4,013 | 4,013 | 0 |
| **Total** | **1,247,151** | **1,233,347** | **13,804** | **13,804** | **0** |

The local `_MICHD` values are consistent with the CDC construction rule across all three annual datasets.

This verifies consistency with the documented formula, not the independent clinical truth of respondents' self-reported answers.

#### Locked Predictor Specification

| Source Variable | Analytical Variable |
|---|---|
| `_AGEG5YR` | `AGE_GROUP` |
| `EXERANY2` | `PHYSICAL_ACTIVITY` |
| `_SMOKER3` | `SMOKING_STATUS` |
| `BPHIGH6` | `BLOOD_PRESSURE` |
| `DIABETE4` | `DIABETES_STATUS` |
| `_BMI5` | `BMI` |

The outcome remains `_MICHD`.

`CVDINFR4` and `CVDCRHD4` are used for outcome construction verification and must not be included as model predictors.

Survey-design variables `_LLCPWT`, `_STSTR` and `_PSU` are not ordinary model predictors. Survey weights may be used for explicitly labelled weighted analyses.

#### Missingness Profile

The audit identified missingness in the core analytical variables.

BMI had the largest predictor-level missingness.

| Variable | BRFSS 2023 Missing Count | BRFSS 2024 Missing Count | BRFSS 2025 Missing Count |
|---|---:|---:|---:|
| `_BMI5` | 40,535 | 43,037 | 32,562 |
| `_MICHD` | 4,585 | 5,206 | 4,013 |
| `BPHIGH6` | Not separately listed in this summary | Variable absent locally | 2,617 |

The exact annual missingness profile should be taken from `phase3_core_variable_profile.csv` during Phase 4 verification.

The proportion of evaluation records with at least one missing predictor was:

- BRFSS 2023: 12.75%.
- BRFSS 2025: 13.52%.

The predictor missingness rates in the two evaluation datasets were:

| Predictor | BRFSS 2023 Missing | BRFSS 2025 Missing |
|---|---:|---:|
| Blood pressure | 0.3685% | 1.1433% |
| Smoking | 5.3754% | 5.7454% |
| Age | 1.7182% | 1.8345% |
| Physical activity | 0.2224% | 0.2567% |
| Diabetes | 0.1570% | 0.1656% |
| BMI | 9.1959% | 9.0644% |

#### Missing-Predictor Robustness Comparison

| Evaluation Year | Record Group | n | Outcome Prevalence | ROC-AUC | Sensitivity |
|---|---|---:|---:|---:|---:|
| 2023 | At least one missing predictor | 8,200 | 0.06976 | 0.78334 | 0.4406 |
| 2023 | Complete predictors | 56,111 | 0.08686 | 0.80268 | 0.5771 |
| 2025 | At least one missing predictor | 47,595 | 0.07450 | 0.78631 | 0.4659 |
| 2025 | Complete predictors | 304,550 | 0.09240 | 0.79531 | 0.5739 |

These differences are retained as robustness evidence and research limitations. They do not justify silently changing the locked model or its reported results.

#### Audit Artefacts

The audit work produced or updated the following research artefacts:

- `scripts/audit_brfss_provenance.py`
- `artifacts/provenance/phase3_dataset_audit.json`
- `artifacts/provenance/phase3_dataset_audit.csv`
- `artifacts/provenance/phase3_target_consistency.json`
- `artifacts/provenance/phase3_core_variable_profile.csv`
- `artifacts/provenance/dataset_provenance.csv`
- `artifacts/provenance/dataset_provenance.json`
- `docs/references/cdc/llcp_varlayout_25_onecolumn.html`
- Companion assets for the archived 2025 CDC detailed variable layout.

The archived 2025 CDC layout has a recorded SHA-256 checksum:

`472BDC94C7E55928CDF312FCC354066424953A4646F9CCDE6B94A7F84E8DDC11`

Official source:

`https://www.cdc.gov/brfss/annual_data/2025/llcp_varlayout_25_onecolumn.html`

#### Audit Reproducibility

The documented audit command is:

```bash
python scripts/audit_brfss_provenance.py --profile
```

The audit requires an environment with the relevant dependencies, including `pandas` and `pyreadstat`.

The existing `.venv` does not contain `pyreadstat`. The dedicated audit environment was used for the audit work.

The old notebook cell 442 in `notebooks/03_brfss_2023_first_look_optimised.ipynb` must not be run for this audit workflow because it overwrites provenance outputs for 2023 and 2025 only and drops the 2024 record.

The audit script and generated outputs should remain the authoritative Phase 3 audit workflow.

#### WP1 Completion Decision

WP1 is complete as a data-provenance and integrity audit.

The overall status remains `PASS_WITH_DOCUMENTED_LIMITATIONS` because the annual variable-count discrepancies are unresolved and 2024 does not contain the complete locked predictor set.

No Phase 1 model retraining or experimental modification was performed.

**Repository integration note:** The audit work and local artefacts are recorded as completed research work. Their Git commit, push, tag and GitHub release status must be verified before claiming that a Phase 3 audit release has been published.

### 4.2. Completed: WP2 — Scientific Manuscript Development

**Status:** First full working manuscript draft completed.

**Manuscript title:**

*Temporal evaluation of a six-predictor Gradient Boosting classifier for prevalent self-reported myocardial infarction or coronary heart disease using BRFSS 2023 and 2025*

**Objective:** Develop a scientifically structured manuscript using the locked computational results, Phase 2 literature positioning and Phase 3 data-provenance findings.

#### Completed Manuscript Components

- [x] Develop a structured abstract.
- [x] Draft the Introduction and research positioning.
- [x] Consolidate the approved Methods draft.
- [x] Prepare the Results section and numerical tables.
- [x] Draft the Discussion.
- [x] Document strengths and limitations.
- [x] Prepare the Conclusion.
- [x] Include references and reporting-framework considerations.
- [x] Identify declarations and author-confirmation placeholders.
- [x] Explicitly distinguish prevalent self-reported disease classification from prospective cardiovascular risk prediction.
- [x] Preserve the limitations of cross-sectional survey data and survey-weighted point estimates.
- [x] Carry forward unresolved provenance and reproducibility questions for Phase 4.

#### Manuscript Structure

The first full draft contains:

1. Structured abstract.
2. Introduction and research rationale.
3. Methods:
   - Study design.
   - Data sources.
   - Outcome definition.
   - Predictor selection.
   - Data preprocessing.
   - Model development.
   - Internal evaluation.
   - Temporal evaluation.
   - Performance metrics.
   - Survey-weighted sensitivity analyses.
   - Missingness and subgroup analyses.
   - Software and reproducibility.
   - Ethics considerations.
4. Results:
   - Dataset characteristics.
   - Target consistency.
   - Candidate-model comparison.
   - Held-out evaluation.
   - Temporal evaluation.
   - Calibration.
   - Survey-weighted results.
   - Missingness findings.
   - Permutation feature importance.
   - Subgroup findings.
5. Discussion:
   - Principal findings.
   - Comparison with prior literature.
   - Interpretation of temporal performance.
   - Strengths.
   - Limitations.
   - Implications for further research.
6. Conclusion.
7. Declarations.
8. References.

#### Locked Model Specification Used in the Manuscript

The manuscript reports the existing Phase 1 specification:

| Component | Locked Specification |
|---|---|
| Primary model | Gradient Boosting |
| Secondary comparator | L2 Logistic Regression |
| Development dataset | BRFSS 2023 |
| Temporal evaluation dataset | BRFSS 2025 |
| Predictors | Six locked analytical predictors |
| Number of estimators | 150 |
| Learning rate | 0.1 |
| Maximum depth | 3 |
| Random seed | 42 |
| Classification threshold | 0.152913 |
| Data split | Stratified 70/15/15 |
| Cross-validation | Three-fold stratified CV on training subset |
| Temporal model handling | Frozen model; no refitting on BRFSS 2025 |

The preprocessing description in the working manuscript includes:

- Five categorical predictors and one numerical predictor (BMI).
- Categorical missing values encoded as `-1`.
- One-hot encoding with predefined category domains.
- BMI median imputation and standard scaling.
- A `ColumnTransformer` and scikit-learn pipeline.
- Unknown categories ignored.
- BMI `_BMI5` divided by 100.

These implementation details and the software versions remain subject to verification against the original notebook, `final_model_specification.csv` and saved provenance records during Phase 4.

#### Main Manuscript Performance Results

| Evaluation Metric | BRFSS 2023 Held-Out | BRFSS 2025 Temporal |
|---|---:|---:|
| Respondents | 64,311 | 352,145 |
| Outcome prevalence | 8.47% | 9.00% |
| ROC-AUC | **0.8012** | **0.7949** |
| Average Precision | 0.2449 | 0.2488 |
| Brier Score | 0.0697 | 0.0738 |
| Accuracy | 0.8070 | 0.7967 |
| Precision | 0.2340 | 0.2358 |
| Sensitivity | 0.5628 | 0.5618 |
| Specificity | 0.8295 | 0.8199 |
| F1 Score | 0.3305 | 0.3322 |

The temporal ROC-AUC decreased by approximately 0.0063. Average precision and F1 were slightly higher in the 2025 evaluation, while the Brier score and accuracy were less favourable.

These results should be interpreted as temporal evaluation of a frozen classifier, not prospective prediction or clinical validation.

#### Calibration Findings Included in the Manuscript

| Calibration Metric | BRFSS 2023 | BRFSS 2025 |
|---|---:|---:|
| Observed prevalence | 0.084682 | 0.089983 |
| Mean predicted probability | 0.085095 | 0.087874 |
| Observed/expected ratio | 0.99514 | 1.02400 |
| Calibration intercept | 0.05090 | 0.03653 |
| Calibration slope | 1.03032 | 1.00403 |
| Brier skill score | 0.10091 | 0.09856 |

#### Survey-Weighted Results Included in the Manuscript

| Evaluation Metric | BRFSS 2023 | BRFSS 2025 |
|---|---:|---:|
| Weighted prevalence | 0.064299 | 0.067504 |
| ROC-AUC | 0.815409 | 0.822815 |
| Average Precision | 0.211950 | 0.231756 |
| Brier Score | 0.054637 | 0.056374 |
| Accuracy | 0.855872 | 0.858539 |
| Precision | 0.215325 | 0.236242 |
| Sensitivity | 0.469537 | 0.490651 |
| Specificity | 0.882420 | 0.885171 |
| F1 Score | 0.295251 | 0.318926 |

These estimates are reported as weighted point estimates, not full complex-survey inferential results.

#### Subgroup Findings Included in the Manuscript

The manuscript retains the observed variation in subgroup performance:

- Age 18–39: ROC-AUC 0.7123 in 2023 and 0.7170 in 2025, with zero sensitivity in both years at the locked threshold.
- Age 65–74: sensitivity 0.5424 in 2023 and 0.5420 in 2025.
- Age 75+: ROC-AUC 0.6475 in 2023 and 0.6397 in 2025, with specificity around 0.40 in both years.
- Diabetes subgroup in 2025: sensitivity 0.8296 and specificity 0.3831.

These results do not demonstrate uniform performance or fairness across population subgroups.

#### Feature-Importance Findings Included in the Manuscript

Permutation importance ranked age group highest in both years, followed by blood pressure and diabetes.

The manuscript explicitly avoids interpreting feature importance as evidence of causality.

#### Figures Referenced in the Manuscript

The working manuscript references the following existing research figures:

- `notebooks/artifacts/figures/roc_internal_vs_temporal.png`
- `notebooks/artifacts/figures/calibration_internal_vs_temporal.png`
- `notebooks/artifacts/figures/permutation_importance_cross_year.png`

The relative paths from `docs/manuscript/` are intended to be:

- `../../notebooks/artifacts/figures/roc_internal_vs_temporal.png`
- `../../notebooks/artifacts/figures/calibration_internal_vs_temporal.png`
- `../../notebooks/artifacts/figures/permutation_importance_cross_year.png`

Their actual existence, visual quality and consistency with the manuscript must be checked during Phase 4.

#### Reporting Frameworks and Research References

The manuscript uses the Phase 2 literature foundation and carries forward the reporting-framework work.

Key references include:

- Noh J, Kim Y, Lim C, Cho SY, Kwon Y, Lee ES, Kim WK, Kim YH, Kim K. *Occupational and socioeconomic predictors of myocardial infarction and coronary heart disease: a machine learning analysis.* BMC Public Health. 2026;26:2015. DOI: `10.1186/s12889-026-27570-3`.
- Kung WM, Yeh HC, Huang APH, Islam MM, Wu CC, Wang YC. *Machine Learning with Social Determinants of Health for Cross-Sectional Diabetes Classification: Development and Temporal Validation.* International Journal of Medical Sciences. 2026;23(11):3323–3335. DOI: `10.7150/ijms.137605`.
- Collins GS et al. *TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods.* BMJ. 2024;385:e078378. DOI: `10.1136/bmj-2023-078378`.
- Moons KGM et al. *PROBAST+AI: a tool to assess risk of bias and applicability of prediction model studies.* BMJ. 2025;388:e082505. DOI: `10.1136/bmj-2024-082505`.

The official TRIPOD+AI checklist contains 27 items. The project's 52-subitem mapping is an expanded internal assessment and must not be presented as the official checklist.

#### Declarations and Author Confirmation

The working manuscript includes placeholders where author or institutional confirmation is required.

The following must not be invented or assumed:

- Institutional ethics approval, exemption or non-human-subjects determination.
- Author affiliations.
- Corresponding-author email.
- ORCID identifiers.
- Funding statement.
- Competing-interest declaration.
- Author contributions.
- Acknowledgements.
- AI-assisted writing disclosure.

These remain Phase 4 verification items.

#### Manuscript Artefact and Repository Integration

**Intended manuscript path:**

`docs/manuscript/manuscript_full.md`

**Intended submission-readiness checklist path:**

`docs/manuscript/08_submission_readiness_checklist.md`

The first full manuscript draft and checklist content have been prepared in the project workflow. Their repository integration, file creation, Git commit and push must be completed and verified before claiming that the files are published in the repository.

#### WP2 Completion Decision

WP2 is complete as a manuscript-development milestone because the first full working draft has been prepared, including the major scientific sections, results and declarations requiring confirmation.

The manuscript is **not submission-ready**.

Scientific verification, exact implementation checks, final references, author declarations and repository integration remain outstanding.

### 4.3. Phase 3 Overall Completion Decision

Phase 3 is considered complete as a research-development and drafting milestone:

- WP1 established the BRFSS data-provenance and integrity audit.
- WP2 produced the first full scientific manuscript draft.
- Phase 1 computational results remain locked.
- Phase 2 literature review and research-positioning decisions remain preserved.
- The CDC local-versus-official variable-count discrepancies remain documented.
- The manuscript is not yet submission-ready.
- Repository integration and Git publication of the Phase 3 deliverables remain to be verified.

**Phase 3 completion does not mean the manuscript has been submitted, accepted or published.**

---

## 5. Future Research Phases

| Phase | Scope | Status |
|---|---|---|
| Phase 1 | Computational research implementation and validation | Completed and locked |
| Phase 2 | Literature review and research positioning | Completed — targeted narrative/scoping review; not systematic |
| Phase 3 | Data provenance audit and scientific manuscript development | Completed — WP1 and WP2 |
| Phase 4 | Scientific review and reproducibility verification | Next |
| Phase 5 | Journal selection, submission and publication preparation | Not started |

### Phase 4 — Scientific and Reproducibility Review

**Status:** Not started.

**Objective:** Conduct a critical scientific, methodological and reproducibility review of the complete manuscript and supporting research artefacts before journal submission preparation.

#### Phase 4 Execution Order

The work should be conducted in the following order:

1. **Repository and working-state inventory**
   - Confirm the current Git branch.
   - Check the working tree for modified, untracked or staged files.
   - Record the latest local commit.
   - Identify which Phase 3 documents and artefacts exist locally.
   - Confirm which files have already been committed or pushed.
   - Avoid overwriting existing work.

2. **Data-provenance investigation**
   - Reconcile the local and official CDC XPT variable-count discrepancies.
   - Check source versions, file integrity, layouts and variable definitions.
   - Document any discrepancy that cannot be conclusively resolved.

3. **Implementation-to-manuscript verification**
   - Compare the manuscript Methods against the original locked notebook.
   - Verify `final_model_specification.csv` and the saved model artefacts.
   - Establish traceability between each reported method and its implementation.

4. **Numerical and figure verification**
   - Recheck every reported metric against the saved outputs.
   - Verify the tables, figures, subgroup analyses and calibration results.
   - Check all manuscript references and relative file paths.

5. **Reproducibility review**
   - Confirm the recorded software versions.
   - Review the environment and dependency documentation.
   - Assess whether the preserved computational baseline can be reproduced without changing the original specification.

6. **Scientific and reporting review**
   - Complete the official TRIPOD+AI checklist.
   - Revisit the PROBAST+AI appraisal.
   - Review scientific interpretation and limitations.
   - Confirm ethics and author declarations.

7. **Internal manuscript review**
   - Resolve factual and methodological inconsistencies.
   - Record any remaining limitations.
   - Establish whether the manuscript meets the project's internal submission-readiness criteria.

#### Planned Activities

- [ ] Reconcile the local and official CDC XPT variable-count discrepancies for BRFSS 2023, 2024 and 2025.
- [ ] Investigate the difference between local and official variable counts without modifying the locked Phase 1 results.
- [ ] Document the source of each discrepancy where possible.
- [ ] Retain a transparent unresolved-discrepancy record where the available evidence is insufficient to establish a definitive explanation.
- [ ] Verify all Methods details against the original locked notebook.
- [ ] Verify the final model configuration against `final_model_specification.csv`.
- [ ] Confirm that the model, preprocessing pipeline and threshold match the preserved Phase 1 artefacts.
- [ ] Verify categorical missing-value handling and one-hot-encoding domains.
- [ ] Verify BMI transformation, median imputation and scaling.
- [ ] Verify the BRFSS 2023 training, validation and test split.
- [ ] Verify the validation-based threshold-selection procedure.
- [ ] Verify that BRFSS 2025 temporal evaluation did not retrain or refit the frozen model.
- [ ] Confirm exact Python, pandas, NumPy, scikit-learn and other relevant software versions from the provenance records.
- [ ] Verify all numerical values in the abstract, tables and Results section.
- [ ] Verify all figures and their underlying data.
- [ ] Check all references, DOIs, citations and relative links.
- [ ] Verify the existence and integrity of all referenced research artefacts.
- [ ] Review the complete manuscript for scientific consistency and unsupported claims.
- [ ] Complete a clean-environment reproducibility review without silently changing Phase 1.
- [ ] Confirm the appropriate institutional ethics determination with the relevant author or institution.
- [ ] Confirm author affiliations and corresponding-author details.
- [ ] Confirm ORCID identifiers, funding, competing interests, author contributions and acknowledgements.
- [ ] Confirm any required AI-assisted writing disclosure.
- [ ] Complete the official 27-item TRIPOD+AI reporting checklist.
- [ ] Revisit the PROBAST+AI methodological quality, risk-of-bias and applicability appraisal.
- [ ] Confirm that the study's cross-sectional design and limitations are consistently reported.
- [ ] Confirm that the manuscript does not overstate clinical validity, prospective prediction, causality or generalisability.

#### Phase 4 Completion Criteria

Phase 4 will be considered complete when:

1. The source-data discrepancies have been investigated and either explained or transparently documented as unresolved.
2. The manuscript's Methods and Results match the locked implementation and saved artefacts.
3. All numerical values, tables, figures and citations have been verified.
4. Reproducibility documentation is complete.
5. Ethics and author declarations have been confirmed.
6. Reporting-framework requirements have been reviewed.
7. The manuscript has passed scientific and internal reproducibility review.

No change to the locked Phase 1 experiment will be made merely to make the manuscript appear more favourable or to resolve a documentation discrepancy.

### Phase 5 — Journal Selection, Submission and Publication Preparation

**Status:** Not started.

**Objective:** Identify an appropriate journal and prepare the complete scientific submission package after Phase 4 has been satisfactorily completed.

#### Journal Selection

- [ ] Identify journals relevant to machine learning, cardiovascular epidemiology, public health and health informatics.
- [ ] Assess journal scope and relevance to a cross-sectional BRFSS classification study.
- [ ] Review publication requirements and article formats.
- [ ] Check journal indexing and publication credibility.
- [ ] Compare open-access and subscription publication options.
- [ ] Assess article-processing charges and available waiver policies.
- [ ] Review journal policies on public datasets, code availability and reproducibility.
- [ ] Review journal requirements for TRIPOD+AI and other reporting checklists.
- [ ] Prepare a ranked shortlist of suitable journals.
- [ ] Select a target journal based on scientific fit and realistic submission requirements.

#### Submission Preparation

- [ ] Finalise the manuscript after Phase 4 review.
- [ ] Prepare the journal-specific manuscript format.
- [ ] Prepare the cover letter.
- [ ] Complete the official reporting checklist.
- [ ] Prepare supplementary methods and reproducibility materials where required.
- [ ] Finalise figures and tables in the journal's required formats.
- [ ] Prepare data and code availability statements.
- [ ] Finalise ethics, funding, competing-interest and author-contribution declarations.
- [ ] Confirm all authors and author order.
- [ ] Complete the final submission-readiness check.
- [ ] Submit the manuscript only after author approval.

#### Post-Submission and Peer-Review Response

- [ ] Record the journal submission date and manuscript reference.
- [ ] Monitor editorial and reviewer decisions.
- [ ] Prepare a structured response-to-reviewers document.
- [ ] Distinguish requests for clarification from requests requiring new analyses.
- [ ] Evaluate any proposed methodological changes against the locked research specification.
- [ ] Document and justify any new analysis or research extension.
- [ ] Revise manuscript sections, tables, figures and supplementary materials.
- [ ] Maintain version control for each manuscript revision.
- [ ] Record resubmission and editorial decisions.
- [ ] Update the research log and changelog when significant publication milestones occur.

Journal acceptance or publication is not assumed.

---

## 6. GitHub Research Development Strategy

The repository uses a phase-oriented development workflow to preserve the research history and distinguish completed experimental work from subsequent documentation, auditing and manuscript development.

### Branch and Tag Structure

| Branch / Tag | Purpose |
|---|---|
| `main` | Stable, reviewed research |
| `v0.1.0` | Completed Phase 1 computational baseline |
| `phase/02-literature-review` | Literature verification and research positioning |
| `phase/03-data-provenance-audit` | Phase 3 WP1 data-provenance audit |
| `phase/03-manuscript-development` | Phase 3 WP2 scientific manuscript development |
| `phase/04-scientific-review` | Scientific and reproducibility assessment |
| `phase/05-publication` | Journal selection, submission and publication preparation |

The branch names above describe the project's branch strategy. Their current existence and remote publication status must be checked using Git before being treated as confirmed.

### Phase 3 Branch Strategy

The intended Phase 3 branch sequence is:

1. Continue the WP1 audit work on `phase/03-data-provenance-audit`.
2. Commit and verify the audit report and supporting artefacts.
3. Push the audit branch after local verification.
4. Create a milestone tag and GitHub release only after the audit deliverables have been verified.
5. Create `phase/03-manuscript-development` from the verified audit branch.
6. Keep all manuscript sections and related documentation on the same manuscript-development branch.
7. Do not create a separate branch for each manuscript section.
8. Integrate the reviewed Phase 3 work into the stable research history through the agreed Git workflow.

**Proposed WP1 audit tag:** `phase-03-data-provenance-audit-v1.0.0`

**Proposed WP1 release title:** `Phase 3 WP1 — BRFSS Data Provenance and Dataset Integrity Audit v1.0.0`

The proposed tag and release are milestone identifiers only. They must not be treated as published until their creation and GitHub release status are verified.

### Repository Development Principles

- Preserve `main` as the stable research branch.
- Preserve the `v0.1.0` computational baseline.
- Keep Phase 1 experimental artefacts unchanged.
- Keep Phase 2 literature records and research decisions intact.
- Separate audit and manuscript development work.
- Use one active branch for the current work package where appropriate.
- Document meaningful changes through Git commits.
- Use GitHub Issues for trackable research tasks.
- Use pull requests for reviewed changes.
- Update `CHANGELOG.md` and `research_log.md` for significant milestones.
- Update `README.md` and `project_status.md` together when a phase is completed.
- Use version tags for significant reviewed milestones rather than routine documentation edits.
- Do not commit raw BRFSS datasets or local environment files.

Actual branch, commit, working-tree, push, tag and release status must be verified locally before any repository milestone is described as published.

---

## 7. Scientific Interpretation Boundaries

This study classifies **prevalent self-reported myocardial infarction and/or coronary heart disease** among BRFSS survey respondents.

It does not:

- Predict future cardiovascular events.
- Establish causal relationships.
- Provide clinical diagnosis or treatment recommendations.
- Constitute a clinically validated cardiovascular risk assessment system.
- Establish clinical utility.
- Establish generalisability to populations outside the evaluated BRFSS survey years.
- Demonstrate prospective individual-level risk prediction.

The study uses cross-sectional survey data. Its temporal evaluation assesses the performance of a frozen model on a later annual survey dataset; it does not establish prospective individual-level prediction.

The `_MICHD` outcome is derived from respondents' self-reported cardiovascular history using the CDC-defined construction rule. Agreement with that rule does not independently establish the clinical truth of those reports.

Survey-weighted predictive-performance results are reported as point estimates, without full complex-survey inferential uncertainty estimation.

Subgroup differences, missingness patterns and feature-importance results must be interpreted within the limitations of the available data and model design.

The study's conclusions must remain proportional to the evidence. No unsupported claim of clinical readiness, causality, universal generalisability or first-study novelty should be introduced during manuscript revision.

---

## 8. Related Project Documentation

- [README.md](../README.md) — Project overview and principal findings.
- [CHANGELOG.md](../CHANGELOG.md) — Completed repository milestones and release history.
- [research_log.md](../research_log.md) — Chronological research activities and methodological decisions.
- [research_protocol.md](research_protocol.md) — Research design and methodology.
- [dataset_selection.md](dataset_selection.md) — Dataset-selection decisions.
- [data_dictionary.md](data_dictionary.md) — Source variables, analytical definitions and transformations.
- [research_questions.md](research_questions.md) — Current documented research questions, subject to justified refinement.
- [CITATION.cff](../CITATION.cff) — Repository citation metadata.
- `literature/literature_matrix.csv` — Core literature evidence records.
- `literature/screening_log.csv` — Literature screening record.
- `literature/search_strategy.md` — Search approach, accessed sources and review limitations.
- `literature/related_work_synthesis.md` — Literature synthesis.
- `literature/references.bib` — Bibliographic references.
- `docs/PHASE2_RESEARCH_POSITIONING.md` — Phase 2 research-positioning document.
- `docs/PHASE2_FINAL_REPORT.md` — Phase 2 final report.
- `scripts/audit_brfss_provenance.py` — Phase 3 WP1 audit script.
- `artifacts/provenance/phase3_dataset_audit.json` — Machine-readable dataset audit.
- `artifacts/provenance/phase3_dataset_audit.csv` — Dataset audit summary.
- `artifacts/provenance/phase3_target_consistency.json` — `_MICHD` target consistency results.
- `artifacts/provenance/phase3_core_variable_profile.csv` — Core-variable profile.
- `docs/audits/phase3_wp1_brfss_data_provenance_audit.md` — Intended Phase 3 WP1 audit report path.
- `docs/manuscript/manuscript_full.md` — Intended Phase 3 WP2 full manuscript path.
- `docs/manuscript/08_submission_readiness_checklist.md` — Intended manuscript submission-readiness checklist path.

---

**Last updated:** 1 November 2026

**Current status:** Phase 1 completed and released as `v0.1.0`; Phase 2 completed for the stated targeted critical narrative/scoping review scope; Phase 3 WP1 data-provenance and dataset-integrity audit completed, and WP2 first full scientific manuscript draft prepared. Phase 4 scientific and reproducibility review is the next milestone.

**Important repository note:** This document is the complete consolidated Project Status content. The manuscript and checklist paths above are intended repository locations; their file creation, integration, Git commits and pushes must be verified separately. The Phase 3 audit report and release status must also be verified before being described as published.