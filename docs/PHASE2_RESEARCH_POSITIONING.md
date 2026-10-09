# Phase 2 — Research positioning and evidence gaps (working document)

**Official title:** Cardiovascular Machine Learning Research: BRFSS-Based Classification of Prevalent Self-Reported Myocardial Infarction and Coronary Heart Disease with Temporal Validation

**Baseline:** Git tag `v0.1.0`, completed Phase 1, BRFSS 2023 development and BRFSS 2025 frozen evaluation. No new models are required to start this phase.

**Status:** Candidate arguments, **not final novelty claims**. The Phase 1 experiment and manuscript research questions must not be retroactively misrepresented.

## Closest published comparator

Noh et al. (2026), *BMC Public Health*, DOI 10.1186/s12889-026-27570-3, classified prevalent self-reported MI/CHD using BRFSS 2023 with 433,323 source respondents. They evaluated model choices and the effect of post-diagnosis proxy variables. This means **BRFSS + MI/CHD classification + prevention of label leakage is not unique to this project**.

Differences requiring further full-text evaluation:

| Dimension | Our released study | Noh et al. (2026) |
|---|---|---|
| Source year | 2023 + 2025 frozen later-year evaluation | 2023 in examined Methods |
| Target | Prevalent self-reported MI/CHD | Prevalent self-reported MI/CHD |
| Predictors | Six fixed predictors | Larger candidate panel; post-diagnosis-proxy exclusions investigated |
| Development evaluation | 70/15/15 with locked 2023 test | 70/30 with training cross-validation and held-out evaluation |
| Cross-year test | Frozen pipeline on BRFSS 2025 | Not described in examined article |
| Calibration | Brier and calibration intercept/slope in both years | Calibration presented in 2023 article |
| Survey weights | Model evaluation point estimates | Weighted association sensitivity analysis in article |

Do **not** read differing ROC-AUC values as a head-to-head test; the models, predictors and evaluation protocols differ.

## Candidate scientific contribution (conditional)

A compact six-predictor classification framework, with honest restricted-feature performance, an untouched held-out test, subsequent frozen application to an independent BRFSS survey year, explicit calibration, survey-weighted evaluation point estimates, and documented subgroup/missingness robustness.

This is currently a **candidate contribution**, not a verified claim that no previous study has combined these elements. Complete the literature review before writing a novelty statement.

## Working manuscript questions — for discussion, not a new experimental protocol

1. What discrimination and calibration does a fixed six-predictor model show on the held-out BRFSS 2023 sample?
2. How well do these results transfer unchanged to the independent BRFSS 2025 survey-year sample?
3. What is the difference between Gradient Boosting and the simpler Logistic Regression benchmark?
4. How do survey evaluation weights, missing predictors, age subgroups and threshold choice affect interpretation?
5. Are model reliance patterns stable between the two surveyed years?

Do **not** claim sex-subgroup findings unless evidence is actually present in the locked analysis. The existing `docs/research_questions.md` should only be edited after reviewing all drafted questions against completed analyses and verified literature.

## Research limitations to carry into manuscript

Cross-sectional, self-reported prevalent disease; possible reverse causality; restricted covariates; selected threshold not clinically validated; survey weighted point estimates without full complex-design uncertainty; source-variable harmonisation/missingness changes; no external clinical population or prospective evaluation.

## Source-provenance issue requiring explicit documentation

As checked 2026-10-09, the current CDC 2023 annual-download page states **345 variables in the downloadable XPT**, while Phase 1 previously documented a local 2023 file with **350 observed source columns**. The local 2025 XPT yielded **283** variables while a CDC page showed **284**. The current CDC 2023 page also describes revisions to the source file. These are **unresolved version/documentation differences**: inspect recorded SHA-256 fingerprints, file dates and exact source snapshots; do not guess a reason or change Phase 1 outputs to fit current CDC metadata. The 2025 discrepancy must likewise be checked against the particular official version used.

CDC 2023 documentation: https://www.cdc.gov/brfss/annual_data/annual_2023.html  
CDC 2025 documentation: https://www.cdc.gov/brfss/annual_data/annual_2025.html

## Next decisions

- Review the existing `literature/literature_matrix.csv` and `literature/search_strategy.md` **before replacing either**. They were not uploaded for this review.
- Read Noh et al. (2026) and the BRFSS→NHANES study carefully; record comparability.
- Finalise actual database search logs and screening results.
- Revise questions/claim of contribution only when grounded; preserve Phase 1 tag.
