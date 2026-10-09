# Contributing

This repository documents a research analysis, not a production clinical application. Feedback on reproducibility, documentation, research integrity and methodological limitations is welcome.

## Development workflow

1. Use `main` for reviewed, stable work. Open a GitHub Issue for proposed corrections or substantive research tasks.
2. Work in an appropriately named branch: `phase/02-literature-review`, `phase/03-manuscript-writing`, `fix/reproducibility-path`, or `docs/methods-clarification`.
3. Open a pull request to `main`. Describe **what changed, why, what was verified, and what remains uncertain**; complete the pull-request checklist.
4. Run `python scripts/check_repository.py` where available, and review the GitHub Actions status. The repository check does **not** retrain models or independently reproduce empirical results.
5. Merge only after human review of scientific claims, filenames, links and any affected artifacts. Update `CHANGELOG.md` for meaningful milestones and `docs/PROJECT_STATUS.md` when the active research phase changes.

## Scientific integrity

- Preserve the official research title: **Cardiovascular Machine Learning Research: BRFSS-Based Classification of Prevalent Self-Reported Myocardial Infarction and Coronary Heart Disease with Temporal Validation**.
- The completed primary analysis develops models with **BRFSS 2023** and evaluates the frozen model on **BRFSS 2025**. The outcome `_MICHD` concerns **prevalent self-reported** MI/CHD; do not call this prospective risk prediction or clinical diagnosis.
- Do not silently edit the locked six predictors, target, threshold, fitted preprocessing, models, empirical outputs, source fingerprints or sample definitions. Report a discovered error in an Issue, assess its impact, and explicitly label corrected or additional analyses.
- Distinguish original results from later sensitivity analyses or extensions. Do not generate synthetic activity, backdate commits or claim publication/peer review that has not occurred.
- Verify bibliographic metadata and citations against actual publications before merging literature or manuscript content. Mark incomplete references as provisional.
- Do not commit `.venv/`, credentials, raw BRFSS XPT files, personal health information or non-public data. Cite official CDC documentation when describing the survey.

## Licensing and attribution

See `LICENSE` for the MIT licence applicable to original repository materials, `CITATION.cff` for citation metadata, and `data/README.md` for separate CDC dataset provenance. The MIT licence does not relicense CDC source files.
