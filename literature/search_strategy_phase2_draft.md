# Phase 2 literature-search strategy — draft (not a completed systematic review)

**Study:** Cardiovascular Machine Learning Research: BRFSS-Based Classification of Prevalent Self-Reported Myocardial Infarction and Coronary Heart Disease with Temporal Validation

**Prepared:** 2026-10-09  
**Status:** Prospective search plan and exploratory seed identification. Do **not** present this document as an executed PRISMA systematic review.

## Review objective

Critically position the completed BRFSS 2023-to-2025 prevalent MI/CHD classification analysis against comparable BRFSS classifiers, model-validation practices, calibration, survey-design considerations and robustness evidence.

## Questions guiding evidence collection

1. Which studies specifically classify **prevalent self-reported MI/CHD**, rather than forecast incident cardiovascular events?
2. Which use BRFSS and comparable predictors/outcome codes?
3. How do studies separate model development from held-out and temporally later evaluation?
4. Do they report threshold-selection strategy, discrimination, calibration, weights, missingness and subgroup stability?
5. What limitation or contribution remains after accounting for closely comparable published studies?

## Information sources

Primary: PubMed/MEDLINE, publisher full texts and PubMed Central, plus CDC annual codebooks. Search Scopus, Web of Science and IEEE Xplore **only if access is available** and document access/search dates. Google Scholar may support citation chaining, but record it separately from database searches.

## Draft search strings — revise for each database

**Q1, directly comparable BRFSS prevalence classification:**

```text
("Behavioral Risk Factor Surveillance System" OR BRFSS)
AND ("myocardial infarction" OR "coronary heart disease" OR "heart disease" OR _MICHD)
AND ("machine learning" OR "gradient boosting" OR "random forest" OR "logistic regression")
```

**Q2, validation and model reporting:**

```text
("cardiovascular" OR "coronary heart disease" OR "myocardial infarction")
AND ("machine learning" OR "prediction model" OR "classification")
AND ("temporal validation" OR "external validation" OR "calibration" OR "generalizability")
```

**Q3, survey design and robustness:**

```text
(BRFSS OR "population health survey")
AND ("survey weights" OR "complex survey" OR "subgroup" OR "missing data")
AND ("machine learning" OR "classification")
```

**Q4, reporting and quality guidance:** TRIPOD+AI; PROBAST+AI; calibration and model performance methodological reviews.

## Working eligibility rules (to finalise after pilot screening)

- Include peer-reviewed English-language empirical studies with a clear cardiovascular outcome, study population and model evaluation. Prioritise BRFSS and self-reported MI/CHD.
- Include systematic reviews and methodological/guideline papers as **separate evidence categories**, not as direct model-performance comparators.
- Do not combine prospective incident-event prediction, diagnostic imaging, troponin-based MI diagnosis and cross-sectional prevalent-disease classification in one undifferentiated performance ranking.
- Exclude sources where model validation or data provenance cannot be characterised; record exclusions with reasons.
- For non-English or inaccessible full texts, log the limitation transparently rather than silently excluding without disclosure.

## Data extraction

For each candidate: DOI, full bibliographic details, year, data source and survey year(s), outcome formulation, number/type of predictors, sampling and missingness, train/validation/test and cross-year setup, model and threshold choices, ROC-AUC/AP (note when PR-AUC definitions differ), calibration/Brier, survey weighting, subgroup analysis, and stated limitations.

## Search and selection audit trail

Record each **actual** run: date/time and timezone, database/interface, complete query, filters, returned count, exported citations, deduplication steps, title/abstract and full-text decisions. Record citation chasing separately. Add counts only after carrying out the action; do not invent counts or a PRISMA flow diagram.

### Preliminary source discovery on 2026-10-09

Exploratory open-web and publisher/PubMed searches identified nine preliminary seed references stored in `verified_seed_sources.csv`. This is **not an exhaustive or protocol-driven retrieval**. Some references have verified metadata/abstract only; see each record's `verification_status`. Source information must be checked against each full text before final extraction or numerical comparison.

## Key scientific cautions

- The model's target `_MICHD` concerns **prevalent self-reported MI and/or CHD**; do not label it as prospective CVD risk.
- AUC values across papers with different outcome definitions, predictor panels, splits or populations are not head-to-head algorithm comparisons.
- A 2026 BRFSS 2023 paper uses the same source year, source row count and outcome type; it is a **direct comparator that must be explicitly discussed**.
- External validation across NHANES and BRFSS and temporal validation across annual BRFSS cross-sections are related but distinct.
- The CDC's currently posted source file dimensions may differ from those observed in your original local XPT; preserve input-file fingerprints and document version discrepancies rather than silently rerunning the locked study.
