# Changelog

This file documents **completed, meaningful changes** to the research repository. Version tags capture reproducible snapshots of the computational work, not publication or clinical approval.

## [Unreleased]

### Planned
- Verify literature references and document the search strategy in Phase 2.
- Prepare and review the scientific manuscript in later phases.

## [0.1.0] — Phase 1 computational snapshot (release pending)

### Added
- Reproducible BRFSS 2023 machine-learning development workflow and an unchanged-model evaluation on BRFSS 2025.
- One canonical executed notebook, `notebooks/03_brfss_2023_first_look_optimised.ipynb`, and an HTML export of its saved contents.
- Frozen Gradient Boosting and Logistic Regression model artifacts; machine-readable evaluation tables, figures, dataset and software provenance.
- Documentation covering dataset selection, outcome and predictor definitions, leakage prevention, training and validation, temporal evaluation, limitations and reproducibility.
- GitHub repository governance, issue/PR templates and data-free repository checks.

### Notes
- `0.1.0` is **not yet released** until the Git tag and GitHub Release exist. Do not add an invented release date.
- The study classifies **prevalent self-reported** myocardial infarction and/or coronary heart disease; it is not a future-risk model, clinical diagnostic tool or peer-reviewed publication.
- Changes made after the Phase 1 tag will be recorded in **Unreleased** until the next justified version.
