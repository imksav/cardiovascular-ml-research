# 3. Results

## 3.1. Dataset integrity and analytical samples

The CDC reported 433,323 records in the 2023 BRFSS, 457,670 in 2024 and 356,158 in 2025 [1–3]. The corresponding local source files contained the same respondent counts.

A dataset provenance audit identified differences between the variable counts reported on the CDC annual data pages and those observed in the local SAS Transport files. The CDC pages report 345, 345 and 284 variables for 2023, 2024 and 2025, respectively, whereas the local files contained 350, 301 and 283 variables. These differences remain unresolved and are retained as a data-provenance limitation.

The local 2024 file did not contain `BPHIGH6`, one of the six predictors in the locked model. Consequently, 2024 was retained for compatibility assessment and was not used for model evaluation. All six predictors were available in the local 2023 and 2025 files.

The target-consistency audit independently reapplied the CDC definition of `_MICHD` using `CVDINFR4` and `CVDCRHD4`. Across 1,247,151 records from the three survey years, 13,804 outcomes were expected to be missing and no discrepancies were identified between the locally stored target and the documented derivation rule [4–6]. This result confirms consistency with the CDC calculation rule, rather than the clinical accuracy of respondents' self-reported histories.

After excluding records with an unknown `_MICHD` outcome, the 2023 development dataset contained 428,738 observations, including 36,311 positive outcomes (8.47%). The 2025 temporal evaluation dataset contained 352,145 observations, including 31,687 positive outcomes (9.00%).

The 2023 development sample was divided into training, validation and held-out test subsets using a stratified 70:15:15 split. The resulting sample sizes were 300,116, 64,311 and 64,311, respectively.

## 3.2. Primary model performance

The locked Gradient Boosting model achieved a ROC-AUC of 0.8012 on the 2023 held-out test set and 0.7949 on the 2025 temporal evaluation set. The absolute difference in ROC-AUC was −0.0063.

Average Precision was 0.2449 in 2023 and 0.2488 in 2025. The Brier score increased from 0.0697 to 0.0738. Sensitivity was similar across the two evaluation samples (0.5628 and 0.5618), as was the F1 score (0.3305 and 0.3322).

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

The results indicate similar observed discrimination and fixed-threshold classification performance across the two evaluation samples. The small difference in ROC-AUC should be interpreted descriptively because confidence intervals and formal statistical comparisons between the estimates were not calculated.

## 3.3. Probability calibration

Calibration summaries were broadly similar between the internal held-out evaluation and the temporal evaluation.

| Calibration measure | BRFSS 2023 held-out | BRFSS 2025 temporal |
|---|---:|---:|
| Observed prevalence | 0.0847 | 0.0900 |
| Mean predicted probability | 0.0851 | 0.0879 |
| Observed-to-expected ratio | 0.9951 | 1.0240 |
| Calibration intercept | 0.0509 | 0.0365 |
| Calibration slope | 1.0303 | 1.0040 |
| Brier skill score | 0.1009 | 0.0986 |

The observed-to-expected ratio was close to one in both samples. In 2025, the mean predicted probability was slightly lower than the observed prevalence. Calibration slopes were close to one in both evaluations. The Brier skill score decreased slightly from 0.1009 to 0.0986.

These summaries suggest modest differences in calibration across the evaluated years. They do not establish calibration equivalence or clinical suitability.

## 3.4. Survey-weighted sensitivity analyses

Survey-weighted point estimates were calculated as a sensitivity analysis using the BRFSS final survey weights. Weighted prevalence was lower than the corresponding unweighted prevalence in both evaluation samples.

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

The weighted estimates showed higher ROC-AUC and specificity than the corresponding unweighted estimates, alongside lower sensitivity. These results are reported as point estimates only. Confidence intervals and full design-based variance estimation incorporating the BRFSS strata and primary sampling units were not performed.

## 3.5. Predictor missingness and missingness-related performance

Among the six predictors, BMI had the highest proportion of missing observations in both primary survey years. Missingness in the other predictors was comparatively lower.

| Predictor | BRFSS 2023 missing (%) | BRFSS 2025 missing (%) |
|---|---:|---:|
| Age group (`_AGEG5YR`) | 1.7182 | 1.8345 |
| Physical activity (`EXERANY2`) | 0.2224 | 0.2567 |
| Smoking status (`_SMOKER3`) | 5.3754 | 5.7454 |
| Blood pressure (`BPHIGH6`) | 0.3685 | 1.1433 |
| Diabetes status (`DIABETE4`) | 0.1570 | 0.1656 |
| BMI (`_BMI5`) | 9.1959 | 9.0644 |

A record-level missingness assessment identified at least one missing predictor in 8,200 of the 64,311 observations in the 2023 held-out test set (12.75%) and 47,595 of the 352,145 observations in the 2025 temporal evaluation set (13.52%).

| Evaluation year | Predictor completeness | Records | Outcome prevalence | ROC-AUC |
|---|---|---:|---:|---:|
| 2023 | At least one missing predictor | 8,200 | 0.0698 | 0.7833 |
| 2023 | Complete predictors | 56,111 | 0.0869 | 0.8027 |
| 2025 | At least one missing predictor | 47,595 | 0.0745 | 0.7863 |
| 2025 | Complete predictors | 304,550 | 0.0924 | 0.7953 |

Discrimination was lower among observations with at least one missing predictor in both evaluation samples. Outcome prevalence also differed between the complete and incomplete groups. These findings indicate that missingness is relevant to the interpretation of model performance and should not be treated solely as a preprocessing issue.

## 3.6. Subgroup performance

Model performance varied across age groups. The most notable finding concerned respondents aged 18–39 years. At the locked classification threshold, observed sensitivity was zero in both the 2023 and 2025 evaluations. The proportion of positive predictions was extremely low in this age group.

| Age group | Metric | BRFSS 2023 | BRFSS 2025 |
|---|---|---:|---:|
| 18–39 years | ROC-AUC | 0.7123 | 0.7170 |
| 18–39 years | Sensitivity | 0.0000 | 0.0000 |
| 18–39 years | Positive predictions | 0.04% | 0.027% |
| 65–74 years | Sensitivity | 0.5424 | 0.5420 |
| 65–74 years | Specificity | 0.7209 | 0.7140 |
| 75 years and older | ROC-AUC | 0.6475 | 0.6397 |
| 75 years and older | Sensitivity | 0.8005 | 0.7799 |
| 75 years and older | Specificity | 0.4034 | 0.4069 |

Among respondents with diabetes in the 2025 evaluation, sensitivity was 0.8296 and specificity was 0.3831. This indicates that the model identified a high proportion of positive outcomes in this subgroup while also producing a substantial proportion of false-positive classifications.

These subgroup estimates demonstrate that aggregate performance does not represent uniform classification behaviour across population groups. They should be interpreted as descriptive subgroup findings rather than a formal fairness assessment.

## 3.7. Summary of findings

The primary Gradient Boosting model showed similar aggregate discrimination and fixed-threshold performance in the 2023 held-out and 2025 temporal evaluation samples. Calibration summaries were also broadly similar, although the 2025 Brier score was higher and mean predicted probability was slightly below observed prevalence.

Survey-weighted point estimates differed from unweighted estimates, particularly for sensitivity and specificity. Missing-predictor observations had lower observed discrimination than complete observations. Subgroup analysis identified important limitations in younger respondents and lower specificity among older respondents.

The unresolved differences between CDC-reported and local variable counts remain a data-provenance issue requiring reconciliation before submission.