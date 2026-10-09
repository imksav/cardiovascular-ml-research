
# Changelog

This file documents **completed, meaningful changes** to the research repository. Version tags capture reproducible snapshots of the computational work, not publication or clinical approval.

## [Unreleased]

### Planned
- Verify literature references and document the search strategy in Phase 2.
- Refine manuscript research questions and identify relevant research gaps.
- Prepare and review the scientific manuscript in later phases.

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
