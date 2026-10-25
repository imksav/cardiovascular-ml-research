
# Changelog

This file documents **completed, meaningful changes** to the research repository. Version tags capture reproducible snapshots of the computational work, not publication or clinical approval.

## [Unreleased]

### Phase 2 close-out — 2026-10-25
- Completed the targeted critical narrative/scoping review and finalized the research-positioning decision; no “first study” claim is made.
- Added `literature/related_work_synthesis.md`, `literature/references.bib`, `literature/probast_ai_appraisal.csv`, and `literature/tripod_ai_reporting_audit.csv`.
- Deduplicated `literature/verified_seed_sources.csv`; expanded source-level notes for the BRFSS 2022 studies and the annual-BRFSS temporal-validation analogue.
- Added `docs/PHASE2_FINAL_REPORT.md` and updated project status/readme/research log for Phase 3 handoff.
- Preserved Phase 1 model artifacts, tables and figures unchanged.

### Added
- Populated `literature/literature_matrix.csv` with a 16-record first-pass evidence set covering direct/related BRFSS classifiers, annual-sample temporal validation, cross-survey validation, calibration, survey-aware ML, reporting guidance and official CDC documentation.
- Added `literature/screening_log.csv` for source-level screening decisions while preserving `literature/screening_log_template.csv` as a blank reusable template.
- Updated `literature/search_strategy.md` with the exploratory queries actually run, source-access limits and the explicit status that this is not an exhaustive systematic review.
- Updated `docs/PHASE2_RESEARCH_POSITIONING.md`, `docs/PROJECT_STATUS.md` and `research_log.md` with the direct comparator, temporal-validation analogue, provisional contribution and unresolved source-version discrepancy.

### Research positioning
- Confirmed Noh et al. (2026) as a close BRFSS 2023 prevalent self-reported MI/CHD comparator; broad novelty claims are not supported.
- Identified additional BRFSS 2022 CHD/MI classification studies and a BRFSS 2023-to-2024 diabetes temporal-validation analogue.
- Flagged unresolved sample/metric inconsistencies in one related study and a possible SMOTE/split-ordering concern in another for verification; neither is treated as a confirmed methodological error.

### Remaining
- If exhaustive coverage is required for a target journal, run a separately protocolled database review with full database exports, result counts and independent screening.
- Resolve the CDC source-file fingerprint/column-count discrepancy before any justified rerun.
- Draft the scientific manuscript in Phase 3 and complete author confirmations listed in the TRIPOD+AI audit.

## [0.1.0] — 2026-10-09

**Phase 1 — Completed Experimental Analysis**

**Release status:** Published as a GitHub pre-release.

### Added
- Reproducible BRFSS 2023 machine-learning development workflow and an unchanged-model evaluation on BRFSS 2025.
- One canonical executed notebook, `notebooks/03_brfss_2023_first_look_optimised.ipynb`, and an HTML export of its saved contents.
- Frozen Gradient Boosting and Logistic Regression model artifacts; machine-readable evaluation tables, figures, dataset and software provenance.
- Documentation covering dataset selection, outcome and predictor definitions, leakage prevention, training and validation, temporal evaluation, limitations and reproducibility.
- GitHub repository governance, issue/PR templates and data-free repository checks.

### Release
- Published the first computational research snapshot as `v0.1.0`.
- Completed Phase 1 experimental analysis and established a versioned baseline for subsequent research.
- Verified the repository using automated GitHub Actions checks.

### Notes
- This release represents the completed **computational research baseline**, not a peer-reviewed publication or clinical approval.
- The study classifies **prevalent self-reported** myocardial infarction and/or coronary heart disease; it is not a future-risk model or clinical diagnostic tool.
- The scientific analysis and reproducibility artifacts are preserved under tag `v0.1.0`.
- Changes made after the Phase 1 tag will be documented under **Unreleased** until the next justified version.

**GitHub Release:** https://github.com/imksav/cardiovascular-ml-research/releases/tag/v0.1.0
