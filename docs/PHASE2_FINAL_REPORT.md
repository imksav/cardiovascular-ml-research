# PHASE 02 FINAL REPORT
## Literature Review, Research Positioning and Methodological Appraisal

**Project title:** Cardiovascular Machine Learning Research: BRFSS-Based Classification of Prevalent Self-Reported Myocardial Infarction and Coronary Heart Disease with Temporal Validation

**Research repository:** `imksav/cardiovascular-ml-research`

**Project branch:** `phase/02-literature-review`

**Document status:** Phase 02 closeout report

**Version:** 1.0

**Prepared:** 25 October 2026

---

## Document Control

| Item | Description |
|---|---|
| Project phase | Phase 02 — Literature review and research positioning |
| Primary research domain | Machine learning, cardiovascular health and population-health data |
| Data source | CDC Behavioral Risk Factor Surveillance System (BRFSS) |
| Development year | 2023 |
| Temporal evaluation year | 2025 |
| Primary outcome | Prevalent self-reported myocardial infarction or coronary heart disease history |
| Primary model | Gradient Boosting classifier |
| Secondary model | L2-regularised Logistic Regression |
| Reporting framework | TRIPOD+AI |
| Risk-of-bias framework | PROBAST+AI |
| Review design | Targeted narrative/scoping literature review |
| Phase outcome | Research positioning established; Phase 03 can proceed subject to documented data-provenance controls |

### Important interpretation statement

This project classifies a **previously reported history of myocardial infarction or coronary heart disease** using cross-sectional survey data. It does not predict future cardiovascular events, establish a clinical diagnosis, estimate causal effects or demonstrate clinical readiness.

The 2025 evaluation uses a separate annual survey sample. It is a temporal transportability assessment, not longitudinal follow-up of the 2023 respondents.

---

<!-- PAGE BREAK -->

# Executive Summary

## 1. Purpose

Phase 02 was undertaken to establish the scientific context, assess relevant cardiovascular machine-learning research, identify methodological and reporting weaknesses in the available evidence, and define a defensible research contribution for the existing BRFSS-based project.

The review focused on studies using BRFSS or related population-health data, machine-learning approaches to cardiovascular classification, temporal or external validation, risk-of-bias assessment, model calibration and reporting transparency.

The work builds on Phase 01, which established the initial dataset-processing and modelling workflow. Phase 02 does not replace the existing experimental record. Instead, it documents how the study should be interpreted, where it fits within the literature, which claims are supportable and what must be addressed before further experiments.

## 2. Research problem

Machine-learning models can identify statistical patterns associated with cardiovascular disease history. However, strong performance within one dataset does not necessarily demonstrate that a model will perform similarly in another survey year, population or clinical setting.

Several issues are particularly important in population-health classification:

- Outcome definitions must be transparent and consistent.
- Predictors must not inadvertently contain the outcome or information recorded after the outcome occurred.
- Imbalanced outcomes require more than accuracy as a performance measure.
- Discrimination, calibration and threshold-dependent classification performance answer different questions.
- Complex survey sampling can affect prevalence estimates and model evaluation.
- Temporal validation must be distinguished from longitudinal prediction and external clinical validation.
- Data provenance, missingness and reproducibility need to be documented before the results can support strong scientific claims.

These issues motivate the project's emphasis on a locked predictor set, a predefined model specification, threshold selection using the validation partition, and evaluation on a separate annual BRFSS sample.

## 3. Project design

The study uses BRFSS 2023 for model development and internal held-out evaluation, followed by evaluation on BRFSS 2025. The target represents a history of myocardial infarction or coronary heart disease. Six predictors are used:

1. Age group
2. Physical activity
3. Smoking status
4. High blood pressure status
5. Diabetes status
6. Body mass index

The primary classifier is Gradient Boosting, with Logistic Regression serving as a secondary model. The recorded training workflow uses a stratified 70/15/15 split, random seed 42, three-fold stratified cross-validation on the training partition, and a classification threshold selected by maximising validation F1.

## 4. Principal results

| Evaluation | BRFSS 2023 held-out test | BRFSS 2025 temporal sample |
|---|---:|---:|
| Evaluation sample size | 64,311 | 352,145 |
| Unweighted outcome prevalence | 8.47% | 9.00% |
| ROC-AUC | 0.8012 | 0.7949 |
| Average Precision | 0.2449 | 0.2488 |
| Brier score | 0.0697 | 0.0738 |
| Accuracy | 0.8070 | 0.7967 |
| Precision | 0.2340 | 0.2358 |
| Sensitivity | 0.5628 | 0.5618 |
| Specificity | 0.8295 | 0.8199 |
| F1 score | 0.3305 | 0.3322 |

The results indicate broadly similar discrimination and threshold-dependent sensitivity across the two annual samples. ROC-AUC decreases modestly in 2025, while Average Precision is slightly higher. The Brier score is higher in 2025, indicating a modest deterioration in overall probabilistic accuracy under that metric.

The similar sensitivity and F1 values are encouraging evidence of temporal performance stability under the recorded evaluation design. They do not establish equivalence between the two years, because confidence intervals, formal equivalence testing and complete design-based uncertainty estimates are not reported here.

## 5. Research positioning

The study's contribution should not be framed as the first application of machine learning to cardiovascular disease using BRFSS. The literature already includes directly relevant work using BRFSS and prevalent myocardial infarction or coronary heart disease outcomes, including Noh et al. (2026).

A more defensible contribution is the transparent evaluation of a locked, six-predictor model developed using BRFSS 2023 and applied to a separate BRFSS 2025 annual sample, accompanied by discrimination, calibration, threshold-based metrics, survey-weighted point estimates, subgroup and missingness considerations, and explicit reporting of data-provenance limitations.

## 6. Phase 02 conclusion

Phase 02 is complete for its defined targeted narrative/scoping purpose. It is not a completed systematic review and should not be presented as one.

The principal outstanding research-control issue is the discrepancy between the recorded local dataset column counts and the counts listed in the corresponding official CDC annual documentation. This discrepancy must remain visible in the project record and be investigated through a documented provenance process. The raw data and locked experiment should not be silently replaced or rerun to make the discrepancy disappear.

---

<!-- PAGE BREAK -->

# 1. Introduction

## 1.1 Background

Cardiovascular diseases remain an important public-health concern, and data-driven methods are increasingly used to investigate the relationship between demographic characteristics, health behaviours, self-reported conditions and cardiovascular outcomes.

Machine-learning methods offer flexible ways to represent nonlinear associations and interactions between variables. They can be useful for classification tasks in which the relationship between candidate predictors and the target is not adequately represented by a simple linear model.

However, flexibility does not automatically produce reliable prediction. A model can appear accurate because of data leakage, target leakage, selection bias, an inappropriate evaluation strategy or reliance on variables that would not be available at the intended time of use. It may also fail to transport across populations, survey years or data-collection procedures.

This project therefore treats model evaluation as a methodological problem rather than an exercise in maximising a single score.

## 1.2 Study context

The Behavioral Risk Factor Surveillance System is a large-scale US health survey. Its annual datasets provide a basis for investigating self-reported health conditions and associated characteristics across survey respondents.

The project uses BRFSS data to classify prevalent history of myocardial infarction or coronary heart disease. The analysis is based on survey responses and associated derived variables, rather than prospectively observed clinical events.

This distinction determines the appropriate interpretation of the results. A model trained to distinguish respondents with and without a reported history of cardiovascular disease is not automatically a model for predicting who will experience a future event.

## 1.3 Research problem

The central methodological problem is how to develop and evaluate a relatively simple cardiovascular classification model while maintaining a transparent relationship between the outcome definition, predictor availability, model-development procedure and evaluation population.

The project also addresses a common problem in applied machine learning: performance is frequently reported from a single random split, while evidence about temporal transportability, calibration, threshold selection, survey weighting and provenance may be incomplete.

## 1.4 Aim

To evaluate a reproducible machine-learning approach for classifying prevalent self-reported myocardial infarction or coronary heart disease using six selected BRFSS predictors, with model development on BRFSS 2023 and temporal evaluation on a separate BRFSS 2025 annual sample.

## 1.5 Objectives

The objectives are to:

1. Establish the relevant cardiovascular machine-learning and population-health modelling literature.
2. Identify methodological risks related to leakage, outcome definition, class imbalance, calibration, survey design and validation.
3. Define a fixed six-predictor model specification.
4. Evaluate the primary model using discrimination, probabilistic and threshold-dependent metrics.
5. Assess performance on a separate annual sample without treating it as longitudinal follow-up.
6. Document limitations, data provenance and reporting requirements.
7. Establish an actionable Phase 03 research plan.

## 1.6 Research questions

**RQ1.** How well does the locked Gradient Boosting classifier distinguish BRFSS respondents with and without a reported history of myocardial infarction or coronary heart disease in the held-out 2023 test partition?

**RQ2.** How similar are the recorded discrimination, probabilistic performance and threshold-dependent metrics when the locked model is applied to the separate BRFSS 2025 sample?

**RQ3.** What methodological safeguards are required to interpret this classification task responsibly, particularly in relation to target leakage, outcome prevalence, calibration, survey weighting and data provenance?

**RQ4.** What specific contribution can be defended in light of existing BRFSS-based cardiovascular machine-learning research?

---

<!-- PAGE BREAK -->

# 2. Scope and Review Methodology

## 2.1 Review design

Phase 02 used a targeted narrative/scoping approach to identify and compare literature relevant to the project's methods and research question.

The review was intended to establish research positioning and identify methodological considerations. It was not designed as a systematic review with exhaustive database coverage, duplicate independent screening, a registered protocol or a complete reproducible search-export archive.

The distinction is important. The evidence synthesis can support a reasoned account of the relevant literature, but it cannot establish that every eligible publication was identified.

## 2.2 Main evidence areas

The review covered the following areas:

- BRFSS-based cardiovascular classification and prediction.
- Machine-learning evaluation for imbalanced binary outcomes.
- Temporal validation and transportability across annual datasets.
- Outcome definition and possible predictor leakage.
- Discrimination, calibration and threshold-dependent performance.
- Complex survey sampling and survey-weighted evaluation.
- Risk-of-bias appraisal for prediction-model research.
- Reporting guidance for regression and machine-learning prediction models.
- Reproducibility and provenance of public-health datasets.

## 2.3 Evidence-selection approach

The project's literature files document the seed sources, screening decisions, evidence matrix, search strategy and synthesis. The working evidence base contains 16 core evidence records, with a smaller deduplicated seed-source list.

Selection prioritised relevance to the study design and methodological questions rather than attempting to collect every paper that mentions cardiovascular disease and machine learning.

Particular attention was given to studies that used BRFSS, classified self-reported myocardial infarction or coronary heart disease, reported discrimination or classification metrics, or discussed validation and survey-aware modelling.

Where a paper's outcome definition, metric calculation or methods could not be independently established from the accessible material, the report does not treat the result as a fully verified comparator.

## 2.4 Limitations of the review process

The following limitations define the strength of the conclusions that can be drawn:

1. **No exhaustive search archive.** A complete set of database exports and exact record counts is not available in the documented review.
2. **No dual independent screening.** Screening and appraisal were not performed by two independent reviewers.
3. **Unequal full-text access.** Some publications were assessed using accessible abstracts, tables or partial text rather than a complete full-text methods review.
4. **Incomplete comparability.** Papers differ in outcome definition, population, predictors, sampling design, data processing, validation and metric reporting.
5. **Potential publication and selection bias.** A targeted review cannot reliably quantify the extent to which favourable results are overrepresented.
6. **No PRISMA flow diagram.** Because this was not an exhaustive systematic review with a complete search and screening record, a PRISMA flow diagram would imply a level of process completeness that has not been established.

These limitations do not make the review uninformative. They define it as a targeted evidence synthesis and prevent unsupported claims of systematic completeness.

## 2.5 Evidence extraction

The literature matrix records study characteristics and relevant methodological observations. The evidence was considered in relation to:

- Data source and survey year.
- Target definition.
- Candidate predictors and possible leakage.
- Model families.
- Validation strategy.
- Discrimination and threshold-based metrics.
- Calibration and probabilistic evaluation.
- Survey weighting.
- Reproducibility and reporting quality.
- Relevance to the current project's design.

Results from studies with uncertain outcome mappings or conflicting reported metrics were not treated as directly comparable benchmark values.

---

<!-- PAGE BREAK -->

# 3. Critical Literature Synthesis

## 3.1 Directly relevant BRFSS cardiovascular research

### Noh et al. (2026)

Noh et al. provide a particularly relevant comparator because the study uses BRFSS 2023 and a prevalent myocardial infarction/coronary heart disease outcome aligned with `_MICHD`.

The reported Gradient Boosting ROC-AUC is approximately 0.867 in the inclusive analysis and 0.858 after excluding post-diagnosis proxy variables. The corresponding reported precision-recall AUC values are approximately 0.389 and 0.372. The study also reports calibration-related analysis and a survey-weighted Logistic Regression sensitivity analysis.

The study matters for two reasons.

First, it establishes that BRFSS-based classification of prevalent cardiovascular disease history is already an active research direction. The current project must not claim novelty merely because it applies machine learning to BRFSS or evaluates an MI/CHD-history outcome.

Second, its comparison of inclusive and restricted predictor sets illustrates the importance of examining variables that could encode information related to the outcome or its consequences.

The current project uses a smaller, fixed six-predictor set. The numerical results should not be compared head-to-head with Noh et al. because a valid comparison would require aligned preprocessing, target construction, sample definitions, predictors, validation design, threshold rules, metric implementations and weighting.

### Chavda and Hyun (2024)

Chavda and Hyun report BRFSS 2022-based heart-disease modelling, with accuracy values around 0.724–0.725 and Matthews correlation coefficient values around 0.305–0.307 in the project’s extracted notes.

These results illustrate why accuracy alone is insufficient for imbalanced health outcomes. The Matthews correlation coefficient offers a complementary summary of classification performance across the confusion matrix.

However, the precise target-code mapping was not independently confirmed in the review record. The paper should therefore be used as contextual evidence, not as a fully aligned benchmark for the present MI/CHD-history target.

### Imani et al. (2026)

Imani et al. describe BRFSS 2022-based heart-disease modelling. The available abstract and table information contain inconsistencies between reported accuracy and class counts.

Where published counts and reported metrics do not reconcile, those values should not be adopted as reliable benchmarks without further source verification. The paper remains relevant to the breadth of cardiovascular machine-learning applications, but disputed metrics should not be used to claim superiority or inferiority.

### Wu et al. (2026)

Wu et al. examine BRFSS-to-NHANES validation, with abstract-level AUC values reported around 0.825 and 0.851.

The work is relevant because it addresses evaluation across data sources rather than relying exclusively on a random partition of a single dataset. However, the exact alignment of outcome definitions, sampling weights and other design choices was not fully verified during this review.

The paper supports the general importance of transportability assessment, but its metrics are not directly comparable with the current project's scores.

### Deng et al. (2025)

Deng, Lu and Hu examine heart-disease prediction using BRFSS 2015 alongside other datasets, including Framingham and Z-Alizadeh Sani data.

The study illustrates the diversity of datasets and target formulations used in cardiovascular prediction research. It also reinforces the need to state precisely which population, outcome and data source a model represents.

Results from datasets with different clinical or survey definitions should not be treated as interchangeable evidence of performance on the current BRFSS target.

### Wanyonyi et al. (2025)

Wanyonyi et al. use a BRFSS-derived secondary dataset. The methods text raises a question about whether SMOTE may have been applied before train/test splitting.

Applying synthetic oversampling before splitting can allow information derived from the eventual test observations to influence the training process, producing optimistic evaluation results. However, the concern identified in the review is not a confirmed code-level finding. It must be described as a potential methodological risk rather than established leakage.

The practical lesson for this project is to keep preprocessing and any resampling operations confined to the appropriate training workflow, with validation and test partitions protected from information leakage.

### Kung et al. (2026)

Kung et al. examine annual BRFSS temporal validation for a cross-sectional diabetes classification problem.

Although the outcome differs from the current cardiovascular target, the design is relevant: a model can be evaluated on a separate annual survey sample without implying that the same individuals were followed over time.

The full text was not available for a complete appraisal during this review pass. The study therefore provides contextual support for annual temporal validation but cannot be treated as a fully appraised methodological template.

## 3.2 Survey-aware machine learning

Oh et al. (2026) address machine-learning methods in survey-data settings. This is relevant because BRFSS is based on a complex sampling design rather than a simple random sample of the US population.

Survey weights, strata and primary sampling units affect population representation and the calculation of design-based uncertainty. An unweighted model score describes performance in the analysed sample; it does not automatically represent performance under the survey's population-representation framework.

The current project reports survey-weighted point estimates as a sensitivity analysis. These are useful, but they are not a substitute for complete design-based uncertainty estimation. In particular, point estimates alone do not establish confidence intervals, statistically significant differences or population-level equivalence between annual samples.

## 3.3 Prediction-model performance and calibration

Steyerberg et al. (2010) provide a framework for evaluating prediction models using complementary measures rather than a single summary score.

Van Calster et al. (2019) emphasise calibration as a critical component of predictive analytics. A model may rank respondents reasonably well while producing probabilities that are systematically too high or too low.

These principles are directly relevant to the current project:

- ROC-AUC assesses ranking discrimination.
- Average Precision summarises precision-recall performance, which is particularly useful for an imbalanced outcome.
- The Brier score measures squared error in predicted probabilities and reflects both calibration and discrimination.
- Sensitivity, specificity, precision and F1 depend on the selected classification threshold.
- Accuracy must be interpreted against the outcome prevalence and the performance of simple baseline classifiers.

No single metric establishes clinical usefulness. The metrics should be interpreted together and in the context of the target's intended meaning.

## 3.4 Reporting and risk-of-bias frameworks

### TRIPOD+AI

Collins et al. (2024) provide updated reporting guidance for prediction models developed using regression or machine-learning methods.

The current project's 52-item TRIPOD+AI audit is intended to make reporting requirements visible and actionable. It should be interpreted as a reporting audit, not as proof that the model is valid or that all requirements have been satisfied.

### PROBAST+AI

Moons et al. (2025) provide an updated framework for assessing risk of bias and applicability in prediction-model studies involving regression or artificial intelligence.

The project includes a provisional desk appraisal of six accessible comparator studies and the current project. Kung et al. was not assigned a complete rating because the available material was insufficient.

The appraisal was undertaken by a single reviewer and was not an independent formal assessment. Its role is to identify methodological concerns and areas requiring verification, not to produce definitive risk-of-bias judgements.

## 3.5 Broader reviews

Cai et al. (2024) and Liu et al. (2025) provide broader review-level context for machine learning in cardiovascular or health prediction research.

Such reviews are useful for understanding the field's recurring challenges, including heterogeneity in datasets, outcomes, evaluation strategies and reporting. However, broad review conclusions cannot replace examination of the exact outcome and validation design used in a particular comparator study.

## 3.6 Synthesis of the evidence

Across the reviewed literature, five themes are particularly relevant.

**First, target definition is fundamental.** Studies using different cardiovascular outcomes cannot be treated as direct benchmarks merely because their labels contain similar disease names.

**Second, validation design matters.** A random test partition, an annual temporal sample, an external dataset and longitudinal follow-up answer different questions.

**Third, leakage must be controlled.** Predictors that directly encode the outcome or information arising after the outcome can make a model appear more useful than it is.

**Fourth, discrimination is not enough.** Calibration, threshold selection, class imbalance and the practical costs of false positives and false negatives need explicit treatment.

**Fifth, reproducibility includes provenance.** A documented model pipeline is not fully reproducible if the exact source dataset version and its relationship to official documentation remain unresolved.

The project's strongest methodological position is therefore transparency about what the analysis establishes, what it does not establish, and what remains to be tested.

---

<!-- PAGE BREAK -->

# 4. Research Gap and Contribution

## 4.1 What is not a defensible research gap

The following claims are not supported by the current review:

- That this is the first use of machine learning for cardiovascular disease using BRFSS.
- That annual temporal validation is itself a novel method.
- That Gradient Boosting is universally superior for cardiovascular prediction.
- That the model is clinically validated.
- That the model predicts future myocardial infarction or coronary heart disease.
- That the model generalises to clinical populations outside BRFSS.
- That the current results demonstrate causal relationships between predictors and cardiovascular disease.

Directly relevant prior work, especially Noh et al. (2026), prevents a broad novelty claim based solely on the dataset and outcome.

## 4.2 Defensible contribution

The contribution is narrower and methodological:

> This study documents the development and evaluation of a locked six-predictor Gradient Boosting classifier for prevalent self-reported myocardial infarction or coronary heart disease history using BRFSS 2023, followed by application to a separate BRFSS 2025 annual sample. It reports discrimination, probabilistic and threshold-dependent performance, selected survey-weighted point estimates, and explicit limitations concerning outcome interpretation, data provenance and transportability.

The contribution rests on the combination of:

1. A deliberately restricted predictor set.
2. Explicit separation of outcome-construction variables from predictors.
3. A documented development and threshold-selection procedure.
4. Evaluation on a separate annual survey sample.
5. Reporting of complementary performance metrics.
6. Inclusion of survey-weighted point estimates as a sensitivity analysis.
7. Explicit documentation of unresolved dataset-version discrepancies.
8. A structured reporting and risk-of-bias audit.

These elements should be described as the study's design and reporting contribution, not as proof of methodological novelty across the entire literature.

## 4.3 Research positioning statement

The study is best positioned as a reproducible population-health machine-learning evaluation examining whether a compact classifier maintains broadly similar performance across two annual BRFSS samples.

It is not positioned as a clinical risk score, an individualised future-event prediction model or a substitute for clinical assessment.

---

<!-- PAGE BREAK -->

# 5. Data and Experimental Design

## 5.1 Data sources and cohorts

The study uses BRFSS 2023 for development and internal evaluation, followed by a separate BRFSS 2025 annual sample for temporal evaluation.

The recorded cohort counts are:

| Cohort or partition | Respondents with known outcome |
|---|---:|
| BRFSS 2023, full analysed cohort | 428,738 |
| BRFSS 2023, training partition | 300,116 |
| BRFSS 2023, validation partition | 64,311 |
| BRFSS 2023, held-out test partition | 64,311 |
| BRFSS 2025, analysed temporal sample | 352,145 |

The 2023 partition counts sum to the full 2023 analysed cohort. The recorded split is approximately 70% training, 15% validation and 15% testing.

The 2023 source file contains 433,323 respondents before exclusion of observations with unknown outcome. The 2025 source file contains 356,158 respondents before exclusion of observations with unknown outcome.

## 5.2 Outcome definition

The outcome represents prevalent self-reported history of myocardial infarction or coronary heart disease.

The project uses the relevant BRFSS cardiovascular history items, including `CVDINFR4` and `CVDCRHD4`, to construct or inspect the target. These variables are not included as predictors.

The target should be interpreted as a report of prior disease history, not a record of incident disease during follow-up.

## 5.3 Predictor specification

The primary model uses the following six predictors.

| Analytical feature | BRFSS source variable | Concept |
|---|---|---|
| `AGE_GROUP` | `_AGEG5YR` | Age group |
| `PHYSICAL_ACTIVITY` | `EXERANY2` | Physical activity |
| `SMOKING_STATUS` | `_SMOKER3` | Smoking status |
| `BLOOD_PRESSURE` | `BPHIGH6` | High blood pressure status |
| `DIABETES_STATUS` | `DIABETE4` | Diabetes status |
| `BMI` | `_BMI5` | Body mass index |

The model's predictor set is intentionally compact. It should not be described as a comprehensive clinical feature set.

The BRFSS survey-design variables `_LLCPWT`, `_STSTR` and `_PSU` are not model predictors. Their role is related to survey representation and analysis, not direct input to the classifier.

## 5.4 Model-development procedure

The recorded workflow uses:

- Stratified 70/15/15 train/validation/test partitioning.
- Random seed 42.
- Three-fold stratified cross-validation on the training partition.
- Candidate models comprising Logistic Regression, Gaussian Naive Bayes, Decision Tree, Random Forest and Gradient Boosting.
- Gradient Boosting as the primary classifier.
- L2-regularised Logistic Regression as the secondary model.
- Validation-based selection of a classification threshold by maximising F1.

The primary Gradient Boosting hyperparameters are:

| Parameter | Recorded value |
|---|---:|
| `n_estimators` | 150 |
| `learning_rate` | 0.10 |
| `max_depth` | 3 |
| Selected threshold | 0.1529128096 |

The selected threshold is approximately 0.153, rather than the conventional 0.5 probability threshold.

This choice reflects the validation-based F1 optimisation objective. It should not be interpreted as a clinically optimal decision threshold. A clinical threshold would require a defined use case, decision consequences and an explicit assessment of the relative costs of false positives and false negatives.

## 5.5 Temporal evaluation

The model specification developed using BRFSS 2023 is applied to the separate BRFSS 2025 sample.

The 2025 sample is not used as a replacement training set in the recorded temporal evaluation. The interpretation therefore depends on keeping the fitted model, predictor definitions, preprocessing rules and selected threshold fixed.

This approach examines performance under a change in annual sample, but it does not isolate the causes of any performance change. Differences may reflect population composition, survey implementation, coding, missingness or other year-specific characteristics.

---

<!-- PAGE BREAK -->

# 6. Results

## 6.1 Outcome prevalence and sample composition

| Measure | BRFSS 2023 | BRFSS 2025 |
|---|---:|---:|
| Source respondents | 433,323 | 356,158 |
| Respondents with known outcome | 428,738 | 352,145 |
| Positive outcomes | 36,311 | 31,687 |
| Unweighted prevalence | 8.47% | 9.00% |
| Recorded survey-weighted prevalence | 6.43% | 6.75% |

The unweighted outcome prevalence is higher in the 2025 analysed sample than in the 2023 sample. The recorded weighted prevalence is lower than the corresponding unweighted prevalence in both years.

These differences reinforce the need to distinguish sample-level descriptive statistics from estimates intended to represent the survey population.

## 6.2 Held-out and temporal performance

The following table summarises the recorded primary-model results.

| Metric | BRFSS 2023 test | BRFSS 2025 temporal sample | Interpretation |
|---|---:|---:|---|
| ROC-AUC | 0.80115 | 0.794859 | Similar ranking discrimination; modest reduction in 2025 |
| Average Precision | 0.244865 | 0.248775 | Slightly higher in 2025 |
| Brier score | 0.069689 | 0.073815 | Higher in 2025; modestly worse probabilistic error |
| Accuracy | 0.806954 | 0.796709 | Lower in 2025 |
| Precision | 0.233987 | 0.235772 | Very similar positive predictive value |
| Sensitivity | 0.562798 | 0.561808 | Very similar detection of positive cases at the selected threshold |
| Specificity | 0.829542 | 0.819936 | Lower in 2025 |
| F1 score | 0.330547 | 0.332152 | Very similar balance of precision and sensitivity |

### ROC-AUC

ROC-AUC is approximately 0.801 in the held-out 2023 test partition and 0.795 in the 2025 sample.

This indicates that the classifier maintains similar ranking discrimination across the two evaluations, with a modest decline in 2025. ROC-AUC does not establish good calibration or clinical utility, and the values should not be interpreted as the percentage of individuals correctly classified.

### Average Precision

Average Precision is approximately 0.245 in 2023 and 0.249 in 2025.

Because the outcome is imbalanced, precision-recall evaluation provides useful information about positive-case detection. The results indicate similar performance across the two samples. Average Precision is prevalence-dependent, however, so comparisons should account for the change in outcome prevalence.

### Brier score

The Brier score increases from approximately 0.0697 to 0.0738.

Since lower Brier scores are generally preferable, the increase indicates worse overall probabilistic error in the 2025 sample under this measure. The Brier score reflects both calibration and discrimination; it does not, by itself, identify the cause of the change.

A dedicated calibration analysis would be required to assess calibration-in-the-large, calibration slope and any systematic probability miscalibration in greater detail.

### Threshold-dependent performance

Sensitivity is approximately 0.563 in 2023 and 0.562 in 2025. Specificity is approximately 0.830 and 0.820, respectively. Precision is approximately 0.234 and 0.236, and F1 is approximately 0.331 and 0.332.

The results are consistent with a similar threshold-dependent operating point across the two annual samples. Nonetheless, the precision values indicate that most positive classifications at this threshold are not true positives under the analysed outcome definition. This is important when considering any hypothetical screening application.

The classifier must not be presented as a standalone diagnostic tool.

## 6.3 Interpretation of accuracy

Accuracy is approximately 80.7% in 2023 and 79.7% in 2025. These figures should not be interpreted in isolation.

With outcome prevalence below 10%, a classifier that predicts the negative class for every respondent would already achieve accuracy close to 91.5% in 2023 and 91.0% in 2025, although it would have zero sensitivity for the positive class.

Consequently, the current model's lower overall accuracy does not automatically imply that it has no value for research. It does mean that accuracy alone cannot justify the model. The balance between sensitivity, precision, false-positive burden and the intended use case must be examined.

## 6.4 Survey-weighted point estimates

The project records the following survey-weighted point estimates.

| Weighted measure | BRFSS 2023 | BRFSS 2025 |
|---|---:|---:|
| Outcome prevalence | 0.06430 | 0.06750 |
| ROC-AUC | 0.81541 | 0.82281 |
| Average Precision | 0.21195 | 0.23176 |
| Brier score | 0.05464 | 0.05637 |

The weighted ROC-AUC estimates are higher than the corresponding unweighted ROC-AUC values in both years. The weighted Average Precision estimates are lower than the unweighted values, and the weighted Brier score is higher in 2025 than in 2023.

These results illustrate that the weighting approach can change the summary of model performance. They should be reported as point estimates only unless the underlying workflow also supplies valid design-based uncertainty estimates.

The current record does not establish confidence intervals or formal statistical comparisons for these weighted measures. The results therefore do not establish statistically significant improvement or deterioration between years.

## 6.5 Feature importance

The recorded feature-importance ordering is:

1. Age group
2. High blood pressure status
3. Diabetes status
4. Smoking status
5. Physical activity
6. Body mass index

This ordering describes the relative importance estimates produced by the fitted model and its chosen importance method.

It should not be interpreted as a causal ranking. Nor does a lower importance score mean that a variable is unimportant for clinical care or for other populations, outcome definitions or model specifications.

Feature importance can be affected by correlations between predictors, coding choices, the model family and the particular importance measure used. Further interpretation would benefit from complementary analyses such as permutation importance, partial dependence or suitable SHAP analyses, with attention to correlated predictors and the limits of associational interpretation.

## 6.6 Results summary

The primary model demonstrates moderate discrimination and broadly similar threshold-dependent results across the recorded 2023 and 2025 evaluations. The temporal results are useful evidence that performance did not collapse in the later annual sample.

However, the analysis does not establish equivalence across years, clinical effectiveness, future-event prediction, causal relationships or transportability beyond the BRFSS survey context.

---

<!-- PAGE BREAK -->

# 7. Risk of Bias, Reporting Quality and Reproducibility

## 7.1 PROBAST+AI appraisal

The project includes a provisional PROBAST+AI desk appraisal of six accessible comparator studies and the current project. One additional study, Kung et al. (2026), was left unrated because the available material was insufficient for a defensible full assessment.

The appraisal was conducted by a single reviewer. It should therefore be treated as a structured identification of potential risks, not as a completed independent formal assessment.

The framework is relevant because prediction-model performance can be misleading when there are weaknesses in participant selection, predictor measurement, outcome definition or analysis.

For the current study, the principal appraisal questions concern:

- Whether the analysed cohort and exclusions are documented.
- Whether the target represents the intended outcome.
- Whether predictors are available independently of the outcome definition.
- Whether preprocessing and model selection protect validation and test partitions.
- Whether performance metrics suit an imbalanced binary outcome.
- Whether the separate annual evaluation is described accurately.
- Whether the conclusions are proportionate to the evidence.

## 7.2 TRIPOD+AI reporting audit

The project includes a 52-item TRIPOD+AI reporting audit.

The purpose is to identify whether essential information about the dataset, participants, outcome, predictors, missing data, model development, evaluation and interpretation is available in the project record.

The audit is a reporting aid. Completing an audit does not guarantee methodological validity, eliminate risk of bias or establish clinical readiness.

For the next phase, the report, notebook and project documentation should remain consistent in their statements about the target, predictors, split design, threshold, metrics and limitations.

## 7.3 Leakage controls

The study uses a restricted predictor set and excludes the MI/CHD history fields used to construct or inspect the target.

This is an important design safeguard, but it does not by itself prove that every form of leakage has been eliminated. The pipeline should continue to be reviewed for:

- Target-derived predictors.
- Features that may encode information arising after the outcome.
- Preprocessing fitted using validation or test observations.
- Feature selection performed using held-out data.
- Oversampling or synthetic-data generation before partitioning.
- Threshold selection based on the test or temporal sample.
- Inconsistent transformations between 2023 and 2025.

Any new experiment should preserve a strict separation between development decisions and held-out evaluation.

## 7.4 Calibration and threshold selection

The classification threshold was selected to maximise F1 on the validation partition. That is a valid way to define an operating point for the chosen metric, provided the held-out test data remain separate.

It is not evidence that the threshold is optimal for every possible use. Different use cases may require prioritising sensitivity, specificity, positive predictive value, net benefit or a defined resource constraint.

Phase 03 should document the threshold-selection procedure and assess whether probability calibration is adequate for the intended research interpretation.

## 7.5 Reproducibility requirements

A reproducible workflow should record:

- The exact source file and its checksum.
- The target construction and missing-outcome handling.
- Predictor definitions and transformations.
- Partition assignments and random seed.
- Model family and hyperparameters.
- Cross-validation configuration.
- Threshold-selection procedure.
- Metric implementations and positive-class convention.
- Weighting procedures.
- Software environment and package versions.
- Outputs produced by each experiment.

The existing provenance files and research log provide a foundation for this process. The outstanding dataset-version discrepancy must be resolved or clearly bounded before the results are treated as fully reproducible against the official annual source files.

---

<!-- PAGE BREAK -->

# 8. Data Provenance and Unresolved Source-Version Discrepancy

## 8.1 Recorded discrepancy

The project provenance record identifies a discrepancy between the recorded local data files and the variable counts listed in official CDC annual documentation.

| Dataset year | Variables reported in official annual documentation | Columns recorded in local file |
|---|---:|---:|
| BRFSS 2023 | 345 | 350 |
| BRFSS 2025 | 284 | 283 |

The local file column counts and official documentation counts do not match.

The recorded SHA-256 fingerprints in `artifacts/provenance/dataset_provenance.json` are important for identifying the exact local files used in the experiment. However, a checksum establishes file identity, not that the file is the intended official release or that its schema matches a particular documentation page.

The cause of the discrepancy has not been established in the current research record.

## 8.2 Why the discrepancy matters

Possible explanations may include differences in file versions, formats, documentation conventions, included or excluded variables, preprocessing or a mismatch between the file and the documentation used for comparison.

These are possibilities, not verified explanations. The project should not choose one without supporting evidence.

The discrepancy affects reproducibility because another researcher attempting to reconstruct the analysis from the official annual source might not obtain the same column count or exact schema.

It does not, by itself, prove that the model metrics are wrong. Equally, it must not be dismissed merely because the notebook runs successfully.

## 8.3 Required resolution procedure

The following procedure is recommended before making any change to the locked experimental dataset.

1. Preserve the existing source files and recorded checksums.
2. Record the exact file names, download locations, access dates and release identifiers, where available.
3. Compare local column names and order against the matching official annual documentation.
4. Inspect duplicate names, unexpected fields, absent fields, derived variables and any transformations applied after download.
5. Determine whether the local files are original source files or processed copies.
6. Document the verified explanation, if one can be established.
7. If a corrected source is required, create a separate, explicitly versioned data artefact rather than silently overwriting the existing file.
8. Re-run affected analyses only under a documented change-control decision, preserving the original results for comparison.
9. Update the provenance record, research log, README and experiment outputs to reflect the outcome.

If the discrepancy cannot be resolved, the report should state that the experiment used the exact fingerprinted local files and that equivalence with the expected official schema has not been confirmed.

## 8.4 Research integrity decision

The locked experiment must not be silently altered to remove the discrepancy. Any future correction should be traceable and should make clear which results correspond to which data version.

This is a research-control issue, not merely a file-format issue.

---

<!-- PAGE BREAK -->

# 9. Limitations

## 9.1 Cross-sectional outcome

The outcome represents prevalent self-reported history of myocardial infarction or coronary heart disease. The analysis does not establish when the condition occurred, predict future incidence or identify causal risk factors.

## 9.2 Self-reported information

BRFSS relies on self-reported information for the relevant measures. Recall, reporting and measurement errors may affect the outcome and predictors.

The model's outputs reflect patterns in the recorded survey data, not independently verified clinical diagnoses.

## 9.3 Restricted predictor set

The six-predictor design provides a compact model but excludes many potentially relevant demographic, behavioural, clinical and socioeconomic characteristics.

The feature set should be understood as a deliberate modelling choice, not as a comprehensive representation of cardiovascular health.

## 9.4 Class imbalance

The positive class represents less than 10% of the analysed observations in both years. Accuracy can therefore be misleading when considered alone.

Precision, Average Precision, sensitivity, specificity, F1 and calibration-related measures provide complementary information, but none removes the need to define the intended use of the model.

## 9.5 Threshold dependence

Sensitivity, specificity, precision, accuracy and F1 depend on the chosen threshold. The threshold was selected to maximise validation F1 and was not established through a clinical decision analysis.

The observed precision values suggest a substantial false-positive burden among positive classifications. Any proposed operational use would require a clear evaluation of that burden.

## 9.6 Temporal rather than longitudinal validation

The 2025 sample consists of a separate annual survey population. It is not follow-up of the 2023 respondents.

Differences in results may reflect changes in sample composition, measurement, missingness, coding or population prevalence. The present analysis cannot attribute performance changes to a single cause.

## 9.7 Survey-design uncertainty

Survey-weighted point estimates are recorded, but full design-based uncertainty estimates are not established in the current summary.

Without appropriate variance estimation and confidence intervals, the analysis should not make formal claims about statistically significant differences between annual samples or precise population-level performance.

## 9.8 Review completeness

The literature review was targeted and narrative/scoping in nature. It lacked a complete search-export archive, exhaustive record counts and dual independent screening.

The findings support research positioning but do not establish exhaustive coverage of the literature.

## 9.9 Appraisal limitations

The PROBAST+AI desk appraisal was conducted by a single reviewer, and not all studies could be fully assessed. The TRIPOD+AI audit is a reporting assessment rather than a validation result.

Neither should be presented as independent certification of the current model.

## 9.10 Dataset provenance

The unresolved column-count discrepancy between local files and official documentation is a significant reproducibility limitation. It must remain visible until investigated and resolved.

## 9.11 No clinical validation

The study does not include prospective evaluation, a clinical deployment study, decision-curve analysis establishing net benefit, or validation in a clinical cohort.

The model is a research classifier and should not be presented as a clinically approved decision-support tool.

---

<!-- PAGE BREAK -->

# 10. Ethical and Responsible Interpretation

## 10.1 Appropriate use

The model is suitable for methodological investigation of a survey-based classification problem. It may help evaluate the behaviour of a compact classifier under a separate annual sample.

The present results do not support individual diagnosis, treatment recommendations, clinical triage or claims about future cardiovascular events.

## 10.2 Population representation

BRFSS sampling and weighting procedures are relevant to how estimates should be interpreted. The project should avoid assuming that unweighted sample performance directly represents all US adults.

Any future population-level statement should explain the role of weights and the limitations of the uncertainty estimation.

## 10.3 Potential for misinterpretation

A classifier with an ROC-AUC near 0.80 may appear strong if only that metric is highlighted. However, the recorded precision is around 0.24 at the selected threshold.

In a hypothetical application that labels people as positive, this means that positive classifications would include many respondents who do not meet the analysed outcome definition. The practical consequences would depend on the intended setting and the costs of false positives and false negatives.

The report should present performance as a set of complementary results rather than selecting only the most favourable metric.

## 10.4 Explainability

Feature importance can support exploratory interpretation, but it does not establish causality or justify changing a person's behaviour or treatment.

Explanations should be framed as descriptions of the fitted model's statistical behaviour and should be checked for stability and sensitivity to correlated features.

## 10.5 Data stewardship

The source-version discrepancy demonstrates the importance of preserving exact dataset fingerprints and maintaining an auditable record of changes.

Data correction, model reruns and changes to the target or predictor set should be explicitly logged, versioned and justified.

---

<!-- PAGE BREAK -->

# 11. Phase 03 Research Handover

## 11.1 Purpose of Phase 03

Phase 03 should move from literature positioning and methodological review to a controlled verification and robustness programme.

The priority is not to add models indiscriminately. It is to establish that the existing results are traceable, evaluate whether they remain robust under defensible analytical choices, and strengthen the evidence needed for a research-quality report or publication.

## 11.2 Priority 1 — Resolve provenance

**Required actions**

- Reconcile the local 2023 and 2025 schemas with the matching official CDC documentation.
- Verify file identity and source-version information.
- Preserve the original checksums and files.
- Record the explanation for any column-count differences, if established.
- Decide whether the locked experiment can be retained as-is or whether a separately versioned re-analysis is required.

**Completion criterion:** The provenance issue is either resolved with evidence or explicitly documented as unresolved, with a defensible statement of what the existing experiment used.

## 11.3 Priority 2 — Revalidate the locked pipeline

**Required actions**

- Confirm the outcome construction.
- Confirm the six predictors and their transformations.
- Verify that the test partition did not influence model selection or threshold choice.
- Verify that the 2025 sample did not influence development decisions.
- Confirm the positive-class convention for all metrics.
- Reproduce the recorded performance metrics from the locked artefacts.

**Completion criterion:** The recorded results can be reproduced from a versioned and documented pipeline, or any discrepancy is recorded and explained.

## 11.4 Priority 3 — Strengthen performance reporting

**Required actions**

- Report confidence intervals where a defensible method is available.
- Evaluate calibration more explicitly, including calibration plots and appropriate summary measures.
- Compare threshold-dependent performance at the locked threshold with other clearly labelled operating points.
- Report confusion matrices and class-specific error counts.
- Compare against simple baseline classifiers.
- Document the implications of class imbalance.
- Avoid changing the locked threshold based on the test or temporal sample.

**Completion criterion:** Performance is reported as a transparent collection of complementary metrics rather than a single headline score.

## 11.5 Priority 4 — Improve survey-aware evaluation

**Required actions**

- Document exactly how `_LLCPWT`, `_STSTR` and `_PSU` are used in weighted analyses.
- Distinguish unweighted sample metrics from weighted point estimates.
- Investigate an appropriate design-based variance-estimation strategy for relevant metrics.
- Report uncertainty only when the calculation method is defensible.
- Avoid treating weighted point estimates alone as evidence of statistically significant differences.

**Completion criterion:** The project can explain which metrics are weighted, how they are calculated and which uncertainty claims are or are not supported.

## 11.6 Priority 5 — Conduct focused robustness analyses

Potential analyses include:

- Sensitivity to alternative threshold-selection objectives.
- Missingness-pattern analysis.
- Subgroup performance analysis where sample sizes permit responsible interpretation.
- Stability of feature importance.
- Sensitivity to reasonable predictor-coding decisions.
- Comparison of the locked model against the secondary Logistic Regression model.
- Calibration assessment and, if justified, a separately documented calibration experiment.

Each analysis should be pre-specified in the research log where practical. Exploratory results should be labelled as such, and repeated experimentation should not be presented as independent confirmation.

## 11.7 Priority 6 — Strengthen reporting and reproducibility

**Required actions**

- Complete the outstanding TRIPOD+AI reporting items.
- Review the provisional PROBAST+AI appraisal without presenting it as independent certification.
- Maintain the literature matrix, screening log and reference database.
- Ensure the README, research log, status file and final report use consistent definitions.
- Record the environment and package versions.
- Preserve a clear link between every reported number and the artefact or notebook that produced it.

**Completion criterion:** An independent reader can understand the target, reproduce the principal workflow, identify the exact data files and distinguish verified results from unresolved issues.

## 11.8 Suggested Phase 03 exit criteria

Phase 03 should not be considered complete until:

1. Data provenance has been reconciled or the remaining uncertainty is explicitly bounded.
2. The locked 2023 and 2025 metrics have been reproduced or differences documented.
3. Threshold selection and held-out evaluation remain separated.
4. Calibration, uncertainty and survey-weighting limitations are adequately reported.
5. The research contribution is stated without unsupported novelty claims.
6. The project's documentation and experiment artefacts are internally consistent.
7. A decision has been recorded about whether a revised experiment is warranted.

---

<!-- PAGE BREAK -->

# 12. Conclusion

Phase 02 established the literature context and research position for a BRFSS-based machine-learning study of prevalent self-reported myocardial infarction or coronary heart disease history.

The reviewed evidence demonstrates that BRFSS-based cardiovascular classification is already represented in the literature. The current study should therefore avoid broad claims of novelty based only on the dataset, outcome or use of Gradient Boosting.

The project uses a restricted six-predictor model, develops it on BRFSS 2023 and evaluates it on a separate BRFSS 2025 annual sample. The recorded ROC-AUC values are approximately 0.801 and 0.795, while threshold-dependent sensitivity and F1 remain similar across the two evaluations. The Brier score is higher in the 2025 sample, and precision remains approximately 0.24 at the selected threshold.

These results support a cautious statement of broadly similar recorded classification performance across the two annual samples. They do not establish clinical readiness, prediction of future events, causal effects or generalisation beyond the survey context.

The project's most defensible contribution is its combination of a locked predictor specification, explicit threshold-selection procedure, separate annual evaluation, complementary performance reporting and transparent discussion of methodological limitations.

The unresolved difference between the local dataset column counts and official CDC documentation is a priority for the next phase. It must be investigated through documented provenance checks rather than corrected silently.

**Phase 02 is complete for the defined targeted narrative/scoping scope.** Phase 03 should prioritise provenance reconciliation, reproduction of the locked results, stronger calibration and uncertainty reporting, and focused robustness analyses before any broader claims are made.

---

<!-- PAGE BREAK -->

# References

*The references below reflect the bibliographic details recorded in the Phase 02 project context. Where a full title or complete source-level detail is not available in the current report record, it should be verified against the project's `literature/references.bib` and the publisher record before manuscript submission.*

1. Noh et al. (2026). BRFSS-based machine-learning research on prevalent myocardial infarction and coronary heart disease. *BMC Public Health*. DOI: [10.1186/s12889-026-27570-3](https://doi.org/10.1186/s12889-026-27570-3).

2. Chavda, S., & Hyun, J. (2024). BRFSS-based heart-disease machine-learning research. *Journal of Emerging Investigators*. DOI: [10.59720/24-006](https://doi.org/10.59720/24-006).

3. Imani et al. (2026). BRFSS-based heart-disease modelling. *American Heart Journal Plus*, 63, 100719. DOI: [10.1016/j.ahjo.2026.100719](https://doi.org/10.1016/j.ahjo.2026.100719).

4. Wu et al. (2026). BRFSS-based modelling with validation involving NHANES. *Computer Methods and Programs in Biomedicine*, 275, 109186. DOI: [10.1016/j.cmpb.2025.109186](https://doi.org/10.1016/j.cmpb.2025.109186).

5. Deng, Lu, & Hu. (2025). Heart-disease prediction using BRFSS and additional datasets. *PLOS ONE*, 20(9), e0330377. DOI: [10.1371/journal.pone.0330377](https://doi.org/10.1371/journal.pone.0330377).

6. Wanyonyi et al. (2025). BRFSS-derived heart-disease machine-learning research. *PLOS ONE*, 20(12), e0328338. DOI: [10.1371/journal.pone.0328338](https://doi.org/10.1371/journal.pone.0328338).

7. Kung et al. (2026). Annual BRFSS temporal-validation research involving cross-sectional diabetes classification. *International Journal of Medical Sciences*, 23(11), 3323–3335. DOI: [10.7150/ijms.137605](https://doi.org/10.7150/ijms.137605).

8. Oh et al. (2026). Research on survey-aware machine learning. *Proceedings of Machine Learning Research*, 333, 198–220. Available at: https://proceedings.mlr.press/v333/oh26a.html.

9. Collins, G. S., et al. (2024). TRIPOD+AI reporting guidance for clinical prediction models using regression or machine-learning methods. *BMJ*, 385, e078378. DOI: [10.1136/bmj-2023-078378](https://doi.org/10.1136/bmj-2023-078378).

10. Moons, K. G. M., et al. (2025). PROBAST+AI guidance for assessing risk of bias and applicability in prediction-model studies using regression or artificial intelligence methods. *BMJ*, 388, e082505. DOI: [10.1136/bmj-2024-082505](https://doi.org/10.1136/bmj-2024-082505).

11. Steyerberg, E. W., Vickers, A. J., Cook, N. R., et al. (2010). Assessing the performance of prediction models: A framework for traditional and novel measures. *Epidemiology*, 21(1), 128–138. DOI: [10.1097/EDE.0b013e3181c30fb2](https://doi.org/10.1097/EDE.0b013e3181c30fb2).

12. Van Calster, B., et al. (2019). Calibration in predictive analytics. *BMC Medicine*, 17, 230. DOI: [10.1186/s12916-019-1466-7](https://doi.org/10.1186/s12916-019-1466-7).

13. Centers for Disease Control and Prevention. (2023). *Behavioral Risk Factor Surveillance System: Annual Survey Data*. https://www.cdc.gov/brfss/annual_data/annual_2023.html.

14. Centers for Disease Control and Prevention. (2025). *Behavioral Risk Factor Surveillance System: Annual Survey Data*. https://www.cdc.gov/brfss/annual_data/annual_2025.html.

15. Cai et al. (2024). Systematic review relevant to machine learning and cardiovascular prediction. *BMC Medicine*, 22, 56. DOI: [10.1186/s12916-024-03273-7](https://doi.org/10.1186/s12916-024-03273-7).

16. Liu et al. (2025). Systematic review relevant to machine learning and cardiovascular prediction using electronic health records. *European Heart Journal – Digital Health*, 6(1), 7–22. DOI: [10.1093/ehjdh/ztae080](https://doi.org/10.1093/ehjdh/ztae080).

---

# Appendix A. Performance Metric Interpretation

| Metric | What it describes | Key limitation |
|---|---|---|
| ROC-AUC | Ranking discrimination across thresholds | Does not establish calibration or clinical utility |
| Average Precision | Precision-recall performance for the positive class | Depends on outcome prevalence and metric implementation |
| Brier score | Mean squared error of predicted probabilities | Combines aspects of calibration and discrimination |
| Accuracy | Fraction of classifications that are correct | Can be misleading with imbalanced outcomes |
| Precision | Fraction of positive predictions that are true positives | Sensitive to prevalence and threshold |
| Sensitivity | Fraction of actual positives detected | Does not quantify false positives by itself |
| Specificity | Fraction of actual negatives correctly identified | Does not quantify positive predictive value by itself |
| F1 score | Harmonic mean of precision and sensitivity | Ignores true negatives and depends on the threshold |

# Appendix B. Key Reproducibility Facts

| Item | Recorded specification |
|---|---|
| Development dataset | BRFSS 2023 |
| Temporal evaluation dataset | BRFSS 2025 |
| Outcome | Prevalent self-reported MI or CHD history |
| Predictor count | Six |
| Primary classifier | Gradient Boosting |
| Secondary classifier | L2 Logistic Regression |
| Training split | 70% |
| Validation split | 15% |
| Test split | 15% |
| Random seed | 42 |
| Cross-validation | Three-fold stratified CV on training data |
| Threshold-selection criterion | Maximum validation F1 |
| Recorded selected threshold | 0.1529128096 |
| Survey-design variables used as predictors | None |
| Dataset provenance discrepancy | Unresolved column-count mismatch for both annual files |

# Appendix C. Project Artefacts to Preserve

The following existing project paths should remain part of the research record:

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
- `research_log.md`
- `CHANGELOG.md`
- `artifacts/provenance/dataset_provenance.json`
- `notebooks/03_brfss_2023_first_look_optimised.ipynb`
- `reports/PHASE2_FINAL_REPORT.pdf`

The existing `literature/screening_log_template.csv` is intended to remain as a blank template alongside the populated screening log.

---

**End of Phase 02 Final Report**