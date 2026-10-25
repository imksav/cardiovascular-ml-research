# Phase 2 Final Report — Literature Review and Research Positioning

**Research project:** Cardiovascular Machine Learning Research: BRFSS-Based Classification of Prevalent Self-Reported Myocardial Infarction and Coronary Heart Disease with Temporal Validation
**Phase:** 02 — Literature review and research positioning
**Status:** Completed for the defined scope on 25 October 2026
**Review type:** Targeted critical narrative/scoping review; not a systematic review
**Phase 1 baseline:** Preserved; no model retraining or experimental result changes were made.

## Executive conclusion

Phase 2 has produced a repository-native evidence matrix, source-level screening log, deduplicated seed bibliography, detailed related-work synthesis, BibTeX references, a provisional PROBAST+AI appraisal (seven comparator studies plus the project; Kung et al. is explicitly unrated because full-text access was insufficient), and a 52-subitem TRIPOD+AI pre-manuscript audit. These deliverables are stored in the existing `literature/`, `docs/`, `research_log.md`, and `CHANGELOG.md` paths.

The main research decision is to **avoid a broad novelty claim**. Noh et al. (2026) is a close direct comparator because it uses BRFSS 2023 and prevalent self-reported MI/CHD. Chavda and Hyun (2024) and Imani et al. (2026) add other BRFSS-based studies of self-reported CHD/MI history. Kung et al. (2026) demonstrates frozen annual-BRFSS temporal validation for a different cross-sectional outcome. The current project's contribution should therefore be described as the specific locked six-predictor MI/CHD design, frozen 2023-to-2025 evaluation, and joint reporting of calibration and selected robustness analyses—not as the first use of BRFSS, ML classification, leakage controls, calibration or temporal validation.

## What was completed

1. **Evidence matrix:** 16 core evidence records in `literature/literature_matrix.csv`, covering direct/related empirical studies, temporal and cross-survey validation, reporting and appraisal guidance, performance/calibration methodology, and official CDC data documentation.
2. **Screening log:** `literature/screening_log.csv` records source-level decisions, access level and limitations. `screening_log_template.csv` remains unchanged as a blank template.
3. **Source-list cleanup:** `literature/verified_seed_sources.csv` is deduplicated; the duplicate Wu et al. record was removed.
4. **Critical synthesis:** `literature/related_work_synthesis.md` synthesizes the direct comparator, related classifiers, temporal validation, survey-aware analysis, calibration and reporting guidance, and supplies a cautious contribution statement.
5. **Citation manager file:** `literature/references.bib` supplies BibTeX entries for core empirical, methodological and CDC sources.
6. **Appraisal:** `literature/probast_ai_appraisal.csv` records provisional domain-level concerns for six accessible comparator studies, an explicitly unrated Kung et al. record, and the current project. It is a single-reviewer desk appraisal, not an independent formal rating.
7. **Reporting readiness:** `literature/tripod_ai_reporting_audit.csv` audits all 52 subitems mapped to the TRIPOD+AI checklist and identifies items for manuscript drafting and author confirmation.
8. **Research positioning and status:** `docs/PHASE2_RESEARCH_POSITIONING.md`, `docs/PROJECT_STATUS.md`, `README.md`, `research_log.md`, and `CHANGELOG.md` now reflect the Phase 2 conclusion and Phase 3 handoff.
9. **Validation:** CSVs were parsed; the existing notebook JSON and Phase 1 figures/model artifacts were preserved. No new figure was necessary for this literature-review phase; the evidence matrix and checklists are more appropriate primary outputs than a PRISMA diagram when exhaustive screening counts are unavailable.

## Final research position

> This study evaluates a locked six-predictor model for classifying prevalent self-reported MI/CHD using BRFSS 2023, then applies the frozen preprocessing pipeline, fitted model and decision threshold unchanged to the independent BRFSS 2025 annual sample. It reports discrimination, probability calibration, fixed-threshold classification metrics, survey-weighted evaluation point estimates, and selected subgroup, missingness and threshold-robustness analyses.

This statement describes the study rather than asserting novelty. Any stronger priority claim would require broader, protocolled searching and independent screening.

## Key risks and limitations carried forward

- **CDC file-version discrepancy:** the recorded local 2023 and 2025 source files have column counts that differ from current official downloadable-file descriptions. The original hashes are preserved. Do not silently replace source data or rerun the locked experiment. Investigate this separately before a rerun or manuscript claim that depends on exact source-file version.
- **Survey inference:** survey-weighted results are point-estimate sensitivity analyses, not full complex-design uncertainty estimates.
- **Temporal evaluation:** BRFSS 2025 is an independent annual sample, not follow-up of 2023 respondents and not external clinical validation.
- **Cross-sectional outcome:** `_MICHD` represents prevalent self-reported MI/CHD; no future-event or causal interpretation is supported.
- **Incomplete database coverage:** no direct Scopus/Web of Science/Embase/IEEE subscription exports, complete query-result counts, independent dual screening or PRISMA flow were produced. Phase 2 is complete as a targeted narrative/scoping review, not as a systematic review.
- **Comparator inconsistencies:** Imani et al.'s abstract/table counts and accuracy conflict; Wanyonyi et al.'s written SMOTE/split order raises a possible leakage concern but was not code-audited. Neither issue is treated as confirmed error.
- **Reporting:** the TRIPOD+AI audit identifies author confirmations still needed for ethics/IRB, funding, conflicts, registration, patient/public involvement and uncertainty reporting.

## Files to retain

- `literature/literature_matrix.csv`
- `literature/verified_seed_sources.csv`
- `literature/screening_log.csv`
- `literature/screening_log_template.csv`
- `literature/search_strategy.md`
- `literature/related_work_synthesis.md`
- `literature/references.bib`
- `literature/probast_ai_appraisal.csv`
- `literature/tripod_ai_reporting_audit.csv`
- `docs/PHASE2_RESEARCH_POSITIONING.md`
- `docs/PROJECT_STATUS.md`
- `docs/PHASE2_FINAL_REPORT.md`
- `reports/PHASE2_FINAL_REPORT.pdf` — concise four-page close-out summary
- `research_log.md` and `CHANGELOG.md`

## Phase 3 handoff

Phase 3 can start immediately with manuscript development. Draft Methods and Results from the locked protocol, notebook and result tables first; then draft the Introduction and Discussion using `literature/related_work_synthesis.md`. The next phase must not change the locked model or results silently. Before submission, resolve or transparently document the source-version discrepancy, complete the author-confirmation items in the TRIPOD+AI audit, and decide whether uncertainty intervals can be added without misrepresenting complex-survey inference.

## Git recommendation

A Git push is not required for this review work to be usable locally. However, before beginning Phase 3 on a separate branch, commit and push the completed Phase 2 files on `phase/02-literature-review` to preserve the checkpoint. Then create `phase/03-manuscript-writing` from that commit. The supplied ZIP itself has no `.git` directory, so the final downloadable snapshot is a source archive, not a Git bundle or proof of a pushed commit.
