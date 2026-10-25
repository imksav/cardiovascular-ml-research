# Research Log

## Current Status — 25 October 2026

Phase 1 is complete and preserved under `v0.1.0`. Phase 2 is complete as a targeted critical narrative/scoping review; the final report and evidence artifacts are in `docs/PHASE2_FINAL_REPORT.md` and `literature/`. Phase 3 manuscript development is the next phase. The review is not systematic, and no exhaustive-search or “first study” claim is made.

## Project

Cardiovascular Machine Learning Research: BRFSS-Based Classification of Prevalent Self-Reported Myocardial Infarction and Coronary Heart Disease with Temporal Validation

## Current Study Status — 9 October 2026

**Research title:** Cardiovascular Machine Learning Research: BRFSS-Based Classification of Prevalent Self-Reported Myocardial Infarction and Coronary Heart Disease with Temporal Validation

**Analytical status:** The BRFSS 2023 development, 2023 held-out evaluation and 2025 frozen-pipeline temporal comparison have been completed in the experimental notebook. Manuscript drafting, source verification, documentation cleanup and reproducibility review are still in progress. No journal acceptance, DOI or official `v1.0.0` software release is claimed.

### Completed Research Decisions

- Outcome: prevalent **self-reported MI and/or CHD**, from BRFSS `_MICHD`; **not** prospective risk prediction.
- Data: 2023 development and internal evaluation; 2024 compatibility audit; 2025 cross-year evaluation.
- Six predictors: age group, physical activity, smoking status (`_SMOKER3`), blood-pressure status, diabetes status and BMI.
- Development: 70/15/15 train/validation/test split, seed 42, training-only preprocessing and 3-fold stratified hyperparameter search.
- Primary model: Gradient Boosting (150 estimators, learning rate 0.10, depth 3); Logistic Regression benchmark.
- Threshold: approximately 0.152913, selected by validation F1 and held fixed for final evaluations.
- ROC-AUC: 0.80115 on 2023 held-out test (n=64,311), 0.79486 on 2025 (n=352,145). The full metrics are in the notebook/README.
- Additional completed work: calibration, survey-weighted evaluation **point estimates**, permutation importance and subgroup/missingness/threshold robustness.

### Pending Before Public Release

- [ ] Check the optimised Markdown notebook against the locked code/output notebook and confirm the final public filename.
- [ ] Reconcile root-level artifact output paths and the notebook's relative raw-data paths.
- [ ] Reconcile package pins with `artifacts/provenance/software_versions.json`; attempt fresh-environment smoke tests.
- [ ] Check README relative links and final notebook/PDF/report freshness.
- [ ] Validate literature citations and create the manuscript. Do **not** describe it as published/submitted before that happens.
- [ ] Decide separately when to create a GitHub Release, `v1.0.0` and an archive DOI.

> **Archival note:** The dated entries below retain the *historical planning status at that time*. Statements such as “not yet finalised” belong to those earlier stages and do not describe the project's status on 9 October 2026.



## Phase 2 Literature Review — First Evidence Pass (25 October 2026)

**Status:** First-pass exploratory retrieval and evidence matrix completed; review remains non-systematic and incomplete.

### Actions completed

- Reviewed the existing branch snapshot and retained the existing file structure and Phase 1 model/results.
- Populated `literature/literature_matrix.csv` with 15 evidence records spanning direct and related BRFSS studies, temporal/external validation, calibration/performance methodology, survey-aware ML, reporting/appraisal guidance, and official CDC documentation.
- Added `literature/screening_log.csv`; retained `literature/screening_log_template.csv` as a blank reusable template.
- Updated `literature/search_strategy.md` with actual exploratory queries, search date, source-access limits and explicit warnings that result counts and PRISMA flow are not available.
- Updated `docs/PHASE2_RESEARCH_POSITIONING.md` to reflect the closest comparator and narrower provisional contribution.

### Main evidence findings

1. **Noh et al. (2026), DOI 10.1186/s12889-026-27570-3, is a direct comparator.** It uses BRFSS 2023 and the prevalent self-reported MI/CHD target, evaluates post-diagnosis proxy exclusions, reports held-out performance and calibration, and includes weighted logistic-regression sensitivity analyses. Therefore, BRFSS 2023 `_MICHD` classification and leakage awareness are not unique claims.
2. **Kung et al. (2026), DOI 10.7150/ijms.137605, is a temporal-validation analogue.** It applies a BRFSS 2023 cross-sectional diabetes classifier to BRFSS 2024 without refitting. Temporal validation across annual BRFSS samples is not novel in itself, though the outcome differs.
3. **Wu et al. (2026), DOI 10.1016/j.cmpb.2025.109186, reports BRFSS internal and NHANES external validation** for a CHD model; exact target coding and survey methods require full-text extraction.
4. **Wanyonyi et al. (2025), DOI 10.1371/journal.pone.0328338, use a BRFSS 2015-derived secondary dataset** and report SMOTE, a 70/15/15 split and a stacking AUC of 0.94. The narrative ordering may place SMOTE before partitioning; code/supplement must be checked before concluding whether leakage occurred.
5. **Chavda and Hyun (2024), DOI 10.59720/24-006, report BRFSS 2022 self-reported CHD/MI history classification** with five-fold cross-validation (MCC 0.299–0.313 for primary models). This further rules out generic claims that BRFSS-based prevalent CHD/MI classification is new.
6. **Imani et al. (2026), DOI 10.1016/j.ahjo.2026.100719, use BRFSS 2022 and a combined self-reported CHD/MI outcome** with 13 predictors. The abstract/table accuracy values and a reported sample-count total conflict; the figures must be reconciled before any numeric comparison.
7. Survey-aware ML guidance by Oh et al. (2026) reinforces the distinction between weighted metric point estimates and full design-aware population inference. The existing study must continue to describe its weighted metrics as sensitivity-analysis point estimates only.
8. Official CDC pages currently report 345 variables for the 2023 XPT and 284 for the 2025 XPT, while local provenance records 350 and 283 observed columns, respectively. Local file hashes are recorded in `artifacts/provenance/dataset_provenance.json`; the source-version discrepancies remain unresolved and no Phase 1 rerun was performed.

### Current interpretation

The defensible provisional contribution is a description of the exact locked six-predictor prevalent MI/CHD classifier, its untouched 2023 test evaluation, unchanged application to the independent 2025 BRFSS sample, and joint reporting of calibration, weighted point-estimate sensitivity, subgroup/missingness and threshold robustness. This is **not yet a novelty claim**; the database-specific search and full-text screening remain incomplete.

### Next tasks

- [ ] Extract full methods/results for uncertain BRFSS/CHD studies and confirm outcome coding, sample restrictions, thresholds, calibration and survey handling.
- [ ] Run direct PubMed/MEDLINE and available Scopus/Web of Science/IEEE Xplore searches; save full queries, filters, exports and exclusion reasons.
- [ ] Deduplicate records and finish title/abstract and full-text screening.
- [ ] Apply relevant TRIPOD+AI reporting items and a proportionate PROBAST+AI appraisal before drafting the manuscript.
- [ ] Preserve Phase 1 model outputs and treat any new design-based inferential analysis as separate work.


---

## Historical Research Restart (5 October 2026)

**Date:** 5 October 2026

**Status:** Fresh research design and problem exploration

---

## 1. Reason for Restart

This project is being restarted as a new research study.

The previous MSc dissertation and earlier experimental research
direction will not determine the dataset, target variable,
machine-learning algorithms, preprocessing approach, model selection,
results, or conclusions of this study.

Previous work may later be consulted only where useful for:

- general academic structure;
- background writing;
- understanding concepts already studied;
- reflecting on methodological development.

Previous experimental results will not be treated as evidence for the
new research.

---

## 2. Broad Research Area

The new research will explore the intersection of:

- Data Analytics
- Statistics
- Data Science
- Machine Learning
- Health Data Science
- Cardiovascular Health
- Explainable Machine Learning
- Model Reliability and Generalisation

The exact research topic will be finalised only after evaluating
current literature and suitable datasets.

---

## 3. Main Learning Objective

This project will also support my progression from Data Analyst skills
toward Data Science and research.

The learning progression will be:

Research Problem

→ Data Understanding

→ Data Quality

→ SQL / Data Analysis

→ Exploratory Data Analysis

→ Statistics

→ Feature Engineering

→ Baseline Modelling

→ Machine Learning

→ Model Validation

→ Explainability

→ Critical Interpretation

→ Scientific Writing

→ Publication

The goal is not only to execute code, but to understand why each
methodological decision is made.

---

## 4. Current Research Stage

The current stage is:

**Research problem exploration and dataset discovery**

No final dataset has been selected.

No target variable has been selected.

No machine-learning algorithm has been selected.

No performance metric has been selected as the primary metric.

No hypothesis has been finalised.

These decisions will be made after understanding the research problem,
available data, and relevant literature.

---

## 5. Current Working Theme

A provisional area of interest is:

> Using population or clinical health data to investigate
> cardiovascular outcomes through data analytics, statistical
> analysis, and interpretable predictive modelling.

This is a working theme rather than a final research title.

---

## 6. Research Principles

The following principles will guide the study:

1. Dataset selection must be justified scientifically.

2. Raw data must be preserved unchanged.

3. Data understanding and exploratory analysis must occur before
   predictive modelling.

4. Each major analysis should answer a meaningful research question.

5. Statistical association must not automatically be interpreted as
   causation.

6. Predictive feature importance must not be interpreted as causal
   evidence.

7. Preprocessing must avoid data leakage.

8. Evaluation data must remain independent of model training and
   hyperparameter selection.

9. Simple baseline models should be established before more complex
   models.

10. Model performance must not be evaluated using accuracy alone.

11. Negative or unexpected findings must be reported honestly.

12. Methodology must not be changed merely to produce better results.

13. Important methodological decisions must be documented.

14. Code, package versions, data provenance, transformations, and
    random seeds should be recorded for reproducibility.

15. Predictive models will not be described as clinically validated
    diagnostic systems unless appropriate clinical validation exists.

---

## 7. Research Questions

Not yet finalised.

Research questions will be developed after:

1. reviewing recent cardiovascular-health data science research;
2. identifying important gaps;
3. comparing suitable datasets;
4. understanding what outcomes those datasets can genuinely support.

---

## 8. Dataset

**Status:** Not selected.

Candidate datasets will be compared based on:

- original source;
- population;
- sample size;
- outcome availability;
- predictor availability;
- missing data;
- data quality;
- temporal structure;
- clinical relevance;
- suitability for statistical analysis;
- suitability for machine learning;
- possibility of external validation;
- licence and reproducibility.

---

## 9. Models

**Status:** Not selected.

Algorithms will be selected only after the research problem and
dataset are understood.

The study will not begin by assuming that Random Forest, XGBoost,
neural networks, or any other particular model must be used.

---

## 10. Research Reflection

The most important change in this restart is that the research will
begin with a question rather than with an algorithm.

The intended sequence is:

Research question

→ appropriate data

→ analysis

→ evidence

→ modelling where justified

→ interpretation

rather than:

Dataset

→ algorithm

→ accuracy

---

## 11. Current Tasks

- [x] Existing development environment created
- [x] Git repository available
- [x] Python virtual environment available
- [x] Previous research direction archived
- [ ] Establish fresh research protocol
- [ ] Review candidate research problems
- [ ] Conduct initial literature search
- [ ] Identify candidate datasets
- [ ] Compare candidate datasets
- [ ] Select research outcome
- [ ] Finalise research question
- [ ] Finalise dataset
- [ ] Begin data understanding

---

## 12. Next Step

Begin Phase 1:

**Research Problem Discovery**

The next task is to investigate which cardiovascular research outcome
would provide a meaningful, feasible, and publishable data-science
study using publicly available data.


### Initial BRFSS Data Understanding

The 2023 BRFSS working dataset contains 433,323 respondent
records.

A small set of research-relevant variables was selected for
initial data understanding rather than loading all available
variables into the analytical DataFrame.

Initial inspection identified several important data-quality
considerations.

`GENHLTH` contains ordered health-status responses together with
special codes representing unknown and refused responses.

`DIABETE4` is not a simple binary variable. It distinguishes
diagnosed diabetes, gestational diabetes, no diabetes,
prediabetes/borderline diabetes, and special responses.

The candidate cardiovascular outcome `_MICHD` is substantially
imbalanced, with considerably fewer respondents reporting MI/CHD
than respondents who did not report MI/CHD. This demonstrates why
accuracy alone would be insufficient for evaluating a predictive
model.

Missingness also differs substantially between variables.
`TOLDHI3`, `_BMI5`, and `SMOKE100` contain notable missing values.

Missing data will not be removed or imputed until the questionnaire
logic, special response codes, and reasons for missingness have been
investigated.

### Key Learning

A numeric value in a dataset does not necessarily represent a
numerical measurement.

Survey variables may use numeric codes for categories, special
responses such as "Don't know" or "Refused", and questionnaire
skip logic.

Therefore, understanding the codebook is necessary before data
cleaning or modelling.


## Phase 2 Close-out — 25 October 2026

**Status:** Completed for the defined scope as a targeted critical narrative/scoping review. This is not a systematic review; no exhaustive database exports, complete search-result counts, dual independent screening or PRISMA flow are claimed.

### Final deliverables

- `literature/literature_matrix.csv`: 16 core evidence records.
- `literature/screening_log.csv`: source-level decisions and access limitations.
- `literature/verified_seed_sources.csv`: deduplicated source list.
- `literature/related_work_synthesis.md`: critical synthesis and cautious contribution statement.
- `literature/references.bib`: BibTeX references for manuscript writing.
- `literature/probast_ai_appraisal.csv`: provisional, single-reviewer domain-level appraisal; not a formal independent rating.
- `literature/tripod_ai_reporting_audit.csv`: 52-subitem pre-manuscript reporting audit.
- `docs/PHASE2_FINAL_REPORT.md`: close-out report, limitations and Phase 3 handoff.

### Final research decision

The closest direct comparator is Noh et al. (2026), which uses BRFSS 2023 and prevalent self-reported MI/CHD. Chavda and Hyun (2024) and Imani et al. (2026) provide additional BRFSS-based CHD/MI classification studies. Kung et al. (2026) demonstrates annual-BRFSS temporal validation for a different outcome. The project will not claim to be the first to use BRFSS, ML classification, leakage controls, calibration or annual-sample temporal validation.

The defensible contribution statement is a description of the locked six-predictor model, 2023 held-out evaluation, unchanged 2025 annual-sample application, and joint reporting of discrimination, calibration, fixed-threshold metrics, survey-weighted point-estimate sensitivity, and selected robustness analyses.

### Limitations retained for Phase 3

- The current CDC annual pages describe file dimensions that differ from the local file fingerprints/observed columns recorded in Phase 1 provenance; no source data or results were silently changed.
- Survey-weighted performance values remain point estimates without full complex-design uncertainty intervals.
- BRFSS 2025 is a separate annual sample, not longitudinal follow-up or independent clinical validation.
- Imani et al. contains unresolved sample-count and accuracy inconsistencies. Wanyonyi et al. has a possible SMOTE/split-order concern based on methods text; neither issue is described as confirmed without code/author verification.
- TRIPOD+AI items concerning ethics/IRB, funding, conflicts, registration and patient/public involvement require author confirmation during manuscript drafting.

### Next phase

Proceed to Phase 3 manuscript development. Draft Methods and Results from the locked protocol/notebook/tables first; then Introduction and Discussion from the related-work synthesis. Do not change the locked Phase 1 analysis silently. Commit and push the final Phase 2 checkpoint before creating the Phase 3 branch if preserving the branch history is desired.
