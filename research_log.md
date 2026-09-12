# Research Log

> **Project:** Robust, Generalisable and Explainable Machine Learning for Cardiovascular Disease Prediction
> **Status:** Research planning and foundation
> **Primary language:** Python

---

## Current Status

- [x] Project directory created
- [x] Git repository initialised
- [x] Python virtual environment created
- [x] Virtual environment activated
- [x] VS Code interpreter configured
- [x] Research directory structure created
- [x] `.gitignore` configured
- [x] Initial repository files created
- [x] Initial Git commit completed

---

## Phase 1 — Research Foundations

**Date:** 2026-09-12

### 1. Research Objective

Investigate the robustness, reliability, explainability, and generalisability of machine-learning models for cardiovascular disease prediction.

The research will not focus solely on achieving the highest accuracy. It will investigate whether high performance on one dataset represents genuine generalisation to unseen and independent data.

---

### 2. Initial Research Question

> **How robust and generalisable are machine-learning models for cardiovascular disease prediction when evaluated using rigorous validation, calibration, interpretability, and external-dataset testing?**

#### Research Questions

* **RQ1:** Why does Random Forest exhibit exceptionally high predictive performance on the Cleveland cardiovascular disease dataset compared with other machine-learning algorithms?
* **RQ2:** To what extent do data characteristics, preprocessing, feature selection, and model configuration contribute to the observed performance?
* **RQ3:** To what extent does Random Forest performance generalise from the Cleveland dataset to independent cardiovascular datasets?

---

### 3. Initial Hypothesis

> **H1:** Random Forest may perform worse on an independent cardiovascular dataset than on the Cleveland dataset because the independent dataset contains unseen patients and potentially different data characteristics and distributions.

This hypothesis will be tested experimentally rather than assumed to be true.

---

## 4. Key Concepts Learned

### 4.1 Scientific Research vs Software Development

A software project primarily focuses on building a functional product, application, or system.

Scientific research focuses on systematically investigating questions, testing hypotheses, generating evidence, and developing knowledge.

**Key insight:**

> Software development focuses mainly on building a solution, while scientific research focuses on producing reliable evidence and knowledge through investigation.

---

### 4.2 Research Questions

A research question defines what the study is attempting to investigate.

The original observation of Random Forest achieving 100% accuracy led to a broader research question:

> Does exceptionally high performance on one cardiovascular dataset represent genuine generalisation, or is the performance specific to that dataset and experimental setup?

---

### 4.3 Hypothesis

A hypothesis is a testable prediction about what is expected to happen during an experiment.

The current hypothesis predicts that Random Forest performance may decrease when the model is evaluated on an independent cardiovascular dataset.

The result does not need to support the hypothesis. Unexpected results will also be treated as valid research findings.

---

### 4.4 Data Leakage

Data leakage occurs when information that should not be available during model training influences the training process.

This can result in artificially high or unrealistic model performance.

**Key principle:**

> Training data is used for learning, while genuinely unseen data is used for evaluation.

Potential leakage must be considered during:

* Data preprocessing
* Feature engineering
* Feature selection
* Hyperparameter tuning
* Model training
* Model evaluation

---

### 4.5 Training, Testing and Generalisation

The basic machine-learning workflow is:

```text
Training Data
     ↓
Model Learning
     ↓
Unseen Test Data
     ↓
Performance Evaluation
```

The test data must remain unseen during model development so that the evaluation provides meaningful evidence about generalisation.

---

### 4.6 Limitations of a Single 80/20 Split

A single 80/20 train-test split can provide a limited estimate of model performance, particularly when the dataset is relatively small.

Different random splits can produce different results because different observations are placed into the training and testing sets.

A favourable split could therefore produce an unusually high performance score.

**Key insight:**

> The result from one random split may depend on which observations happen to be selected for training and testing.

---

### 4.7 Cross-Validation

Cross-validation evaluates a model across multiple different splits of the available dataset.

For example, in 5-fold cross-validation:

```text
Fold 1 → Validation
Fold 2 → Validation
Fold 3 → Validation
Fold 4 → Validation
Fold 5 → Validation
```

Each fold is used for validation while the remaining folds are used for training.

This provides a more reliable estimate of performance than relying entirely on one random split.

---

### 4.8 Cross-Validation vs External Validation

These methods answer different research questions.

**Cross-validation:**

> How consistently does the model perform across different splits of the available dataset?

**External validation:**

> Does a model trained using one dataset continue to perform well on a completely independent dataset?

Both will be important for this research.

---

## 5. Important Research Insight

A Random Forest model achieving 100% accuracy on the Cleveland dataset should not automatically be considered a clinically reliable or highly generalisable model.

For example:

```text
Cleveland Dataset
       ↓
100% Accuracy
       ↓
Independent Dataset
       ↓
80% Accuracy
```

A substantial reduction in performance would be scientifically important.

It could indicate that the original 100% performance did not represent true external generalisation.

Therefore:

> **High accuracy on one dataset is an observation that requires investigation, not proof of generalisable performance.**

---

## 6. Research Principles Established

The following principles will guide the project:

* Do not optimise experiments simply to obtain a high accuracy score.
* Do not fabricate, manipulate, or cherry-pick results.
* Keep training and evaluation data properly separated.
* Investigate potential data leakage.
* Do not rely solely on one train-test split.
* Use appropriate cross-validation.
* Evaluate models using multiple metrics.
* Investigate calibration and reliability.
* Examine model interpretability.
* Test generalisation using independent datasets.
* Report unexpected and negative results honestly.
* Maintain reproducible experiments.
* Preserve raw datasets.
* Document experimental decisions and changes.

---

## 7. Reflection

Today I learned that machine-learning research is not simply about training a model and obtaining the highest possible accuracy.

A model can achieve extremely high performance on a particular dataset without necessarily generalising well to unseen data.

The previous 100% Random Forest result should therefore be treated as an observation requiring further investigation.

The new research will focus on whether the observed performance is robust, reproducible, interpretable, calibrated, and generalisable.

---

## 8. Next Step

Begin the Python research and data-science foundation.

### Planned Learning Progression

```text
Python Fundamentals
        ↓
NumPy
        ↓
Pandas
        ↓
Data Cleaning
        ↓
Statistics & Probability
        ↓
Data Visualisation
        ↓
Exploratory Data Analysis
        ↓
Machine Learning
        ↓
Model Evaluation
        ↓
Cross-Validation
        ↓
Hyperparameter Optimisation
        ↓
Calibration
        ↓
Explainability
        ↓
External Validation
        ↓
Scientific Writing & Publication
```

---

## 9. Questions to Revisit

* Why did Random Forest achieve 100% accuracy in the previous study?
* Was there any data leakage?
* How stable is Random Forest performance across different validation splits?
* How does performance change under rigorous cross-validation?
* Does the model remain effective on independent cardiovascular datasets?
* Are the model's predictions well calibrated?
* Which features contribute most strongly to predictions?
* Are feature contributions stable across datasets and validation folds?
* Does model performance differ across relevant patient subgroups?

---


# Phase 2 — Python Research Environment & Project Setup

## Objective

Establish a clean, isolated, version-controlled and reproducible
Python environment for the cardiovascular machine-learning research project.

## Environment

- Operating System: Windows
- Development Environment: Visual Studio Code
- Programming Language: Python
- Version Control: Git / GitHub
- Environment Management: Python `venv`

## Project Structure

The repository has been organised into separate directories for:

- raw, interim and processed data
- exploratory notebooks
- reusable source code
- preprocessing
- feature engineering
- machine-learning models
- model evaluation
- statistical analysis
- explainability
- experiments
- research results
- testing
- manuscript development

## Reproducibility Decision

A dedicated Python virtual environment (`.venv`) is being used so
that project dependencies remain isolated from other Python projects.

The `.venv` directory will not be committed to Git.

Project dependencies will instead be documented so that the
environment can be recreated by another researcher.

## Data Management Decision

Raw datasets will be preserved without modification.

Processed and intermediate datasets will be stored separately from
the original source data.

Dataset provenance, licensing, version and preprocessing decisions
will be documented before datasets are incorporated into the project.

## Version Control Decision

Git will be used throughout the research project to track changes
to code, documentation and research decisions.

Meaningful changes will be committed incrementally rather than
placing the entire completed research project into a single commit.


## Next Step

Verify the Python environment and establish the project's initial
dependency-management and reproducibility workflow before beginning
Python research programming.

### Environment Verification

Python environment verification confirmed that the project is using
the isolated `.venv` interpreter rather than the system-wide Python
installation.

```text
Python: 3.14.6
Git: 2.49.0.windows.1
Environment: .venv
Platform: Windows


---

## What comes immediately after this

Our order will be:

```text
Phase 1
Research Foundations
        ✓
        │
        ▼
Phase 2
Python Research Environment
        ✓
        │
        ├── Git repository
        ├── Virtual environment
        ├── Project architecture
        ├── Dependency management
        ├── GitHub repository
        └── Reproducibility check
                 │
                 ▼
        Python Fundamentals
                 │
                 ▼
              NumPy
                 │
                 ▼
              Pandas