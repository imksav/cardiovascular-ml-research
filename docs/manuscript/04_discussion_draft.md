# 4. Discussion

## 4.1. Principal findings

This study evaluated a six-predictor Gradient Boosting model for classifying prevalent self-reported myocardial infarction or coronary heart disease using BRFSS data. A model developed using the 2023 survey sample was evaluated on an internal held-out test set and subsequently applied unchanged to the 2025 survey sample.

The principal finding was that aggregate discrimination remained similar across the two evaluation samples. ROC-AUC decreased from 0.8012 in the 2023 held-out evaluation to 0.7949 in the 2025 temporal evaluation. Average Precision increased slightly, from 0.2449 to 0.2488, while sensitivity and F1 remained similar. These results provide evidence of relatively stable observed classification performance across the two evaluated survey years.

However, this stability should not be interpreted as evidence of clinical validity or prospective cardiovascular risk prediction. The outcome represents prevalent self-reported disease history, and the predictors and outcome were collected within cross-sectional survey interviews. The model therefore classifies existing reported disease status rather than estimating the probability of a future cardiovascular event.

## 4.2. Interpretation in relation to previous BRFSS studies

The findings should be considered alongside the recent BRFSS-based study by Noh et al. [7]. That study directly examined prevalent self-reported MI or CHD using BRFSS 2023 and compared several machine-learning algorithms. Gradient Boosting achieved a ROC-AUC of 0.867 in the inclusive model and 0.858 after the removal of selected post-diagnosis proxy variables.

The present study differs substantially in predictor specification and evaluation design. It uses six predictors rather than a high-dimensional predictor set and evaluates the frozen model in a later survey year. Consequently, the reported performance estimates should not be treated as a direct algorithmic comparison with Noh et al. The difference in ROC-AUC may reflect differences in predictors, sample definitions, preprocessing, model configuration and evaluation procedures.

The study by Kung et al. [8] provides a further methodological comparator. It used BRFSS 2023 for model development and applied models without refitting to BRFSS 2024 for temporal validation of prevalent diagnosed diabetes. Although the outcome and predictor specifications differ, that work demonstrates that consecutive-year temporal validation using BRFSS is not, by itself, a novel methodological contribution.

The contribution of the present study is therefore more narrowly defined: a compact six-predictor specification for prevalent self-reported MI/CHD, evaluated through a frozen-model 2023-to-2025 design, with additional reporting of calibration, survey-weighted point estimates, missingness and subgroup performance.

## 4.3. Temporal performance and calibration

The relatively small reduction in ROC-AUC between 2023 and 2025 suggests that the model retained similar observed ranking ability in the later survey sample. Sensitivity and F1 were also similar at the locked threshold. Nevertheless, the Brier score increased from 0.0697 to 0.0738, indicating a modest deterioration in overall probabilistic accuracy.

The 2025 observed-to-expected ratio of 1.024 suggests that average predicted probabilities were slightly lower than the observed outcome prevalence. The calibration slope remained close to one, decreasing from 1.0303 in 2023 to 1.0040 in 2025. These summaries are consistent with broadly similar calibration, but they do not establish equivalence between the two samples.

The unchanged application of the model is an important feature of the evaluation. The 2025 data were not used to refit the model, modify the preprocessing pipeline, select a new threshold or recalibrate predicted probabilities. This preserves the distinction between model development and temporal evaluation. However, the results do not demonstrate transportability to other data sources, healthcare settings or populations outside the evaluated BRFSS samples.

## 4.4. Survey-weighted estimates

The survey-weighted sensitivity analysis produced different point estimates from the unweighted evaluation. Weighted prevalence was approximately 6.43% in 2023 and 6.75% in 2025, compared with unweighted prevalences of 8.47% and 9.00%.

Weighted ROC-AUC was higher than the corresponding unweighted estimate in both years. Weighted sensitivity was lower, while weighted specificity was higher. This illustrates that the interpretation of classification performance can depend on the distributional weighting applied to the evaluation observations.

These estimates must be interpreted cautiously. The analysis used the final BRFSS weights to calculate weighted point estimates but did not establish full design-based confidence intervals or variance estimates incorporating the survey strata and primary sampling units. The results therefore do not constitute complete complex-survey inference. Future work should use an appropriate survey-aware statistical framework if population-level uncertainty estimates are required.

## 4.5. Missingness and model performance

BMI was the predictor with the greatest missingness in both primary evaluation years. More than one in eight evaluation observations had at least one missing predictor. Discrimination was lower in these observations than in those with complete predictor information.

The difference in performance between complete and incomplete observations may reflect differences in outcome prevalence, respondent characteristics, survey response behaviour or other unmeasured factors. The current analysis does not establish the mechanism generating missing data and should not be interpreted as demonstrating that missingness is random or non-informative.

The findings nevertheless show that missingness is relevant to the model's observed performance. Reporting only aggregate discrimination would conceal the lower AUC observed among records with at least one missing predictor. Future work should investigate missingness mechanisms and assess whether alternative missing-data strategies change performance, calibration or subgroup behaviour. Such work would constitute a separate research extension and should not be presented as part of the locked experiment.

## 4.6. Subgroup performance

Subgroup analysis identified substantial differences in classification behaviour across age groups. At the fixed threshold, the model had zero observed sensitivity among respondents aged 18–39 years in both evaluation samples. The proportion of positive predictions in this group was extremely small.

Among respondents aged 75 years and older, sensitivity was comparatively high, but specificity was approximately 0.40 in both years. This indicates that a substantial proportion of respondents without the target outcome were classified as positive in this age group. The diabetes subgroup in 2025 showed a similar sensitivity-specificity trade-off, with sensitivity of 0.8296 and specificity of 0.3831.

These results demonstrate why aggregate performance metrics are insufficient to describe model behaviour. A model can achieve an overall ROC-AUC close to 0.80 while performing poorly at a selected threshold in particular subgroups. The observed subgroup differences should be reported transparently and should not be interpreted as evidence of fairness, clinical suitability or consistent performance across demographic groups.

The subgroup analyses are descriptive. Formal fairness assessment would require a prespecified framework, appropriate uncertainty estimates and a more comprehensive assessment of subgroup definitions and sample sizes.

## 4.7. Data provenance and outcome integrity

The provenance audit confirmed that the locally stored `_MICHD` values agreed with the documented CDC derivation rule across 1,247,151 records, with no mismatches. This provides evidence that the local outcome variable was calculated consistently with the documented rule using `CVDINFR4` and `CVDCRHD4`.

However, the audit also identified unresolved differences between the variable counts stated on the CDC annual data pages and those observed in the local XPT files. Although the respondent counts agreed and the required predictors were available in the local 2023 and 2025 files, the variable-count differences raise a source-version question that should be resolved before the manuscript is submitted.

The 2024 local file also lacked `BPHIGH6`, preventing its use in the locked six-predictor model. It was therefore used only for compatibility assessment. No alternative blood-pressure variable was substituted to force compatibility.

The outcome-consistency audit verifies agreement with the CDC calculation rule; it does not verify the clinical truth of the original survey responses. The outcome remains self-reported and may be affected by recall, access to healthcare and prior diagnosis.

## 4.8. Strengths and limitations

Several features strengthen the analysis. The study uses large annual public-health survey samples, a documented six-predictor specification, an independent held-out evaluation sample and a later-year temporal evaluation. The primary model, preprocessing pipeline and classification threshold were frozen before temporal evaluation. The target variable was checked against its documented derivation rule, and performance was examined using discrimination, calibration, fixed-threshold metrics, survey-weighted point estimates, missingness and subgroup analyses.

The findings should nevertheless be interpreted in light of several limitations.

First, BRFSS is cross-sectional. The analysis cannot establish temporal ordering between predictors and the reported cardiovascular outcome and cannot predict incident MI or CHD. Second, the outcome and several predictors are self-reported and may be affected by recall or reporting error. Third, some predictors, including blood-pressure and diabetes status, may be associated with healthcare contact or disease recognition; their temporal relationship to the reported cardiovascular outcome cannot be established.

Fourth, the temporal evaluation uses a later BRFSS survey year rather than an independent clinical dataset. It therefore provides evidence about performance across the evaluated survey years, not external clinical validation. Fifth, survey-weighted results are point estimates without full complex-survey variance estimation or confidence intervals.

Sixth, performance differed across age and diabetes subgroups, including zero sensitivity in the youngest age group at the locked threshold and low specificity in the oldest age group. Seventh, predictor missingness was associated with lower observed discrimination. Finally, unresolved differences between CDC-reported and local variable counts require source-version reconciliation.

The classification threshold was selected by maximising F1 on the 2023 validation sample. This is a statistical optimisation criterion rather than a clinically established decision threshold. The results do not demonstrate clinical net benefit or justify using the model to guide screening, diagnosis or treatment.

## 4.9. Implications and future research

The results suggest that a compact set of routinely collected demographic, behavioural and health-status variables can support classification of prevalent self-reported MI/CHD with similar observed aggregate discrimination across the evaluated BRFSS years. However, the subgroup and missingness findings show that overall performance should not be considered sufficient evidence of model reliability.

Future research should first resolve the source-file version discrepancies and confirm the provenance of the local XPT files. Further work could examine the sensitivity of results to alternative missing-data strategies, assess survey-design uncertainty, and evaluate model behaviour in genuinely independent datasets. Any such work should be documented as a separate analysis and should not retrospectively alter the locked results reported here.

## 4.10. Conclusion

A six-predictor Gradient Boosting model developed using BRFSS 2023 demonstrated similar observed aggregate discrimination when applied unchanged to BRFSS 2025. Calibration summaries were broadly similar, although the Brier score was higher in the temporal evaluation. Survey-weighted point estimates, missingness analyses and subgroup assessments revealed important differences that are not captured by aggregate discrimination alone.

The findings support cautious temporal evaluation of a compact model for prevalent self-reported MI/CHD classification. They do not establish prospective cardiovascular risk prediction, clinical utility or external clinical validity. Source-version reconciliation and further survey-aware and independent validation work are required before stronger conclusions can be drawn.