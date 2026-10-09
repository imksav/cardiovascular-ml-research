# Project Status

**Research title:** Cardiovascular Machine Learning Research: BRFSS-Based Classification of Prevalent Self-Reported Myocardial Infarction and Coronary Heart Disease with Temporal Validation

**Current milestone:** Phase 1 — Completed Experimental Analysis.

**Release version:** `v0.1.0`

**Release date:** 9 October 2026

**Release status:** Published as a GitHub pre-release.

**Current research stage:** Transitioning from completed computational analysis to Phase 2 — Literature Review and Research Positioning.

**GitHub Release:** [v0.1.0 — Phase 1: Completed Experimental Analysis](https://github.com/imksav/cardiovascular-ml-research/releases/tag/v0.1.0)

---

## 1. Completed: Phase 1 — Research Implementation

Phase 1 established a reproducible machine-learning workflow for classifying prevalent self-reported myocardial infarction (MI) and/or coronary heart disease (CHD) using CDC BRFSS survey data.

### Data Preparation and Research Design

- [x] Inspect BRFSS 2023 source data and variable coding.
- [x] Validate the cardiovascular outcome `_MICHD`.
- [x] Identify and exclude direct target-construction variables to prevent leakage.
- [x] Establish the final six-predictor analytical specification.
- [x] Apply documented missing-value handling and preprocessing.
- [x] Establish a stratified 70/15/15 training, validation and held-out test split.
- [x] Document dataset selection and cross-year variable compatibility.

### Machine-Learning Development

- [x] Compare five candidate machine-learning algorithms.
- [x] Establish Logistic Regression as a comparative benchmark.
- [x] Select and tune the primary Gradient Boosting model.
- [x] Select the classification threshold using validation data.
- [x] Freeze the final model, preprocessing configuration and threshold.
- [x] Preserve trained models and reproducibility artifacts.

### Model Evaluation

- [x] Evaluate the frozen model on the independent BRFSS 2023 held-out test set.
- [x] Assess BRFSS 2024 variable compatibility.
- [x] Conduct unchanged-model temporal evaluation using BRFSS 2025.
- [x] Evaluate ROC-AUC, average precision, Brier score and classification metrics.
- [x] Examine probability calibration.
- [x] Conduct survey-weighted evaluation sensitivity analyses.
- [x] Evaluate permutation feature importance.
- [x] Assess missing-data robustness and threshold behaviour.
- [x] Examine performance differences across relevant population subgroups.

### Final Computational Results

| Evaluation Metric | BRFSS 2023 Held-Out | BRFSS 2025 Temporal |
|---|---:|---:|
| Respondents | 64,311 | 352,145 |
| Outcome prevalence | 8.47% | 9.00% |
| ROC-AUC | **0.8012** | **0.7949** |
| Average Precision | 0.2449 | 0.2488 |
| Brier Score | 0.0697 | 0.0738 |
| Sensitivity | 0.5628 | 0.5618 |
| Specificity | 0.8295 | 0.8199 |
| F1 Score | 0.3305 | 0.3322 |

The approximately 0.0063 decrease in ROC-AUC indicates broadly stable discrimination between the evaluated survey years.

These findings relate to prevalent self-reported disease classification and do not establish clinical validity or prospective cardiovascular risk prediction.

---

## 2. Completed: GitHub Repository Establishment

The repository was established with a new Git history and a professional structure for scientific research development.

### Repository Management

- [x] Initialise a fresh Git repository.
- [x] Establish `main` as the stable branch.
- [x] Create the initial Phase 1 research commit.
- [x] Push the completed research snapshot to GitHub.
- [x] Configure `.gitignore` to exclude raw BRFSS datasets, the virtual environment and the local PDF export.
- [x] Establish repository documentation and contribution guidelines.
- [x] Configure GitHub Actions repository-integrity checks.
- [x] Verify successful execution of the initial GitHub Actions workflow.
- [x] Create and push the annotated `v0.1.0` Git tag.
- [x] Publish the Phase 1 GitHub pre-release.

### Included Research Materials

- Final optimised Jupyter notebook.
- HTML research report.
- Frozen Gradient Boosting and Logistic Regression model artifacts.
- Machine-readable experimental results.
- Research figures and visualisations.
- Dataset, model and software provenance records.
- Research methodology and supporting documentation.
- GitHub workflow, issue templates and pull-request guidance.

**Primary notebook:** [03_brfss_2023_first_look_optimised.ipynb](../notebooks/03_brfss_2023_first_look_optimised.ipynb)

**HTML report:** [03_brfss_2023_first_look_optimised.html](../reports/03_brfss_2023_first_look_optimised.html)

**Permanent Phase 1 reference:** [v0.1.0](https://github.com/imksav/cardiovascular-ml-research/releases/tag/v0.1.0)

### Reproducibility Status

The initial repository audit and GitHub Actions checks passed.

These checks validate repository structure and selected file integrity. They do **not** independently demonstrate complete clean-kernel notebook execution, full experimental replication or clinical validation.

The released `v0.1.0` tag preserves the computational baseline for subsequent research development.

---

## 3. Next: Phase 2 — Literature Review and Research Positioning

**Status:** Not started.

**Planned working branch:** `phase/02-literature-review`

**Objective:** Establish a verified scientific literature foundation, identify relevant research gaps, and develop a defensible positioning of the completed BRFSS analysis.

### Planned Tasks

- [ ] Create the Phase 2 working branch.
- [ ] Review the existing literature matrix and search-strategy documents.
- [ ] Define and document the literature search strategy.
- [ ] Search relevant academic databases and scholarly sources.
- [ ] Verify publication details, DOIs and research findings.
- [ ] Establish transparent inclusion and exclusion criteria.
- [ ] Compare related cardiovascular machine-learning studies.
- [ ] Examine literature on temporal validation, model calibration and generalisability.
- [ ] Assess evidence concerning survey-weighted evaluation and subgroup performance.
- [ ] Identify research gaps supported by verified literature.
- [ ] Refine manuscript research questions where scientifically justified.
- [ ] Prepare a critical literature synthesis.
- [ ] Update the research log and project documentation.
- [ ] Review and merge completed Phase 2 contributions into `main`.

### Research Integrity

The completed Phase 1 experimental specification is preserved.

Literature findings may lead to refinements in manuscript framing, interpretation or research-question wording.

Any substantive change to the locked predictors, model, outcome, preprocessing or experimental results must be clearly documented as a new analysis or research extension.

---

## 4. Future Research Phases

| Phase | Scope | Status |
|---|---|---|
| Phase 1 | Computational research implementation and validation | Completed |
| Phase 2 | Literature review and research positioning | Next |
| Phase 3 | Scientific manuscript development | Not started |
| Phase 4 | Scientific and reproducibility review | Not started |
| Phase 5 | Journal selection, submission and publication preparation | Not started |

### Phase 3 — Manuscript Development

Prepare the scientific manuscript using the completed experimental results and verified literature.

The planned writing sequence is:

Methods → Results → Discussion → Introduction → Abstract.

### Phase 4 — Scientific Review

Review methodological reporting, reproducibility, research limitations, references, tables, figures and consistency between the manuscript and computational results.

### Phase 5 — Publication Preparation

Identify suitable research journals, assess submission requirements, prepare publication materials, and complete the scientific submission process when the manuscript is ready.

Journal acceptance or publication is not assumed.

---

## 5. GitHub Research Development Strategy

The repository uses a phase-oriented development workflow.

| Branch / Tag | Purpose |
|---|---|
| `main` | Stable, reviewed research |
| `v0.1.0` | Completed Phase 1 computational baseline |
| `phase/02-literature-review` | Literature verification and research positioning |
| `phase/03-manuscript-writing` | Scientific manuscript development |
| `phase/04-scientific-review` | Scientific and reproducibility assessment |
| `phase/05-publication` | Publication preparation |

Only the current working phase needs an active development branch.

Meaningful changes will be documented through Git commits, GitHub Issues, pull requests, the changelog and research log.

Version tags will identify significant reviewed milestones rather than routine documentation edits.

---

## 6. Scientific Interpretation Boundaries

This study classifies **prevalent self-reported MI/CHD** among BRFSS survey respondents.

It does not:

- Predict future cardiovascular events.
- Establish causal relationships.
- Provide clinical diagnosis or treatment recommendations.
- Constitute a clinically validated cardiovascular risk assessment system.
- Establish generalisability to populations outside the evaluated BRFSS survey years.

Survey-weighted predictive-performance results are reported as point estimates, without full complex-survey inferential uncertainty estimation.

These limitations will remain explicit throughout manuscript preparation and publication.

---

## 7. Related Project Documentation

- [README.md](../README.md) — Project overview and principal findings.
- [CHANGELOG.md](../CHANGELOG.md) — Completed repository milestones and release history.
- [research_log.md](../research_log.md) — Chronological research activities and methodological decisions.
- [research_protocol.md](research_protocol.md) — Research design and methodology.
- [dataset_selection.md](dataset_selection.md) — Dataset-selection decisions.
- [data_dictionary.md](data_dictionary.md) — Source variables, analytical definitions and transformations.
- [research_questions.md](research_questions.md) — Current documented research questions, subject to justified refinement.
- [CITATION.cff](../CITATION.cff) — Repository citation metadata.

---

**Last updated:** 9 October 2026

**Current status:** Phase 1 completed and released as `v0.1.0`; Phase 2 literature review is the next research milestone.
