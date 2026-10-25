# Phase 2 Related-Work Synthesis

**Study title:** Cardiovascular Machine Learning Research: BRFSS-Based Classification of Prevalent Self-Reported Myocardial Infarction and Coronary Heart Disease with Temporal Validation
**Review snapshot:** 25 October 2026
**Review type:** Targeted critical narrative/scoping review. It is **not** a systematic review and does not claim exhaustive database coverage.

## 1. Scope and question

This review positions the completed study against evidence on (i) cross-sectional classification of prevalent self-reported myocardial infarction (MI) and/or coronary heart disease (CHD) using BRFSS, (ii) annual-sample temporal evaluation, (iii) cross-survey validation, and (iv) calibration, complex-survey analysis, and reporting quality. Studies that predict incident/future CVD, use clinical EHR follow-up, use imaging, or use small benchmark datasets are contextual evidence rather than direct comparators.

The distinction between **prevalent-status classification** and **future-risk prediction** is central. The BRFSS `_MICHD` construct records a respondent's self-reported history of MI or CHD. It does not establish when disease began relative to the predictors and is not a prospective event outcome.

## 2. Direct BRFSS MI/CHD classification evidence

### 2.1 Noh et al. (2026): closest comparator

Noh et al. analysed BRFSS 2023, the same survey year and broad outcome family used in the present study. Their target was prevalent self-reported MI or CHD, not future cardiovascular risk. They compared logistic regression, decision tree, random forest and gradient boosting and explicitly contrasted an inclusive predictor set with a second specification excluding a priori defined post-diagnosis proxies. The paper reports a stratified 70:30 split, five-fold cross-validation in the training data, a held-out evaluation, and calibration curves, Brier score, calibration intercept and slope. Gradient boosting ROC-AUC was reported as 0.867 in the inclusive specification and 0.858 after post-diagnosis proxies were excluded; corresponding PR-AUC values were 0.389 and 0.372. Weighted logistic regression was used as a sensitivity analysis on a complete-case subset, while the machine-learning models were not fitted using a full complex-survey design workflow [1].

This paper materially narrows the novelty claim. BRFSS 2023, `_MICHD`, machine-learning classification, leakage awareness, hold-out evaluation, calibration and a weighted regression sensitivity analysis are **not individually novel** in the current project. The studies are not head-to-head: Noh et al. used a broad candidate predictor set and different model-selection/threshold rules, while this project locks six predictors and evaluates a frozen pipeline on a separate later annual sample. The different AUCs must not be interpreted as evidence that one model is superior.

### 2.2 Chavda and Hyun (2024)

Chavda and Hyun used the 2022 BRFSS survey to classify self-reported CHD or MI history from demographic, behavioral and health-condition survey questions. Their source file contained 445,132 records; the reported preprocessed dataset contained 340,200 records and 32 features. A 10% holdout was reserved while the remaining data were used for stratified five-fold cross-validation. Logistic regression was selected; the reported global model had mean cross-validation accuracy 0.725 and MCC 0.305, and holdout accuracy 0.724 with MCC 0.307. Their demographic-specific models showed variation in performance, which supports the need to describe subgroup performance rather than report a single aggregate score [2].

The paper provides direct evidence that broad BRFSS survey questions can classify self-reported MI/CHD history. Its year, feature set, preprocessing, metric choices and validation design differ from the present six-predictor 2023-to-2025 study. The exact derived outcome code was not independently confirmed to be identical to the current `_MICHD` construction.

### 2.3 Imani et al. (2026)

Imani et al. report a 2022 BRFSS complete-case analysis of 221,643 participants, with 13 predictors and comparisons among XGBoost, random forest, logistic regression and Naive Bayes. Their abstract reports accuracy of 94.2%, F1 of 85.3% and ROC-AUC of 0.94, while the accessible article's Table 2 reports accuracy of 85.02% and F1 of 85.34%. The reported class counts (12,884 positives plus 209,039 negatives) sum to 221,923 rather than 221,643. These inconsistencies remain unresolved in this review snapshot; no disputed value is used as a dependable performance benchmark [3].

The study is still relevant as another recent BRFSS-based analysis of a self-reported MI/CHD-related outcome. Its complete-case selection, 13-feature specification, resampling/modeling choices and unresolved reporting inconsistencies make numerical comparisons inappropriate.

## 3. Related CHD models and cross-dataset validation

### 3.1 Wu et al. (2026)

Wu et al. report a BRFSS-trained CHD model using 12 clinical features, with a 70:30 internal split and external evaluation using NHANES. Their abstract reports LightGBM AUC of 0.825 internally and 0.851 externally [4]. This is useful evidence that cross-survey evaluation has been used in BRFSS-related CHD modeling. It is not the same validation design as applying an unchanged model to a later BRFSS annual sample, and the exact outcome coding and survey-weight handling could not be established from the accessible abstract. It should therefore be treated as related evidence, not a direct comparator.

### 3.2 Deng, Lu and Hu (2025)

Deng et al. describe an interpretable LightGBM model trained with BRFSS 2015 data and evaluated across the Framingham and Z-Alizadeh Sani datasets [5]. The multiple datasets have different populations and outcome construction. The paper is relevant to the broader practice of cross-dataset validation and feature interpretation, but its performance metrics should not be ranked against this study's annual BRFSS estimates.

### 3.3 Wanyonyi et al. (2025)

Wanyonyi et al. analyse a BRFSS-derived secondary dataset of 253,680 records and report a suite of hybrid/ensemble models, including a stacking ensemble with AUC around 0.94 [6]. Their methods describe SMOTE, expansion of the dataset to 459,574 records, a subsequent subsample of about 9,789, and later a 70/15/15 train/validation/test split. The narrative order places resampling before the split description, which raises a **possible** leakage concern if that order reflects the implementation. The code and supplementary implementation were not independently audited, so this must not be stated as a confirmed error. The derived dataset and preprocessing pipeline also differ substantially from direct use of the official 2023/2025 BRFSS files.

Taken together, these studies show that CHD classification using BRFSS-derived data and ML is an established topic. They also show why model results need to be compared by outcome definition, source version, participant selection, preprocessing, split order, thresholding, calibration and survey design—not by AUC alone.

## 4. Temporal validation and survey-aware analysis

Kung et al. (2026) report a BRFSS 2023 diabetes classifier that is applied to BRFSS 2024 without refitting, retuning or changing the decision threshold [7]. Although the outcome differs, the design demonstrates that frozen evaluation across successive annual BRFSS cross-sections is not a novel validation method by itself. The present contribution, if supported by a broader future search, is the specific application to the six-predictor prevalent MI/CHD classification problem and the combined reporting of its temporal performance, calibration and robustness analyses.

Temporal validation within BRFSS is not the same as longitudinal follow-up: the 2025 respondents are not a follow-up cohort of 2023 respondents. Nor is it independent external clinical validation. CDC documentation confirms that annual files can differ in included reporting areas and in file versions; the 2023 and 2025 public datasets also differ in geographic coverage [13, 14]. Consequently, cross-year performance differences may reflect sample composition, coverage, measurement, or prevalence changes as well as model transportability.

Oh et al. (2026) provide survey-aware ML guidance emphasizing sampling weights, strata and primary sampling units across the analytical lifecycle [8]. In this project, survey-weighted performance values are sensitivity-analysis point estimates only; full complex-design uncertainty intervals have not been established. This limitation must remain explicit. Weighted point estimates should not be described as fully design-based population inference.

## 5. Reporting, appraisal and performance interpretation

TRIPOD+AI is the current reporting guideline for prediction-model studies using regression or ML, with 27 main items and 52 subitems spanning study rationale, data, participants, outcomes, predictors, analysis, open science, participant involvement, results and discussion [9]. It is a reporting checklist, not a guarantee of low risk of bias.

PROBAST+AI is the updated tool for assessing model-development quality, risk of bias in model evaluation, and applicability. It separates development from evaluation and addresses participants/data, predictors, outcome and analysis domains [10]. The project audit created for Phase 2 is a **pre-manuscript self-audit**; it is not a formal independent review or a claim of compliance. A paper must report missing items transparently, including ethical/IRB status, funding/conflicts, registration status, data/code availability, and any patient/public involvement or absence thereof.

Steyerberg et al. describe a framework for assessing prediction-model performance beyond a single discrimination statistic, including calibration [11]. Van Calster et al. emphasize calibration as central to predictive analytics [12]. These sources support reporting ROC-AUC, Average Precision (AP), Brier score and calibration diagnostics together, particularly with an imbalanced outcome. Use **Average Precision (AP)** consistently in the manuscript for the metric exported by this project; do not rename it “PR-AUC” unless the exact implementation and terminology are checked.

Broader systematic reviews also warn that many cardiovascular ML models have methodological, reporting, calibration and independent-validation limitations. Cai et al. reviewed CVD AI models and found substantial risk-of-bias and validation concerns in the literature they searched through July 2021 [15]. A later systematic review/meta-analysis focused on EHR-based medium- to long-term CVD risk prediction likewise reports heterogeneity and limitations in external validation and calibration reporting [16]. These reviews provide methodological context, but their populations and prospective-risk questions differ from the present cross-sectional BRFSS classification task.

## 6. Defensible contribution statement

> This study evaluates a locked six-predictor model for classifying prevalent self-reported MI/CHD using BRFSS 2023, then applies the frozen preprocessing pipeline, fitted model and decision threshold unchanged to the independent BRFSS 2025 annual sample. It reports discrimination, probability calibration, fixed-threshold classification metrics, survey-weighted evaluation point estimates, and selected subgroup, missingness and threshold-robustness analyses.

This is a description of the study design, not a novelty claim. The current targeted search did not identify an exact equivalent combination, but it was not exhaustive and cannot support “first,” “unique,” or “state-of-the-art” claims. The final manuscript should say the study **extends the applied evidence** by documenting this specific design, subject to further searching if the intended journal requires a systematic literature review.

## 7. Final Phase 2 conclusion

The evidence supports proceeding to manuscript development, with a deliberately narrow framing:

1. Acknowledge Noh et al. as the closest direct comparator.
2. Acknowledge prior BRFSS 2022 self-reported CHD/MI classifiers.
3. State that temporal validation across annual BRFSS samples has precedent for other outcomes.
4. Distinguish later-year temporal evaluation from longitudinal or external clinical validation.
5. Report calibration and thresholded metrics alongside discrimination, and use AP terminology consistently.
6. Keep survey-weighted metrics labelled as point-estimate sensitivity analyses.
7. Avoid direct performance rankings across different datasets and outcome definitions.
8. Preserve the unresolved CDC source-version/column-count discrepancy as a reproducibility limitation to address before any reanalysis.

### Scope boundary

This phase is complete as a targeted critical narrative/scoping review. It is **not** a systematic review: institutional Scopus/Web of Science/Embase/IEEE exports, complete result counts, independent dual screening, and a PRISMA flow were not available or performed. No PRISMA diagram or exhaustive-coverage claim should be added. If the manuscript's claims later require systematic-review standards, conduct a separately protocolled database review rather than retrospectively relabeling this exploratory review.

## References

[1] Noh J, Kim Y, Lim C, et al. Occupational and socioeconomic predictors of myocardial infarction and coronary heart disease: a machine learning analysis. *BMC Public Health*. 2026;26:2015. https://doi.org/10.1186/s12889-026-27570-3

[2] Chavda A, Hyun J. Using broad health-related survey questions to predict the presence of coronary heart disease. *Journal of Emerging Investigators*. 2024;7. https://doi.org/10.59720/24-006

[3] Imani M, Maroosi A, Shojaei S, et al. Predicting cardiovascular diseases using imbalanced data: An XGBoost-based analysis of the 2022 BRFSS dataset. *American Heart Journal Plus*. 2026;63:100719. https://doi.org/10.1016/j.ahjo.2026.100719

[4] Wu B, Huang K, Hong X, et al. Building and validating a machine learning model to predict coronary heart disease risk based on non-invasive indicators. *Computer Methods and Programs in Biomedicine*. 2026;275:109186. https://doi.org/10.1016/j.cmpb.2025.109186

[5] Deng L, Lu K, Hu H. An interpretable LightGBM model for predicting coronary heart disease: Enhancing clinical decision-making with machine learning. *PLOS ONE*. 2025;20(9):e0330377. https://doi.org/10.1371/journal.pone.0330377

[6] Wanyonyi M, Morris ZN, Musyoka FM, Kitavi DM. Enhanced machine learning and hybrid ensemble approaches for Coronary Heart Disease prediction. *PLOS ONE*. 2025;20(12):e0328338. https://doi.org/10.1371/journal.pone.0328338

[7] Kung WM, Yeh HC, Huang APH, Islam MM, Wu CC, Wang YC. Machine Learning with Social Determinants of Health for Cross-Sectional Diabetes Classification: Development and Temporal Validation. *International Journal of Medical Sciences*. 2026;23(11):3323–3335. https://doi.org/10.7150/ijms.137605

[8] Oh Y, Zheng HW, Feng J, Bui AAT. Survey-Aware Machine Learning: A Guideline for Valid Population Health Inference based on Scoping Review. *Proceedings of Machine Learning Research*. 2026;333:198–220. https://proceedings.mlr.press/v333/oh26a.html

[9] Collins GS, Moons KGM, Dhiman P, et al. TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods. *BMJ*. 2024;385:e078378. https://doi.org/10.1136/bmj-2023-078378

[10] Moons KGM, Damen JA, Kaul T, et al. PROBAST+AI: an updated quality, risk of bias, and applicability assessment tool for prediction models using regression or artificial intelligence methods. *BMJ*. 2025;388:e082505. https://doi.org/10.1136/bmj-2024-082505

[11] Steyerberg EW, Vickers AJ, Cook NR, et al. Assessing the performance of prediction models: a framework for traditional and novel measures. *Epidemiology*. 2010;21(1):128–138. https://doi.org/10.1097/EDE.0b013e3181c30fb2

[12] Van Calster B, McLernon DJ, van Smeden M, Wynants L, Steyerberg EW. Calibration: the Achilles heel of predictive analytics. *BMC Medicine*. 2019;17:230. https://doi.org/10.1186/s12916-019-1466-7

[13] US Centers for Disease Control and Prevention. 2023 BRFSS Survey Data and Documentation. https://www.cdc.gov/brfss/annual_data/annual_2023.html

[14] US Centers for Disease Control and Prevention. 2025 BRFSS Survey Data and Documentation. https://www.cdc.gov/brfss/annual_data/annual_2025.html

[15] Cai Y, Cai YQ, Tang LY, et al. Artificial intelligence in the risk prediction models of cardiovascular disease and development of an independent validation screening tool: a systematic review. *BMC Medicine*. 2024;22:56. https://doi.org/10.1186/s12916-024-03273-7

[16] Liu T, Krentz A, Lu L, Curcin V. Machine learning based prediction models for cardiovascular disease risk using electronic health records data: systematic review and meta-analysis. *European Heart Journal – Digital Health*. 2025;6(1):7–22. https://doi.org/10.1093/ehjdh/ztae080
