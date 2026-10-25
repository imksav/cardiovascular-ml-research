# Phase 2 — Research positioning and evidence gaps (working document)

**Official title:** Cardiovascular Machine Learning Research: BRFSS-Based Classification of Prevalent Self-Reported Myocardial Infarction and Coronary Heart Disease with Temporal Validation

**Baseline:** Existing `v0.1.0` Phase 1 release; BRFSS 2023 development and BRFSS 2025 frozen evaluation. No new models are required to start this phase.

**Status as of 2026-10-25:** Phase 2 completed as a targeted critical narrative/scoping review. This is not an exhaustive systematic review. The contribution statement is intentionally descriptive and does not claim priority or novelty.

## 1. Closest direct comparator: Noh et al. (2026)

Noh et al., *BMC Public Health* 26:2015, DOI [10.1186/s12889-026-27570-3](https://doi.org/10.1186/s12889-026-27570-3), used BRFSS 2023 (433,323 source respondents) to classify **prevalent self-reported MI or CHD**, explicitly not prospective risk. The study compared logistic regression, decision tree, random forest and gradient boosting; it tested inclusive and post-diagnosis-proxy-excluded feature specifications; reserved a held-out test set; used five-fold stratified cross-validation; and reported calibration curves, Brier score, calibration intercept/slope. It also fitted weighted logistic-regression sensitivity analyses on a complete-case subset (n=40,073).

The paper reports gradient-boosting ROC-AUC 0.867 / PR-AUC 0.389 in the inclusive specification and ROC-AUC 0.858 / PR-AUC 0.372 after post-diagnosis proxies were excluded. Its later analysis selected decision-tree models under sensitivity/specificity criteria. Those results are **not head-to-head** with the present six-predictor pipeline because predictor sets, model-selection rules, missingness and evaluation protocols differ.

**Positioning consequence:** BRFSS + `_MICHD` + ML classification + attention to leakage is not unique to this project. Do not claim otherwise.

## 2. Temporal validation is not new in itself

Kung et al. (2026), [DOI 10.7150/ijms.137605](https://doi.org/10.7150/ijms.137605), report development of a cross-sectional diabetes classifier using BRFSS 2023 and application to BRFSS 2024 without refitting, retuning or threshold adjustment. This is a methodological analogue rather than a same-outcome comparator.

Wu et al. (2026), [DOI 10.1016/j.cmpb.2025.109186](https://doi.org/10.1016/j.cmpb.2025.109186), report BRFSS internal validation and external validation using NHANES for a CHD model. This is cross-survey external validation, not the same design as frozen application to a later annual BRFSS sample; exact outcome-code comparability still needs full-text checking.
Wanyonyi et al. (2025), [DOI 10.1371/journal.pone.0328338](https://doi.org/10.1371/journal.pone.0328338), report CHD classification on a BRFSS 2015-derived secondary dataset with SMOTE and a 70/15/15 split. Their methods narrative appears to describe SMOTE before the final split, so the exact implementation should be checked against code/supplement before interpreting its high reported AUC as generalisable performance. This is a methodological question, not a confirmed error.
Chavda and Hyun (2024), [DOI 10.59720/24-006](https://doi.org/10.59720/24-006), report BRFSS 2022 classification of self-reported CHD/MI history with five-fold cross-validation (MCC 0.299–0.313 for the primary models). Imani et al. (2026), [DOI 10.1016/j.ahjo.2026.100719](https://doi.org/10.1016/j.ahjo.2026.100719), also use BRFSS 2022 with a combined self-reported CHD/MI outcome and 13 predictors. However, the accessible Imani article contains conflicting sample-count and accuracy figures between passages/tables; do not quote its performance until reconciled. Both papers further establish that broad BRFSS-based CHD/MI classification is already represented in the literature.

**Positioning consequence:** Do not claim the first use of temporal validation for annual BRFSS ML or the first validation of BRFSS-based CHD models. The narrower possible contribution is the particular outcome-specific six-feature specification, frozen 2023-to-2025 evaluation, and joint reporting of calibration, weighted point-estimate sensitivity, subgroup/missingness and threshold robustness—if a more complete search finds no closer equivalent.

## 3. Provisional evidence synthesis

| Evidence strand | Current finding | Implication |
|---|---|---|
| Direct BRFSS 2023 MI/CHD classification | A close direct comparator exists (Noh et al., 2026), with additional BRFSS 2022 CHD/MI classification studies by Chavda and Hyun (2024) and Imani et al. (2026). | Acknowledge explicitly and compare design choices, not raw AUCs. |
| Compact predictor set | The current project locks six predictors; the closest comparator uses a broader candidate panel and tests post-diagnosis proxies. | Restricted-feature design may be an applied distinction, but accessibility alone does not establish novelty or usefulness. |
| Annual survey temporal validation | Demonstrated for a different outcome in Kung et al. (2026). | Outcome-specific application and locked evaluation may be differentiators; temporal validation itself is not new. |
| Cross-survey external validation | BRFSS-to-NHANES CHD model reported by Wu et al. (2026); other cross-dataset CHD studies exist. | Clearly distinguish temporal validation within BRFSS from external validation across survey populations. |
| Calibration and evaluation | Noh et al. report Brier and calibration intercept/slope; foundational methods support separate reporting of discrimination and calibration. | Calibration reporting is good practice, not a stand-alone novelty claim. |
| Survey design | Noh et al. use weighted logistic-regression sensitivity analysis; 2026 survey-aware ML guidance stresses weights, PSU and strata across the ML lifecycle. | Present this study’s weighted metrics as point-estimate sensitivity analyses only; no design-corrected inference is claimed. |
| Reporting and bias | TRIPOD+AI and PROBAST+AI provide current reporting and appraisal frameworks. | Complete checklists before manuscript submission; do not claim formal compliance or risk-of-bias rating yet. |

## 4. Candidate contribution statement (not yet a novelty claim)

> This study evaluates a locked, six-predictor model for classifying prevalent self-reported MI/CHD using BRFSS 2023, then applies the frozen preprocessing, model and decision threshold unchanged to the independent BRFSS 2025 annual sample. It reports discrimination, probability calibration, fixed-threshold metrics, survey-weighted evaluation point estimates, and selected subgroup, missingness and threshold-robustness analyses.

This describes what was done. It does **not** state that the combination is the first of its kind, that the model predicts future cardiovascular risk, or that it is clinically validated. Any novelty wording must await broader database-specific searching and full-text screening.

## 5. Key limitations to preserve

- Cross-sectional, self-reported prevalent outcome; possible reverse causation and no prospective-risk interpretation.
- BRFSS 2025 is an independent annual survey sample, not follow-up of 2023 respondents; year-to-year performance differences can reflect sample composition and survey coverage.
- The six predictors are intentionally restricted and do not represent a clinical diagnostic panel.
- The fixed threshold was selected on 2023 validation data, not clinically selected.
- Survey-weighted metrics are point estimates; full complex-survey uncertainty intervals for model performance were not established.
- No external clinical cohort validation, prospective evaluation or evidence of clinical utility is available.
- Cross-study AUC/AP comparisons are not head-to-head due to different outcome definitions, populations, feature sets, missingness handling and thresholds.

## 6. Unresolved CDC source-version discrepancy

The current CDC 2023 annual page reports 433,323 records and 345 variables in the currently posted XPT; the 2025 page reports 356,158 records and 284 variables. Project provenance records the locally used 2023 file as 1,205,554,400 bytes with SHA-256 `3d3bf8ef5195bde227828ddc4c90745b76e8b304f8f5b9a043b6d99895fd1615` and 350 observed columns; the 2025 file as 799,971,280 bytes with SHA-256 `d99262f8854f018a600c3538ee78e4308569af700abe6b92b36180336c24dec2` and 283 observed columns.

CDC states that the 2023 file was updated, including a February 2025 revision. The precise reason for the local-versus-current column-count differences has not been established. Preserve the hashes and current locked outputs; compare local source fingerprints, download dates and official snapshots before deciding whether any separate sensitivity rerun is justified. Do not silently replace the files or rewrite Phase 1 results.

Official data pages: [CDC BRFSS 2023](https://www.cdc.gov/brfss/annual_data/annual_2023.html) · [CDC BRFSS 2025](https://www.cdc.gov/brfss/annual_data/annual_2025.html).

## 7. Phase 3 handoff

1. Draft Methods and Results from the locked protocol, notebook, provenance and exported tables.
2. Use `literature/related_work_synthesis.md` and `literature/references.bib` to write the Introduction and Discussion.
3. Use `literature/tripod_ai_reporting_audit.csv` to track author confirmations and reporting gaps.
4. Preserve the caveat that survey-weighted performance values are point estimates, not full complex-survey inference.
5. Do not alter the locked Phase 1 model or results silently. If a source-version issue requires reanalysis, document it as a separate, justified analysis.

## 8. Phase 2 close-out and Phase 3 entry

Phase 2 is complete for the scoped review objective. The final narrative synthesis is stored at `literature/related_work_synthesis.md`; the evidence matrix and screening log remain the structured extraction record; `literature/references.bib` is the citation-manager source; `literature/probast_ai_appraisal.csv` records provisional study-level appraisal; and `literature/tripod_ai_reporting_audit.csv` records manuscript reporting readiness.

The final contribution statement is:

> This study evaluates a locked six-predictor model for classifying prevalent self-reported MI/CHD using BRFSS 2023, then applies the frozen preprocessing pipeline, fitted model and decision threshold unchanged to the independent BRFSS 2025 annual sample. It reports discrimination, probability calibration, fixed-threshold classification metrics, survey-weighted evaluation point estimates, and selected subgroup, missingness and threshold-robustness analyses.

This is not a “first study” claim. The review is targeted and non-systematic because full database exports, exhaustive counts and independent dual screening were not performed. The project can proceed to Phase 3 without pretending those steps occurred. Any manuscript that makes an exhaustive or priority claim would require a separate protocolled review.

Before submission, carry forward the unresolved CDC source-version discrepancy, the point-estimate-only survey-weighted analysis, and the TRIPOD+AI author-confirmation items. These do not require changing the locked Phase 1 model in order to begin writing.
