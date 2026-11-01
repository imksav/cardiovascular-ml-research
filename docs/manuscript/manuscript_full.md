# Temporal evaluation of a six-predictor Gradient Boosting classifier for prevalent self-reported myocardial infarction or coronary heart disease using BRFSS 2023 and 2025

**Author:** Keshav Bhandari
**Affiliation:** To be confirmed
**Manuscript status:** Complete first working draft; scientific and reproducibility review required before submission.

# Abstract

**Background:** Machine-learning analyses of cross-sectional health surveys can classify existing self-reported disease status, but should not be interpreted as predicting future clinical events. Evaluation on a later survey-year sample provides evidence about temporal stability beyond a random split within one year.

**Objective:** To evaluate a six-predictor Gradient Boosting classifier for prevalent self-reported myocardial infarction (MI) or coronary heart disease (CHD), and to assess its performance when applied unchanged to a later BRFSS survey year.

**Methods:** This secondary analysis used the 2023, 2024 and 2025 Behavioral Risk Factor Surveillance System (BRFSS) annual files. BRFSS 2023 was used for model development and internal evaluation; BRFSS 2025 was used for temporal evaluation. BRFSS 2024 was assessed for variable compatibility but was not used for model evaluation because the locally audited file lacked one of the six locked predictors. The outcome was the CDC-calculated `_MICHD` variable. Predictors were age group, physical activity, smoking status, blood-pressure status, diabetes status and body mass index (BMI). The Gradient Boosting model, preprocessing pipeline and classification threshold were frozen before the 2025 evaluation. Discrimination, calibration and fixed-threshold metrics were examined alongside survey-weighted point estimates, missingness and subgroup performance.

**Results:** The 2023 held-out test set contained 64,311 observations (outcome prevalence 8.47%); the 2025 temporal evaluation contained 352,145 observations (prevalence 9.00%). ROC-AUC was 0.8012 in 2023 and 0.7949 in 2025. Average Precision was 0.2449 and 0.2488, respectively, while Brier scores were 0.0697 and 0.0738. Sensitivity was 0.5628 and 0.5618; F1 was 0.3305 and 0.3322. At the locked threshold, sensitivity was zero among respondents aged 18–39 years in both evaluation samples. Records with at least one missing predictor had lower observed discrimination than records with complete predictors.

**Conclusions:** The model showed similar aggregate discrimination across the evaluated BRFSS years, but performance varied by age group and predictor completeness. The findings concern classification of prevalent self-reported disease; they do not establish prospective cardiovascular risk prediction, clinical utility or clinical validity. Source-file count discrepancies and the absence of full design-based uncertainty estimates require further review.

**Keywords:** cardiovascular disease; myocardial infarction; coronary heart disease; BRFSS; machine learning; Gradient Boosting; temporal evaluation; calibration.

---

# 1. Introduction

Cardiovascular disease remains a major cause of morbidity and mortality worldwide. Myocardial infarction (MI) and coronary heart disease (CHD) are important components of the cardiovascular disease burden and are frequently examined in population-health surveillance. Understanding characteristics associated with existing disease can help describe population patterns and identify groups in which reported disease burden is concentrated.

The Behavioral Risk Factor Surveillance System (BRFSS), conducted by the United States Centers for Disease Control and Prevention (CDC), is an annual cross-sectional telephone survey that collects information on health-related behaviours, chronic conditions and demographic characteristics among adults. Its large annual samples and range of health indicators make it a valuable source for population-health research [1–3]. However, the cross-sectional design requires careful interpretation: a model trained on contemporaneous predictors and reported disease status classifies prevalent disease and cannot, without longitudinal outcome data, be interpreted as predicting future events.

Machine-learning methods have been applied to BRFSS data to classify prevalent cardiovascular conditions. Noh et al. analysed BRFSS 2023 to classify prevalent self-reported MI or CHD and explicitly examined the influence of post-diagnosis proxy variables [7]. Their Gradient Boosting model achieved a ROC-AUC of 0.867 in an inclusive specification and 0.858 after removing selected post-diagnosis variables. This work is a close comparator because it uses the same survey year and a closely aligned outcome. The reported performance values are not directly comparable with those in the present study because the predictor sets, analytical samples, preprocessing and model-development procedures differ.

Temporal evaluation across consecutive BRFSS years has also been used for other cross-sectional health outcomes. Kung et al. developed models for prevalent diagnosed diabetes using BRFSS 2023 and applied the models unchanged to BRFSS 2024 [8]. Although their outcome and predictor specification differ, the study illustrates the value of testing whether model performance is retained in a later annual survey sample. It also demonstrates that annual-sample temporal evaluation is not, by itself, a novel methodological contribution.

The present study therefore does not claim to be the first BRFSS-based classification of prevalent MI/CHD or the first use of annual BRFSS temporal evaluation. Its focus is a compact, prespecified six-predictor model and a frozen 2023-to-2025 evaluation design, accompanied by reporting of discrimination, calibration, survey-weighted point estimates, predictor missingness, permutation importance and subgroup behaviour.

The primary objective was to evaluate a Gradient Boosting classifier developed using BRFSS 2023 for classification of prevalent self-reported MI or CHD and to assess its performance when applied unchanged to BRFSS 2025.

The specific objectives were to:

1. develop and evaluate a model using six prespecified demographic, behavioural and health-status predictors, excluding the variables used directly to construct the `_MICHD` outcome;
2. compare model performance in a held-out BRFSS 2023 test sample and a later BRFSS 2025 sample without refitting the model or changing the classification threshold;
3. examine discrimination, calibration and fixed-threshold classification performance;
4. describe survey-weighted point estimates and performance differences associated with missing predictors and selected population subgroups.

The study concerns classification of prevalent self-reported MI/CHD. It does not estimate incident disease, predict future cardiovascular events, establish causal relationships or validate a clinical decision tool.

---

# 2. Methods

## 2.1. Study design and data sources

This study was a secondary analysis of public-use annual BRFSS data for 2023, 2024 and 2025. BRFSS is a repeated cross-sectional survey; the annual files represent separate survey samples and do not constitute longitudinal follow-up of the same respondents [1–3].

BRFSS 2023 was used for model development, validation and internal held-out evaluation. BRFSS 2025 was reserved for temporal evaluation. BRFSS 2024 was assessed for variable compatibility but was not used to evaluate the locked model because the locally audited file did not contain `BPHIGH6`, one of the six prespecified predictors.

The CDC annual data pages report 433,323 records for 2023, 457,670 for 2024 and 356,158 for 2025. The same pages report 345, 345 and 284 variables in the respective SAS Transport files [1–3]. A read-only audit of the local XPT files confirmed the respondent counts but observed 350, 301 and 283 columns, respectively. These variable-count differences remain unresolved and are treated as a source-provenance limitation. The analysis did not silently alter the local files or infer that matching respondent counts alone resolve the discrepancy.

## 2.2. Outcome definition

The outcome was the CDC-calculated BRFSS variable `_MICHD`, representing reported history of myocardial infarction or coronary heart disease. The CDC documentation defines `_MICHD = 1` when either `CVDINFR4 = 1` or `CVDCRHD4 = 1`; `_MICHD = 2` when both source variables equal 2; otherwise the outcome is missing [4–6].

Records with a missing `_MICHD` value were excluded from the binary-outcome modelling samples. The source variables `CVDINFR4` and `CVDCRHD4` were excluded from the predictor set because they are used to derive the outcome and would create direct target leakage if included as predictors.

A read-only audit independently reapplied the CDC derivation rule to the local 2023, 2024 and 2025 files. Across 1,247,151 records, 13,804 outcomes were expected to be missing and no mismatches were observed between the derived and stored `_MICHD` values. This check establishes consistency with the documented derivation rule; it does not establish the clinical accuracy of respondents’ self-reported histories.

## 2.3. Predictor selection

The locked primary model used six predictors selected from the BRFSS files:

| BRFSS variable | Analytical representation | Description |
|---|---|---|
| `_AGEG5YR` | `AGE_GROUP` | Age group |
| `EXERANY2` | `PHYSICAL_ACTIVITY` | Any leisure-time physical activity |
| `_SMOKER3` | `SMOKING_STATUS` | Smoking status |
| `BPHIGH6` | `BLOOD_PRESSURE` | Blood-pressure status |
| `DIABETE4` | `DIABETES_STATUS` | Diabetes status |
| `_BMI5` | `BMI` | Body mass index |

The five categorical predictors were age group, physical activity, smoking status, blood-pressure status and diabetes status. BMI was treated as a continuous predictor after conversion from the BRFSS stored representation by dividing `_BMI5` by 100.

The survey-design variables `_LLCPWT`, `_STSTR` and `_PSU` were not included in the predictive feature matrix. The final survey weight was retained for separately labelled weighted evaluation summaries.

## 2.4. Data preparation and preprocessing

The analysis used the local annual XPT files without manual modification of the raw source data. Records without a defined `_MICHD` outcome were excluded from the corresponding binary-outcome analysis.

Categorical missing responses were represented using a dedicated sentinel value (`-1`) before one-hot encoding. Predefined category domains were used for categorical encoding, with previously unseen categories handled by the fitted transformation pipeline. BMI values were converted to their conventional scale, median-imputed using the training data and standardised using training-derived scaling parameters.

Preprocessing was implemented as part of the model pipeline so that transformations were fitted within the development data and applied unchanged to validation, held-out and temporal evaluation data. The pipeline was not refitted on BRFSS 2025.

## 2.5. Model development and selection

The 2023 records with known outcomes comprised 428,738 observations, including 36,311 positive outcomes. These records were divided using a stratified 70:15:15 split into training (n = 300,116), validation (n = 64,311) and held-out test (n = 64,311) subsets. The random seed was 42.

Five candidate classifiers were compared: Gradient Boosting, Logistic Regression, Gaussian Naive Bayes, Random Forest and Decision Tree. Three-fold stratified cross-validation was conducted within the training subset. Candidate performance was examined on the training and validation data; the held-out test set was reserved for final internal evaluation.

The primary model was a Gradient Boosting classifier with 150 estimators, a learning rate of 0.10 and maximum tree depth of 3 (random state 42). L2-regularised Logistic Regression was retained as a comparative benchmark. The classification threshold was selected by maximising F1 on the 2023 validation subset and was locked at 0.152913. The held-out 2023 test data and the 2025 temporal data were not used to select or modify the threshold.

## 2.6. Temporal evaluation

The final 2023 preprocessing pipeline, Gradient Boosting model and classification threshold were applied unchanged to the 2025 records with known outcomes. No preprocessing refitting, model retraining, hyperparameter retuning, predictor substitution, probability recalibration or threshold re-optimisation was performed using the 2025 data.

BRFSS 2024 was not substituted into the temporal evaluation because `BPHIGH6` was absent from the locally audited file. No alternative blood-pressure variable was introduced to force compatibility with the locked six-predictor specification.

## 2.7. Model-performance measures

Discrimination was assessed using the area under the receiver operating characteristic curve (ROC-AUC) and Average Precision (AP). Overall probabilistic accuracy was assessed using the Brier score. At the locked classification threshold, accuracy, precision, sensitivity, specificity and F1 were calculated.

Calibration was summarised using observed prevalence, mean predicted probability, the observed-to-expected ratio, calibration intercept, calibration slope and Brier skill score. The same locked model and threshold were used for both evaluation years.

Results are reported as point estimates. Confidence intervals and formal statistical tests comparing the 2023 and 2025 performance estimates were not calculated; differences are therefore interpreted descriptively rather than as evidence of statistical equivalence.

## 2.8. Survey-weighted sensitivity analysis

The BRFSS final survey weight (`_LLCPWT`) was used to calculate survey-weighted point estimates for prevalence and selected performance measures. Survey weights were used for evaluation only and were not supplied to the predictive model as features.

The weighted analysis did not estimate full design-based variance using the BRFSS strata (`_STSTR`) and primary sampling units (`_PSU`). Consequently, the weighted results are descriptive point estimates and are not accompanied by design-based confidence intervals or inferential tests.

## 2.9. Missingness and subgroup assessment

Predictor-level missingness was profiled for the six locked predictors. Evaluation observations were also grouped according to whether they had complete predictor information or at least one missing predictor. Discrimination and fixed-threshold sensitivity were compared descriptively between these groups.

Subgroup performance was examined for selected age groups and for respondents with diabetes in the 2025 evaluation. The analyses focused on ROC-AUC, sensitivity, specificity and the proportion of positive predictions where available. These subgroup summaries were descriptive; no formal fairness framework, subgroup confidence intervals or hypothesis tests were applied.

## 2.10. Feature-importance analysis

Held-out permutation importance was used to describe model reliance on each predictor in the 2023 and 2025 evaluation samples. The reported values represent changes in model discrimination when predictor information was permuted, as recorded in the project results. Permutation importance is not a measure of causal effect, biological mechanism, direction of association or clinical importance.

## 2.11. Reproducibility and software

The locked notebook, model artefacts, result tables, figures and provenance records are maintained in the research repository. Python, pandas, NumPy and scikit-learn were used for data preparation and modelling. The exact software versions are recorded in the repository provenance files (`notebooks/artifacts/provenance/software_versions.txt` and `software_versions.json`) and should be transcribed into the final journal-formatted manuscript during the technical review. Raw BRFSS XPT files are not intended to be distributed through Git; they are obtained from the CDC annual-data pages.

## 2.12. Ethical considerations

The analysis uses public-use BRFSS survey data and does not involve new participant recruitment or direct participant contact. The institutional ethics approval or exemption determination applicable to this secondary analysis was not present in the project records available for manuscript preparation. The author must confirm the appropriate institutional determination and insert the exact wording and reference, if applicable, before submission. No claim of ethics approval or exemption is made in this draft.

---

# 3. Results

## 3.1. Dataset integrity and analytical samples

The CDC annual pages report 433,323 records for BRFSS 2023, 457,670 for 2024 and 356,158 for 2025. The local audited XPT files contained the same respondent counts. However, the official pages report 345, 345 and 284 variables, whereas the local files contained 350, 301 and 283 columns, respectively [1–3]. These differences remain unresolved.

| Survey year | CDC-reported respondents | Local XPT respondents | CDC-reported XPT variables | Local XPT columns | Required predictors present |
|---|---:|---:|---:|---:|---:|
| 2023 | 433,323 | 433,323 | 345 | 350 | 6 of 6 |
| 2024 | 457,670 | 457,670 | 345 | 301 | 5 of 6 |
| 2025 | 356,158 | 356,158 | 284 | 283 | 6 of 6 |

The 2024 local file did not contain `BPHIGH6`, one of the six locked predictors. It was therefore used for compatibility assessment only and was not used for model evaluation.

The target-consistency audit independently reapplied the CDC `_MICHD` derivation rule to all three local files [4–6]. Across 1,247,151 records, 13,804 outcomes were expected to be missing and no mismatches were found.

| Survey year | Records checked | Defined outcomes | Expected missing outcomes | Observed missing outcomes | Mismatches |
|---|---:|---:|---:|---:|---:|
| 2023 | 433,323 | 428,738 | 4,585 | 4,585 | 0 |
| 2024 | 457,670 | 452,464 | 5,206 | 5,206 | 0 |
| 2025 | 356,158 | 352,145 | 4,013 | 4,013 | 0 |
| **Total** | **1,247,151** | **1,233,347** | **13,804** | **13,804** | **0** |

The 2023 development sample contained 428,738 observations with a known outcome, including 36,311 positive outcomes (8.47%). The 2025 temporal sample contained 352,145 observations with a known outcome, including 31,687 positive outcomes (9.00%).

The 2023 development sample was divided into training (n = 300,116), validation (n = 64,311) and held-out test (n = 64,311) subsets.

## 3.2. Candidate-model comparison

The baseline comparison favoured Gradient Boosting and Logistic Regression on validation ROC-AUC. Random Forest and Decision Tree showed substantially higher training ROC-AUC but poorer validation performance.

| Candidate model | Training ROC-AUC | Validation ROC-AUC |
|---|---:|---:|
| Gradient Boosting | 0.8000 | 0.8017 |
| Logistic Regression | 0.7976 | 0.8011 |
| Gaussian Naive Bayes | 0.7794 | 0.7836 |
| Random Forest | 0.9596 | 0.6830 |
| Decision Tree | 0.9684 | 0.6023 |

The final Gradient Boosting model only marginally outperformed the tuned Logistic Regression benchmark in the 2025 temporal sample (ROC-AUC 0.79486 versus 0.79389).

## 3.3. Primary model performance

The locked Gradient Boosting model achieved a ROC-AUC of 0.8012 on the 2023 held-out test set and 0.7949 on the 2025 temporal evaluation. The absolute difference was −0.0063.

Average Precision was 0.2449 in 2023 and 0.2488 in 2025. The Brier score increased from 0.0697 to 0.0738. Sensitivity was similar (0.5628 and 0.5618), as was F1 (0.3305 and 0.3322).

| Metric | BRFSS 2023 held-out | BRFSS 2025 temporal |
|---|---:|---:|
| Evaluation records | 64,311 | 352,145 |
| Outcome prevalence | 0.0847 | 0.0900 |
| ROC-AUC | 0.8012 | 0.7949 |
| Average Precision | 0.2449 | 0.2488 |
| Brier score | 0.0697 | 0.0738 |
| Accuracy | 0.8070 | 0.7967 |
| Precision | 0.2340 | 0.2358 |
| Sensitivity | 0.5628 | 0.5618 |
| Specificity | 0.8295 | 0.8199 |
| F1 score | 0.3305 | 0.3322 |

The results indicate similar observed aggregate discrimination across the two evaluation samples. Because confidence intervals and formal comparisons were not calculated, the small difference in ROC-AUC should be interpreted descriptively.

## 3.4. Calibration

Calibration summaries were broadly similar between the 2023 held-out and 2025 temporal evaluations.

| Calibration measure | BRFSS 2023 held-out | BRFSS 2025 temporal |
|---|---:|---:|
| Observed prevalence | 0.0847 | 0.0900 |
| Mean predicted probability | 0.0851 | 0.0879 |
| Observed-to-expected ratio | 0.9951 | 1.0240 |
| Calibration intercept | 0.0509 | 0.0365 |
| Calibration slope | 1.0303 | 1.0040 |
| Brier skill score | 0.1009 | 0.0986 |

The observed-to-expected ratio was close to one in both samples. In 2025, the mean predicted probability was slightly lower than the observed prevalence. Calibration slopes were close to one in both evaluations. These summaries do not establish calibration equivalence or clinical suitability.

![Figure 1. ROC curves for the 2023 held-out and 2025 temporal evaluations](../../notebooks/artifacts/figures/roc_internal_vs_temporal.png)

![Figure 2. Calibration comparison for the 2023 held-out and 2025 temporal evaluations](../../notebooks/artifacts/figures/calibration_internal_vs_temporal.png)

## 3.5. Survey-weighted sensitivity analysis

Survey-weighted point estimates differed from the unweighted results. Weighted prevalence was 6.43% in 2023 and 6.75% in 2025.

| Metric | BRFSS 2023 weighted | BRFSS 2025 weighted |
|---|---:|---:|
| Weighted prevalence | 0.0643 | 0.0675 |
| ROC-AUC | 0.8154 | 0.8228 |
| Average Precision | 0.2120 | 0.2318 |
| Brier score | 0.0546 | 0.0564 |
| Accuracy | 0.8559 | 0.8585 |
| Precision | 0.2153 | 0.2362 |
| Sensitivity | 0.4695 | 0.4907 |
| Specificity | 0.8824 | 0.8852 |
| F1 score | 0.2953 | 0.3189 |

Weighted ROC-AUC and specificity were higher than the corresponding unweighted estimates, while sensitivity was lower. These results are point estimates only; confidence intervals and full design-based variance estimation were not performed.

## 3.6. Predictor missingness

BMI had the highest missingness among the six predictors in both primary survey years. Missingness percentages were:

| Predictor | BRFSS 2023 missing (%) | BRFSS 2025 missing (%) |
|---|---:|---:|
| Age group (`_AGEG5YR`) | 1.7182 | 1.8345 |
| Physical activity (`EXERANY2`) | 0.2224 | 0.2567 |
| Smoking status (`_SMOKER3`) | 5.3754 | 5.7454 |
| Blood pressure (`BPHIGH6`) | 0.3685 | 1.1433 |
| Diabetes status (`DIABETE4`) | 0.1570 | 0.1656 |
| BMI (`_BMI5`) | 9.1959 | 9.0644 |

At least one predictor was missing in 8,200 of the 64,311 observations in the 2023 held-out set (12.75%) and 47,595 of the 352,145 observations in the 2025 temporal set (13.52%).

| Evaluation year | Predictor completeness | Records | Outcome prevalence | ROC-AUC | Sensitivity |
|---|---|---:|---:|---:|---:|
| 2023 | At least one missing predictor | 8,200 | 0.0698 | 0.7833 | 0.4406 |
| 2023 | Complete predictors | 56,111 | 0.0869 | 0.8027 | 0.5771 |
| 2025 | At least one missing predictor | 47,595 | 0.0745 | 0.7863 | 0.4659 |
| 2025 | Complete predictors | 304,550 | 0.0924 | 0.7953 | 0.5739 |

Discrimination and sensitivity were lower among observations with at least one missing predictor in both evaluation samples. Outcome prevalence also differed between the complete and incomplete groups.

## 3.7. Permutation importance

Age group had the highest reported permutation-importance score in both evaluation years, followed by blood-pressure status and diabetes status. The predictor ranking was unchanged between the 2023 and 2025 evaluations.

| Predictor | 2023 importance | 2025 importance |
|---|---:|---:|
| Age group | 0.12832 | 0.13120 |
| Blood-pressure status | 0.04004 | 0.03867 |
| Diabetes status | 0.01882 | 0.01790 |
| Smoking status | 0.01485 | 0.01496 |
| Physical activity | 0.00399 | 0.00381 |
| BMI | 0.00162 | 0.00156 |

![Figure 3. Cross-year permutation importance](../../notebooks/artifacts/figures/permutation_importance_cross_year.png)

These values describe model reliance under the reported permutation procedure. They do not establish causal effects, biological mechanisms or clinical importance.

## 3.8. Subgroup performance

Performance varied across age groups. Among respondents aged 18–39 years, observed sensitivity at the locked threshold was zero in both evaluation samples, and the positive-prediction rate was extremely low.

| Age group | Measure | BRFSS 2023 | BRFSS 2025 |
|---|---|---:|---:|
| 18–39 years | ROC-AUC | 0.7123 | 0.7170 |
| 18–39 years | Sensitivity | 0.0000 | 0.0000 |
| 18–39 years | Positive predictions | 0.04% | 0.027% |
| 65–74 years | Sensitivity | 0.5424 | 0.5420 |
| 65–74 years | Specificity | 0.7209 | 0.7140 |
| 75 years and older | ROC-AUC | 0.6475 | 0.6397 |
| 75 years and older | Sensitivity | 0.8005 | 0.7799 |
| 75 years and older | Specificity | 0.4034 | 0.4069 |

Among respondents with diabetes in the 2025 evaluation, sensitivity was 0.8296 and specificity was 0.3831. These findings show that aggregate metrics conceal important differences in fixed-threshold behaviour across subgroups.

## 3.9. Threshold robustness

The selected threshold was 0.152913. A local sensitivity analysis around the locked threshold (±20%) showed the expected trade-off: lowering the threshold increased sensitivity while reducing specificity; increasing it increased specificity while reducing sensitivity. F1 changed only modestly around the selected operating point. The threshold is an analytical decision rule selected by validation F1, not a clinically established diagnostic or treatment threshold.

## 3.10. Summary of results

The primary Gradient Boosting model showed similar observed aggregate discrimination and fixed-threshold sensitivity across the 2023 held-out and 2025 temporal evaluation samples. The Brier score was higher in 2025, while calibration summaries remained broadly similar. Survey-weighted point estimates differed from unweighted estimates. Missing-predictor observations had lower observed discrimination and sensitivity, and subgroup analysis identified zero sensitivity among younger respondents and low specificity among the oldest age group. The local XPT variable-count discrepancies remain unresolved.

---

# 4. Discussion

## 4.1. Principal findings

This study evaluated a six-predictor Gradient Boosting classifier for prevalent self-reported MI or CHD using BRFSS data. A model developed using the 2023 survey sample was evaluated on an internal held-out test set and then applied unchanged to the 2025 survey sample.

The principal finding was that aggregate discrimination was similar across the two evaluation samples: ROC-AUC decreased from 0.8012 in 2023 to 0.7949 in 2025, an absolute difference of −0.0063. Average Precision increased slightly, from 0.2449 to 0.2488. Sensitivity and F1 were also similar at the locked threshold. The Brier score increased from 0.0697 to 0.0738, indicating a modest deterioration in overall probabilistic accuracy.

These results provide descriptive evidence that the frozen model retained similar aggregate ranking performance across the two evaluated annual survey samples. They do not establish statistical equivalence, because confidence intervals and formal comparisons were not calculated.

## 4.2. Relationship to previous BRFSS research

Noh et al. provide the closest direct comparator because they classified prevalent self-reported MI/CHD using BRFSS 2023 [7]. Their Gradient Boosting model achieved ROC-AUC values of 0.867 in an inclusive predictor specification and 0.858 after selected post-diagnosis proxy variables were removed. Those estimates are higher than the estimates in the present study, but they should not be interpreted as a direct algorithmic comparison. The predictor sets, sample definitions, preprocessing, modelling choices and evaluation procedures differ. The present study uses a compact six-predictor specification and places particular emphasis on applying a frozen model to a later survey year.

Kung et al. used BRFSS 2023 for development and BRFSS 2024 for temporal evaluation of prevalent diagnosed diabetes [8]. Their study demonstrates that temporal validation across annual BRFSS samples is not a new concept. The contribution of the present work is therefore not the first use of BRFSS for MI/CHD classification or the first annual-sample temporal evaluation. It is the specific locked predictor specification and the combined reporting of later-year discrimination, calibration, weighted point estimates, missingness, permutation importance and subgroup performance.

## 4.3. Temporal performance and calibration

The small reduction in ROC-AUC suggests that the model retained similar observed ranking ability in the later survey sample. The near-unchanged sensitivity and F1 at the locked threshold are also notable. However, accuracy and specificity were lower in 2025, and the Brier score increased. The 2025 mean predicted probability was slightly below observed prevalence, while the observed-to-expected ratio was 1.024.

The model and preprocessing pipeline were not refitted on 2025 data, and the threshold was not recalibrated. This preserves the distinction between model development and temporal evaluation. Nevertheless, the 2025 sample comes from the same surveillance system and should not be described as independent clinical validation. The analysis provides evidence about performance across two BRFSS survey-year samples, not transportability to healthcare settings or other data sources.

The tuned Logistic Regression benchmark had a 2025 ROC-AUC of 0.79389 compared with 0.79486 for Gradient Boosting. The difference was very small. For this compact predictor set, the more flexible model therefore offered only marginal improvement in observed temporal discrimination over the regularised linear benchmark. This supports the importance of retaining simple comparators rather than assuming that greater algorithmic complexity will produce materially better performance.

## 4.4. Survey-weighted estimates

Survey-weighted point estimates differed from unweighted estimates. Weighted prevalence was lower than unweighted prevalence in both years, while weighted ROC-AUC and specificity were higher and sensitivity was lower. These differences illustrate that performance summaries depend partly on the population representation induced by survey weights.

The weighted analyses should be interpreted cautiously. Final survey weights were used for point estimates, but the analysis did not incorporate the complete BRFSS complex design into variance estimation. No design-based confidence intervals or formal inferential comparisons are reported. The results should not be described as complete population-level survey inference.

## 4.5. Missingness and performance

BMI had the highest predictor missingness in both primary survey years. More than one in eight evaluation observations had at least one missing predictor. In both evaluation samples, records with at least one missing predictor had lower ROC-AUC and sensitivity than records with complete predictor information.

These differences may reflect differences in respondent characteristics, outcome prevalence, survey response behaviour or other unmeasured factors. The current analysis does not establish the mechanism generating missing data and does not show that missingness is random or non-informative. The findings demonstrate that imputation alone does not remove all performance differences associated with incomplete predictor information.

Future work could examine alternative missing-data strategies and investigate whether missingness indicators or more detailed response-pattern analyses change model performance. Such analyses would be new research extensions and should not retrospectively alter the locked experiment.

## 4.6. Feature importance and subgroup behaviour

Permutation importance ranked age group highest in both evaluation years, followed by blood-pressure status and diabetes status. The ordering was unchanged across the two samples. These values indicate how much the fitted model relied on each predictor under the selected permutation procedure; they do not establish causal effects, direction of association or biological importance.

Subgroup analysis showed that the global threshold did not produce uniform classification behaviour. Among respondents aged 18–39 years, sensitivity was zero in both years and the proportion of positive predictions was extremely low. Among respondents aged 75 years and older, sensitivity was higher but specificity was approximately 0.40. The 2025 diabetes subgroup also showed a high-sensitivity/low-specificity pattern.

These findings are important because aggregate ROC-AUC does not describe the consequences of applying one classification threshold to all subgroups. They should be reported as descriptive subgroup limitations, not as a formal fairness assessment. A formal fairness analysis would require a prespecified framework, appropriate uncertainty estimates and careful consideration of subgroup sizes and definitions.

## 4.7. Data provenance and outcome integrity

The audit confirmed that local `_MICHD` values agreed with the CDC derivation rule across 1,247,151 records, with no mismatches. This provides evidence of consistency between the stored target and the documented rule based on `CVDINFR4` and `CVDCRHD4` [4–6]. It does not establish the clinical truth of the original self-reported responses.

The audit also identified unresolved differences between the variable counts stated on CDC annual pages and those observed in the local XPT files. The 2023 and 2024 official pages each report 345 variables, compared with 350 and 301 in the local files; the 2025 page reports 284, compared with 283 locally [1–3]. Although respondent counts agree, the variable-count differences require source-version reconciliation before submission. The 2024 local file also lacked `BPHIGH6`, preventing its use in the locked six-predictor evaluation.

## 4.8. Strengths

The study has several strengths. It uses large annual public-health survey samples and a documented six-predictor specification. It separates training, validation and held-out test data, uses cross-validation within the training subset, and locks the final model and threshold before held-out and temporal evaluation. The later-year evaluation did not involve refitting, retuning or recalibration. The study also reports discrimination, calibration, survey-weighted point estimates, predictor missingness, permutation importance and subgroup behaviour rather than relying on accuracy alone. A read-only provenance audit checked the stored outcome against the CDC derivation rule.

## 4.9. Limitations

The findings should be interpreted in light of several limitations.

First, BRFSS is cross-sectional. The model classifies prevalent self-reported MI/CHD and cannot establish temporal ordering between predictors and disease history or predict incident cardiovascular events. Second, the outcome and several predictors are self-reported and may be affected by recall or reporting error. Third, predictors such as blood-pressure and diabetes status may reflect prior diagnosis and healthcare contact; the cross-sectional data cannot establish whether these characteristics preceded the reported cardiovascular condition.

Fourth, the temporal evaluation uses a later annual BRFSS sample rather than an independent clinical dataset. It therefore does not establish external clinical validity. Fifth, survey-weighted results are point estimates without full design-based variance estimation. Sixth, no confidence intervals or formal statistical tests were calculated for the reported performance comparisons.

Seventh, performance varied across age and diabetes subgroups, including zero sensitivity among respondents aged 18–39 years at the locked threshold and low specificity among respondents aged 75 years and older. Eighth, observations with missing predictors had lower observed discrimination and sensitivity. Ninth, the unresolved CDC/local variable-count discrepancies require source-version reconciliation. Finally, the classification threshold was selected by maximising validation F1; it is not a clinically established operating threshold and no clinical net-benefit analysis was performed.

## 4.10. Implications and future research

The findings suggest that a compact set of demographic, behavioural and health-status variables can classify prevalent self-reported MI/CHD with similar aggregate discrimination across the evaluated BRFSS years. However, the missingness and subgroup findings show that aggregate performance is insufficient to describe model behaviour.

Before stronger conclusions are drawn, the local XPT files and CDC variable counts should be reconciled. Further work could estimate uncertainty using methods appropriate to the BRFSS complex survey design, investigate missing-data mechanisms, and evaluate the frozen model in a genuinely independent dataset. Such work should be recorded as a separate extension and should not alter the locked Phase 1 results.

## 4.11. Conclusion

A six-predictor Gradient Boosting classifier developed using BRFSS 2023 demonstrated similar observed aggregate discrimination when applied unchanged to BRFSS 2025. Calibration summaries were broadly similar, although the Brier score was higher in the temporal evaluation. Survey-weighted point estimates, missingness analyses and subgroup assessments revealed important differences not captured by aggregate discrimination alone.

The findings support cautious temporal evaluation of a compact model for prevalent self-reported MI/CHD classification. They do not establish prospective cardiovascular risk prediction, clinical utility or external clinical validity. Source-version reconciliation, survey-aware uncertainty estimation and independent validation are required before stronger conclusions can be drawn.

---

# 5. Author declarations

> **Author completion required.** The statements below are deliberately not invented. Confirm each item and replace bracketed text before journal submission.

## Author information

- **Author:** Keshav Bhandari
- **Affiliation:** [Insert the institution or independent-researcher affiliation that accurately applied during the work.]
- **Corresponding author:** [Insert email address.]
- **ORCID:** [Insert ORCID, if available.]

## Ethics approval

This study is a secondary analysis of public-use BRFSS data. The applicable institutional ethics approval, exemption or non-human-subjects determination has not been confirmed in the project records available for this draft.

**Required action:** Obtain and insert the exact determination from the relevant institution or ethics office. Do not state that approval was unnecessary unless that determination has been made by the appropriate authority.

## Consent to participate

[Confirm the appropriate statement for secondary analysis of public-use BRFSS data and the journal's requirements.]

## Consent for publication

[Confirm. The manuscript does not include identifiable individual-level data or images.]

## Funding

[Author to confirm whether any funding supported this research. Do not use “no funding” until confirmed.]

## Competing interests

[Author to declare any competing interests or confirm none.]

## Author contributions

[Author to confirm the CRediT contribution statement. Suggested roles to review: conceptualisation; methodology; software; validation; formal analysis; data curation; visualisation; writing—original draft; writing—review and editing.]

## Data availability

The BRFSS annual public-use datasets are available from the CDC annual-data pages cited in the manuscript. Raw XPT files are not intended to be distributed through the Git repository. The exact public repository commit or release containing the analysis code and derived artefacts should be added here after the manuscript package is committed and made publicly accessible.

## Code availability

The analysis repository is maintained at: https://github.com/imksav/cardiovascular-ml-research

**Required action:** Confirm the public repository state, identify the commit or release containing the manuscript and relevant analysis artefacts, and ensure that raw datasets and private/local files are excluded.

## Acknowledgements

[Insert acknowledgements, if applicable, or remove this section.]

## Generative AI / AI-assisted writing disclosure

The manuscript text was prepared with AI-assisted drafting and editing support. The author must review, verify and take responsibility for all content, and must adapt this disclosure to the target journal's current policy. Do not submit an AI-use statement that does not accurately describe the actual workflow.

---

# 6. References

1. Centers for Disease Control and Prevention. **2023 BRFSS Survey Data and Documentation.** Atlanta, GA: CDC. Available from: https://www.cdc.gov/brfss/annual_data/annual_2023.html

2. Centers for Disease Control and Prevention. **2024 BRFSS Survey Data and Documentation.** Atlanta, GA: CDC. Available from: https://www.cdc.gov/brfss/annual_data/annual_2024.html

3. Centers for Disease Control and Prevention. **2025 BRFSS Survey Data and Documentation.** Atlanta, GA: CDC. Available from: https://www.cdc.gov/brfss/annual_data/annual_2025.html

4. Centers for Disease Control and Prevention. **Calculated Variables in the 2023 Data File of the Behavioral Risk Factor Surveillance System.** Version 12; revised May 23, 2024. Atlanta, GA: CDC. Available from: https://www.cdc.gov/brfss/annual_data/2023/pdf/2023-calculated-variables-version4-508.pdf

5. Centers for Disease Control and Prevention. **Calculated Variables in the 2024 Data File of the Behavioral Risk Factor Surveillance System.** Version 26; revised August 7, 2025. Atlanta, GA: CDC. Available from: https://www.cdc.gov/brfss/annual_data/2024/pdf/2024-calculated-variables-version4-508.pdf

6. Centers for Disease Control and Prevention. **Calculated Variables in the 2025 Data File of the Behavioral Risk Factor Surveillance System.** Version 5; revised June 26, 2026. Atlanta, GA: CDC. Available from: https://www.cdc.gov/brfss/annual_data/2025/pdf/2025-calculated-variables-version4-508.pdf

7. Noh J, Kim Y, Lim C, Cho SY, Kwon Y, Lee ES, Kim WK, Kim YH, Kim K. Occupational and socioeconomic predictors of myocardial infarction and coronary heart disease: a machine learning analysis. **BMC Public Health.** 2026;26:2015. doi:10.1186/s12889-026-27570-3.

8. Kung WM, Yeh HC, Huang APH, Islam MM, Wu CC, Wang YC. Machine Learning with Social Determinants of Health for Cross-Sectional Diabetes Classification: Development and Temporal Validation. **International Journal of Medical Sciences.** 2026;23(11):3323–3335. doi:10.7150/ijms.137605.

9. Collins GS, Moons KGM, Dhiman P, Riley RD, Beam AL, Van Calster B, et al. TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods. **BMJ.** 2024;385:e078378. doi:10.1136/bmj-2023-078378.

10. Moons KGM, Damen JAA, Kaul T, Hooft L, Andaur Navarro C, Dhiman P, et al. PROBAST+AI: an updated quality, risk of bias, and applicability assessment tool for prediction models using regression or artificial intelligence methods. **BMJ.** 2025;388:e082505. doi:10.1136/bmj-2024-082505.