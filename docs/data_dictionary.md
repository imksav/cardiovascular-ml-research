# BRFSS Analytical Data Dictionary

**Study:** Cardiovascular Machine Learning Research: BRFSS-Based Classification of Prevalent Self-Reported Myocardial Infarction and Coronary Heart Disease with Temporal Validation

**Source:** U.S. Centers for Disease Control and Prevention (CDC), Behavioral Risk Factor Surveillance System (BRFSS), annual public-use survey data, **2023 and 2025**. BRFSS 2024 was inspected for compatibility but was not used in the frozen temporal evaluation.

**Unit of analysis:** One survey respondent record per row. Questionnaire numeric codes represent categories unless explicitly described as continuous measurements. Original BRFSS source variables are preserved; analytical recodes are separate.

## Locked Outcome

| Field | Interpretation | Analytical handling |
|---|---|---|
| `_MICHD` | Calculated indicator of reported myocardial infarction and/or coronary heart disease | `1` → positive (`TARGET=1`); `2` → negative (`TARGET=0`); other/unknown values excluded from supervised evaluation |
| `CVDINFR4` | Respondent-reported myocardial infarction | Used only to audit construction of `_MICHD`; **never a predictor** |
| `CVDCRHD4` | Respondent-reported coronary heart disease | Used only to audit construction of `_MICHD`; **never a predictor** |

The target measures a **history reported at the survey interview**, not future cardiovascular risk or clinical confirmation.

## Six Locked Predictors

| Model feature | Source field | Type | Coding / preprocessing |
|---|---|---|---|
| `AGE_GROUP` | `_AGEG5YR` | Categorical | Valid categories `1–13`; `14` treated as missing; one-hot encoded |
| `PHYSICAL_ACTIVITY` | `EXERANY2` | Categorical | `1` yes, `2` no; `7/9` missing; one-hot encoded |
| `SMOKING_STATUS` | `_SMOKER3` | Categorical | `1` current every day, `2` current some days, `3` former, `4` never; `9` missing; one-hot encoded |
| `BLOOD_PRESSURE` | `BPHIGH6` | Categorical | `1` high blood pressure, `2` pregnancy only, `3` no high blood pressure, `4` borderline/pre-hypertension; `7/9` missing; one-hot encoded |
| `DIABETES_STATUS` | `DIABETE4` | Categorical | `1` diabetes, `2` pregnancy only, `3` no diabetes, `4` prediabetes; `7/9` missing; one-hot encoded |
| `BMI` | `_BMI5` | Continuous (kg/m²) | Divide stored value by `100`; missing values imputed using **training-only median** and standardised within fitted preprocessing |

Missing categorical values are represented using an explicit `-1` category in the fitted one-hot preprocessing. Preprocessing is fitted using the 2023 training data and reused unchanged for validation, held-out testing and 2025 temporal evaluation.

## Survey Design and Identification (Not Predictors)

| Field | Analytical role |
|---|---|
| `_LLCPWT` | Final BRFSS sample weight; evaluation-weighted point estimates |
| `_STSTR` | Stratification variable; retained as design metadata |
| `_PSU` | Primary sampling unit; retained as design metadata |
| `_STATE` | Reporting area; metadata, not a locked predictor |
| `SEQNO` | Source sequence value; provenance only and **not guaranteed globally unique** across areas |
| `ROW_INDEX` / DataFrame index | Unique technical row identity used for split integrity in the notebook |

Full complex-survey variance estimation is distinct from applying sample weights to performance metrics. The latter alone does not provide valid complex-survey confidence intervals.

## Audited but Not Included in the Locked Six-Predictor Model

`SEXVAR`, `GENHLTH`, `TOLDHI3`, `SMOKE100`, `SMOKDAY2` and several additional demographic/behavioural variables were explored during data-quality and candidate-feature assessment. They were **not** substituted into the final primary model. In particular, `SMOKE100` must not be confused with the selected `_SMOKER3` smoking-status measure.

## Population and Data Handling

- **BRFSS 2023:** 433,323 raw respondent records; 428,738 with known binary `_MICHD` outcome.
- **BRFSS 2025:** 356,158 raw records; 352,145 with known outcome in the temporal analytical sample.
- **BMI exploratory 2023 audit:** 392,788 valid values, unweighted mean approximately 28.48 kg/m². These are raw sample summaries, not population estimates.
- BRFSS nonresponse and special questionnaire codes are interpreted before modelling; records are **not** discarded solely because a predictor is missing.
- The final 2023 supervised population is stratified into training, validation and held-out testing; survey design variables remain separate from predictive features.

**Source of truth:** the executed notebook and its saved provenance files. Refer to the relevant annual CDC BRFSS codebooks when interpreting response codes. Do not apply these 2023/2025 harmonisation rules to unrelated years without reassessing survey-year compatibility.
