# 1. Introduction

Cardiovascular disease remains an important cause of morbidity and mortality worldwide. Myocardial infarction (MI) and coronary heart disease (CHD) contribute substantially to the burden of cardiovascular illness and are important outcomes for population-health surveillance. Understanding the characteristics associated with existing cardiovascular disease can support epidemiological analysis and help describe patterns of disease burden across populations.

The Behavioral Risk Factor Surveillance System (BRFSS), conducted by the United States Centers for Disease Control and Prevention (CDC), provides annual survey data on health-related behaviours, chronic conditions and demographic characteristics among adults. Its large annual samples and broad range of variables make it a valuable source for population-level health research [1–3]. However, BRFSS is a cross-sectional surveillance system. Analyses using these data must distinguish classification of existing self-reported disease from prediction of future clinical events.

Machine-learning methods have increasingly been applied to population-health survey data to examine relationships between demographic, behavioural and health-related characteristics and chronic disease outcomes. Their use in cross-sectional data nevertheless raises important methodological questions. High discrimination may partly reflect variables associated with prior diagnosis, healthcare utilisation or consequences of established disease. Such models may classify individuals with recognised disease more effectively without necessarily identifying individuals who will develop disease in the future.

Recent work has directly examined machine-learning classification of prevalent MI and CHD using BRFSS 2023. Noh et al. compared several algorithms and investigated the effect of excluding selected post-diagnosis proxy variables. Their Gradient Boosting model achieved a ROC-AUC of 0.867 in the inclusive specification and 0.858 after removing selected post-diagnosis variables [7]. This study establishes a close comparator for BRFSS-based classification of prevalent MI/CHD and demonstrates the importance of considering the information represented by candidate predictors.

Temporal validation using consecutive BRFSS survey years has also been reported for other health outcomes. Kung et al. developed models for prevalent diagnosed diabetes using BRFSS 2023 and applied the models unchanged to BRFSS 2024 [8]. Although the outcome and predictor specification differ from the present study, this work demonstrates the relevance of evaluating whether a model retains performance when applied to a later annual survey sample.

The present study does not claim that BRFSS-based classification of prevalent MI/CHD or annual-sample temporal validation is novel in itself. Instead, it examines a specific six-predictor model and combines internal held-out evaluation with temporal application to a later survey year. The analysis also considers calibration, fixed-threshold classification metrics, survey-weighted point estimates, missingness-related performance and subgroup variation.

The primary objective was to evaluate a Gradient Boosting model developed using BRFSS 2023 for classifying prevalent self-reported MI or CHD and to assess its performance when applied unchanged to BRFSS 2025.

The specific objectives were:

1. To develop and evaluate a model using six prespecified demographic, behavioural and health-status predictors, excluding variables directly used to construct the `_MICHD` outcome.
2. To assess the model's performance on a held-out BRFSS 2023 test sample and a later BRFSS 2025 sample without refitting the model or changing the classification threshold.
3. To examine discrimination, calibration and fixed-threshold classification performance across the two evaluation samples.
4. To conduct survey-weighted sensitivity analyses and describe missingness-related and subgroup differences in model performance.

The study addresses classification of prevalent self-reported MI/CHD rather than prospective cardiovascular risk prediction. Its findings are intended to contribute evidence about temporal stability and limitations of a compact survey-based classification model, not to establish a clinically validated risk assessment tool.