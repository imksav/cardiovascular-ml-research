# Dataset Selection and Temporal Compatibility

**Study:** Cardiovascular Machine Learning Research: BRFSS-Based Classification of Prevalent Self-Reported Myocardial Infarction and Coronary Heart Disease with Temporal Validation

**Status:** Dataset selection and temporal compatibility review completed for the locked analysis.

## Final Dataset Roles

| Survey year | Role | Decision |
|---|---|---|
| **BRFSS 2023** | Model development, validation and internal held-out testing | **Selected** |
| **BRFSS 2024** | Candidate later-year evaluation and feature compatibility audit | **Not used** for the six-feature frozen model |
| **BRFSS 2025** | Independent later-year sample evaluated using the frozen 2023 pipeline | **Selected** |

The study uses CDC Behavioral Risk Factor Surveillance System (BRFSS) **cross-sectional public-use** annual samples. The outcome is prevalent self-reported myocardial infarction and/or coronary heart disease (`_MICHD`).

## Rationale for BRFSS

BRFSS supplies large survey-year samples, demographic/behavioural and health-status measures, a relevant calculated MI/CHD outcome, survey weights, and an opportunity to evaluate model behaviour across separately collected years. Its limitations include self-report, potential questionnaire changes, survey-design complexity and an inability to establish future disease incidence or causality.

## Why 2024 Was Not Used

The 2024 source was assessed against the **six predictor fields locked for the 2023 model**. The required `BPHIGH6` high-blood-pressure variable was not structurally available in the required compatible form. Rather than substitute a different predictor or revise the model after selection, the 2024 dataset was excluded from the primary temporal evaluation.

This is a **feature-compatibility decision**, not a claim that 2024 BRFSS data are unusable for every cardiovascular study.

## Why 2025 Was Selected

The 2025 file contained the required outcome and locked predictor structure. Compatible fields were harmonised using the same analytical definitions; the fitted 2023 preprocessing, model parameters and F1-selected threshold were retained **without refitting or tuning** on 2025.

| Sample | Respondent records | Known-outcome analytical records |
|---|---:|---:|
| BRFSS 2023 | 433,323 | 428,738 |
| BRFSS 2025 | 356,158 | 352,145 |

The comparison supports **cross-year temporal generalisation within BRFSS**. It does not track the same respondents and is not prospective clinical outcome prediction.

## Alternatives Considered During Planning

- **NHANES:** Rich examination and laboratory data, but a different design, smaller samples and more extensive questionnaire/measurement harmonisation requirements; not chosen for this locked BRFSS project.
- **UCI Heart Failure Clinical Records:** A much smaller dataset (299 records), with a mortality outcome that differs from BRFSS self-reported MI/CHD; not appropriate as a direct frozen-model temporal sample.

These were initial candidates, **not additional validation datasets** used in the completed experiment.

## Reproducibility

Obtain the original annual BRFSS XPT files from the CDC rather than redistributing them in GitHub. Expected local paths:

```text
data/raw/brfss/2023/LLCP2023.XPT
data/raw/brfss/2024/LLCP2024.XPT   # compatibility audit only
data/raw/brfss/2025/LLCP2025.XPT
```

The notebook and `artifacts/provenance/` contain further data-compatibility checks and recorded dataset fingerprints. Their results should be checked against the exact local files before a full rerun.
