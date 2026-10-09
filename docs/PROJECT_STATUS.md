# Project Status

**Research title:** Cardiovascular Machine Learning Research: BRFSS-Based Classification of Prevalent Self-Reported Myocardial Infarction and Coronary Heart Disease with Temporal Validation

**Current milestone:** Phase 1 — Computational analysis completed; first public repository snapshot and release preparation.

**Planned first tag:** `v0.1.0` (Phase 1 computational snapshot). This page **does not assert that a tag or GitHub Release already exists**.

## Completed: Phase 1 — Research implementation

- BRFSS 2023 source-data inspection, variable coding, missing-data handling and leakage-controlled analytical preparation.
- Six-predictor classification of prevalent self-reported MI/CHD (`_MICHD`).
- Development-set candidate model comparison and frozen Gradient Boosting model and validation-selected decision threshold.
- Independent 2023 held-out test and unchanged-model evaluation on BRFSS 2025.
- Calibration, survey-weighted evaluation point estimates, permutation importance, missingness/threshold checks and subgroup analyses.
- Optimised research notebook, HTML export, saved model artifacts, machine-readable tables/figures and recorded provenance.

**Headline results, unweighted ROC-AUC:** 2023 held-out **0.8012**; 2025 temporal **0.7949**. Neither value constitutes clinical validation.

## Final preparation before the Phase 1 tag

- [ ] Confirm GitHub Actions repository checks pass on the new remote.
- [ ] Verify tracked files exclude raw XPT datasets, environments and the locally ignored PDF.
- [ ] Ensure paths and links reference `03_brfss_2023_first_look_optimised` and the public HTML report.
- [ ] Resolve old-history `git_provenance.json` references and review data/model fingerprint records.
- [ ] Create first clean Git commit, verify repository visibility, then add `v0.1.0` and a GitHub Release.

A structural repository audit does **not** demonstrate successful clean-kernel execution or independent recreation of trained results. Record those separately if performed.

## Next: Phase 2 — Literature review and manuscript evidence

Planned working branch: `phase/02-literature-review`.

The next phase will verify literature, document the actual search process, evaluate the research gap and refine manuscript framing where justified. Verified changes will be merged to `main` through reviewed commits. The completed Phase 1 experimental specification will not be silently rewritten.

## Later phases

| Phase | Planned scope | Status |
|---|---|---|
| 3 | Manuscript writing (Methods, Results, Discussion, Introduction, Abstract) | Not started |
| 4 | Scientific and reproducibility review | Not started |
| 5 | Journal submission and release/publication preparation | Not started |

## Interpretation boundaries

This work classifies **prevalent self-reported** MI/CHD among BRFSS respondents. It does not forecast incident cardiovascular events, establish causal effects, or supply an approved clinical diagnostic or treatment system. Survey-weighted predictive-performance results are point estimates, not full complex-survey inferential uncertainty estimates.

For the chronological record, see `research_log.md`; for decisions and methods, see `docs/research_protocol.md`; for future software releases, see `CHANGELOG.md`.
