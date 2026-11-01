# Temporal validation of a six-predictor machine-learning model for prevalent self-reported myocardial infarction or coronary heart disease using BRFSS 2023 and 2025

**Author:** Keshav Bhandari
**Affiliation:** [Confirm institutional affiliation before submission]

## Abstract

**Background:** Machine-learning models applied to cross-sectional health surveys may classify existing disease status but should not automatically be interpreted as predicting future clinical events. Their performance should be evaluated beyond a single random data split.

**Objective:** To evaluate a six-predictor Gradient Boosting model for classifying prevalent self-reported myocardial infarction (MI) or coronary heart disease (CHD), and to assess its performance when applied unchanged to a later BRFSS survey year.

**Methods:** BRFSS 2023 was used for model development and internal evaluation. BRFSS 2025 was used for temporal evaluation, with the model, preprocessing pipeline and classification threshold held unchanged. The outcome was the CDC-calculated `_MICHD` variable. Six predictors represented age group, physical activity, smoking status, blood-pressure status, diabetes status and body mass index. BRFSS 2024 was assessed for variable compatibility but was not used for model evaluation because the audited local file lacked one of the locked predictors. Performance was assessed using discrimination, calibration and fixed-threshold classification metrics. Survey-weighted point estimates, missingness and subgroup performance were also examined.

**Results:** The 2023 held-out test sample contained 64,311 observations, with an outcome prevalence of 8.47%. The 2025 temporal evaluation contained 352,145 observations, with a prevalence of 9.00%. ROC-AUC was 0.8012 in 2023 and 0.7949 in 2025. Average Precision was 0.2449 and 0.2488, respectively; Brier scores were 0.0697 and 0.0738. Sensitivity remained similar (0.5628 and 0.5618), as did F1 (0.3305 and 0.3322). Subgroup analysis identified zero observed sensitivity among respondents aged 18–39 years at the locked threshold in both evaluation samples. Records with at least one missing predictor also had lower observed discrimination than complete records.

**Conclusions:** The model demonstrated similar aggregate discrimination across the evaluated BRFSS years, but performance was not uniform across subgroups or missingness groups. The findings concern classification of prevalent self-reported disease and do not establish prospective cardiovascular risk prediction or clinical validity. Further source-version reconciliation, survey-aware uncertainty estimation and independent validation are required.

**Keywords:** cardiovascular disease; myocardial infarction; coronary heart disease; BRFSS; machine learning; Gradient Boosting; temporal validation.