# Cardiovascular Machine Learning Research

## Project Title

**Robust, Generalisable and Explainable Machine Learning for Cardiovascular Disease Prediction**

## Overview

This repository contains the development of a research project investigating the robustness, reliability, explainability, calibration and generalisability of machine-learning models for cardiovascular disease prediction.

The project builds upon observations from previous research in which Random Forest achieved exceptionally high predictive performance on the Cleveland Heart Disease dataset.

Rather than assuming that high performance represents true generalisation, this research investigates whether such results remain reliable under more rigorous experimental conditions.

## Main Research Question

> How robust and generalisable are machine-learning models for cardiovascular disease prediction when evaluated using rigorous validation, calibration, interpretability and external-dataset testing?

## Initial Research Questions

1. Why does Random Forest exhibit exceptionally high predictive performance on the Cleveland cardiovascular disease dataset compared with other machine-learning algorithms?

2. To what extent do data characteristics, preprocessing, feature selection and model configuration contribute to the observed performance?

3. To what extent does Random Forest performance generalise from the Cleveland dataset to independent cardiovascular datasets?

## Research Principles

The project follows several core principles:

* Reproducible experimentation
* Proper separation of training and evaluation data
* Explicit investigation of data leakage
* Cross-validation rather than reliance on a single random split
* Multiple evaluation metrics
* Calibration analysis
* Model explainability
* Statistical evaluation
* External validation
* Transparent reporting of positive and negative results
* Preservation of raw datasets
* Version-controlled research development

## Repository Structure

```text
cardiovascular-ml-research/
│
├── data/
│   ├── raw/
│   ├── interim/
│   └── processed/
│
├── notebooks/
│
├── src/
│   ├── data/
│   ├── preprocessing/
│   ├── features/
│   ├── models/
│   ├── evaluation/
│   ├── explainability/
│   └── statistics/
│
├── configs/
├── experiments/
│
├── results/
│   ├── tables/
│   └── figures/
│
├── tests/
├── paper/
│
├── research_log.md
├── requirements.txt
├── README.md
└── .gitignore
```

## Current Research Stage

**Phase 2 — Python Research Environment and Project Setup**

Current work includes:

* Research methodology foundations
* Research question development
* Python environment configuration
* Git/GitHub version control
* Repository architecture
* Reproducibility planning

Machine-learning experiments have not yet begun.

## Programming Environment

* Python
* Visual Studio Code
* Git
* GitHub
* Python virtual environment (`venv`)

## Data

Datasets will be obtained only from documented and authoritative sources where possible.

Raw datasets will remain unchanged.

Intermediate and processed datasets will be stored separately so that all transformations can be reproduced.

Dataset provenance, access conditions, licensing, version information and preprocessing decisions will be documented.

## Reproducibility

The repository uses an isolated Python virtual environment.

The local `.venv` directory is intentionally excluded from Git.

Dependencies will be recorded so that the research environment can be recreated independently.

## Status

This project is currently under active research development.

Results, conclusions and model-performance claims should therefore not be interpreted as final until the experimental methodology and validation stages have been completed.
