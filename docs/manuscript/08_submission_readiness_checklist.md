# Phase 3 manuscript completion and Phase 4 handover checklist

## Phase 3 writing deliverables

- [x] Complete structured abstract.
- [x] Complete introduction with defensible research positioning.
- [x] Complete Methods draft using the locked model and audit record.
- [x] Complete Results with primary, calibration, weighted, missingness, feature-importance and subgroup findings.
- [x] Complete Discussion and conclusion.
- [x] Assemble core references.
- [x] Add author-declaration placeholders rather than inventing ethics, funding or conflict statements.
- [x] Prepare README and PROJECT_STATUS update blocks.
- [x] Preserve Phase 1 locked results and Phase 2 scope.

## Phase 4 scientific and reproducibility review — required before submission

### Critical data-provenance issue

- [ ] Reconcile the official CDC variable counts with the local XPT files: 2023 official 345 vs local 350; 2024 official 345 vs local 301; 2025 official 284 vs local 283.
- [ ] Verify the exact CDC download/archive version and local file identity for each annual XPT.
- [ ] Confirm whether any local processing, column filtering or import behaviour explains the differences.
- [ ] Update the audit report only after evidence supports a resolution. Do not edit the raw XPT files to force a match.

### Methods and reproducibility

- [ ] Compare every preprocessing statement with the locked notebook and `final_model_specification.csv`.
- [ ] Transcribe exact Python, pandas, NumPy and scikit-learn versions from `notebooks/artifacts/provenance/software_versions.txt` and `.json`.
- [ ] Confirm the exact three-fold cross-validation and model-tuning procedure.
- [ ] Confirm how categorical sentinel values and unknown categories were encoded in the fitted pipeline.
- [ ] Confirm the permutation-importance scoring metric and number of repeats from the analysis artefacts.
- [ ] Confirm the exact definition and baseline used for Brier skill score.
- [ ] Verify all numerical values against the machine-readable CSV outputs.

### Ethics and declarations

- [ ] Obtain the relevant institutional ethics approval, exemption or non-human-subjects determination.
- [ ] Confirm author affiliation, corresponding-author email and ORCID.
- [ ] Confirm funding and competing-interest statements.
- [ ] Confirm author contributions and acknowledgements.
- [ ] Complete the journal-specific AI-assisted writing disclosure.

### Reporting and presentation

- [ ] Complete the official 27-item TRIPOD+AI checklist against the final manuscript. The guideline is a reporting framework, not a quality appraisal tool.
- [ ] Revisit the provisional PROBAST+AI assessment as a separate quality/risk-of-bias appraisal; do not describe it as a reporting checklist.
- [ ] Confirm that all figures render from the repository-relative paths and meet journal resolution requirements.
- [ ] Check all references, in-text citations, table labels and figure captions.
- [ ] Confirm the target journal's word limits, reference style and supplementary-material requirements.
- [ ] Confirm that public repository code and artefacts are available at a fixed commit or release.

## Interpretation boundaries to preserve

- [x] Describe the outcome as prevalent self-reported MI/CHD.
- [x] Do not claim prospective cardiovascular-event prediction.
- [x] Do not claim clinical diagnosis, clinical utility or clinical validation.
- [x] Do not claim causal effects from permutation importance.
- [x] Describe weighted metrics as point estimates, not full design-based inference.
- [x] Describe subgroup results as descriptive, not as a formal fairness assessment.
- [x] Do not claim that BRFSS classification or temporal validation is novel in itself.
- [x] Do not claim statistical equivalence from the descriptive AUC difference.