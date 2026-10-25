# Phase 2 literature-search strategy and audit trail

**Study:** Cardiovascular Machine Learning Research: BRFSS-Based Classification of Prevalent Self-Reported Myocardial Infarction and Coronary Heart Disease with Temporal Validation
**Updated:** 2026-10-25
**Status:** Exploratory open-web and publisher-source retrieval completed for this pass; screening is ongoing. This is **not** a systematic review and does not support a PRISMA flow diagram or exhaustive-coverage claim.

## Review objective

Critically position the locked BRFSS 2023-to-2025 analysis against (1) direct studies of prevalent self-reported MI/CHD using BRFSS, (2) related BRFSS classifiers and annual-sample temporal validation, (3) cross-survey external validation, (4) calibration and performance methodology, (5) survey-aware ML, and (6) reporting/risk-of-bias guidance.

## Questions guiding evidence collection

1. Which studies specifically classify **prevalent self-reported MI/CHD**, rather than forecast incident cardiovascular events?
2. Which use BRFSS and comparable outcome codes/predictors?
3. How do studies separate development from held-out and later-year evaluation?
4. Do they report threshold-selection strategy, discrimination, calibration, weights, missingness and subgroup stability?
5. What contribution remains after accounting for the closest comparator and temporal-validation analogues?

## Sources actually accessed in this pass

- Open-web search results leading to PubMed records and publisher pages.
- Full-text publisher pages: BMC Public Health, PLOS ONE, BMC Medicine and BMJ.
- PubMed/PMC records and full text for accessible papers.
- Proceedings of Machine Learning Research (PMLR) article page.
- Official CDC BRFSS 2023 and 2025 annual-data documentation.

**Not performed in this pass:** direct searches within subscribed Scopus, Web of Science, Embase or IEEE Xplore interfaces; exhaustive PubMed/MEDLINE query export; deduplication of a complete bibliographic export; dual-reviewer screening. The search interface did not expose total result counts for the queries below, so no total retrieval counts are claimed. The screening log records source-level decisions and access limits.

## Executed search log

Search session: **2026-10-25, approximately 21:00–21:15 UTC**. Search IDs are local labels used to connect queries to `screening_log.csv`.

| Search ID | Query as entered | Purpose / observed result |
|---|---|---|
| Q01 | `10.1186/s12889-026-27570-3 Noh BRFSS myocardial infarction coronary heart disease machine learning full text` | Located the direct 2026 BRFSS 2023 prevalent MI/CHD comparator; publisher full text reviewed. |
| Q02 | `10.1016/j.cmpb.2025.109186 Building and validating machine learning model coronary heart disease non-invasive indicators full text` | Located BRFSS-to-NHANES CHD model; PubMed/publisher abstract available, full text not fully accessed. |
| Q03 | `10.1371/journal.pone.0330377 Deng Lu Hu LightGBM coronary heart disease full text` | Located and reviewed PLOS ONE full-text page for a multi-dataset CHD model. |
| Q04 | `BRFSS coronary heart disease machine learning temporal validation survey weights calibration research` | Broad exploratory query; surfaced relevant BRFSS and validation sources. Results were not treated as exhaustive. |
| Q05 | `TRIPOD+AI BMJ 2024 official PROBAST+AI BMJ 2025 official` | Located BMJ reporting and appraisal guidance. |
| Q06 | `CDC BRFSS 2023 annual data codebook 2025 annual data official` | Located official annual BRFSS documentation for both years. |
| Q07 | `"Machine Learning with Social Determinants of Health for Cross-Sectional Diabetes Classification" temporal validation BRFSS 2023 2024` | Located a BRFSS 2023-to-2024 frozen temporal-validation analogue for diabetes; direct article fetch failed. |
| Q08 | `Survey-Aware Machine Learning` guideline population health inference scoping review PMLR 333 198 | Located 2026 survey-aware ML guidance. |
| Q09 | `Machine learning based prediction models for cardiovascular disease risk using electronic health records data` systematic review meta-analysis ztae080 | Located systematic review/meta-analysis of EHR-based long-horizon CVD risk prediction. |
| Q10 | `Artificial intelligence in the risk prediction models of cardiovascular disease and development of an independent validation screening tool` BMC Medicine 2024 | Located full-text systematic review on validation/reporting concerns. |
| Q11 | `Assessing the performance of prediction models` framework traditional and novel measures Steyerberg 2010 calibration external validation | Located full-text methodological framework for discrimination and calibration. |
| Q12 | `10.7150/ijms.137605 authors DOI Machine Learning with Social Determinants of Health Cross-Sectional Diabetes Classification` and `heart disease BRFSS 2022 SMOTE machine learning 2026 Imani` | Confirmed the temporal-validation analogue and extracted accessible methods/results for the 2022 BRFSS study; found inconsistencies between abstract/table metrics and reported sample counts. |
| Q13 | `"Building and validating a machine learning model to predict coronary heart disease risk based on non-invasive indicators" authors` and `"Wanyonyi" "e0328338" coronary heart disease BRFSS machine learning` | Confirmed authors/metadata and reviewed the Wanyonyi full text; it describes a BRFSS 2015-derived secondary dataset distributed via IEEE DataPort and raises a methods-ordering question about SMOTE and splitting. |
| Q14 | `TRIPOD+AI BMJ q824 full text checklist 2024` | Confirmed the current 27-item TRIPOD+AI reporting checklist and its scope. |
| Q15 | `"Using broad health-related survey questions to predict the presence of coronary heart disease" Chavda Hyun 2024` | Located a 2024 BRFSS 2022 CHD/MI history classification study; landing-page summary reports MCC and accuracy under five-fold CV. |

## Working eligibility and evidence classes

- **Direct comparator:** same BRFSS source year and same prevalent self-reported MI/CHD target.
- **Temporal-validation analogue:** same annual survey framework but a different outcome.
- **External-validation comparator:** related CHD outcome with a different survey or population.
- **Methodological evidence:** calibration, validation, survey-aware ML and reporting/risk-of-bias guidance.
- **Official dataset documentation:** CDC codebooks, annual coverage, file versions and survey-design guidance.

Do not combine incident CVD prediction, clinical diagnosis, imaging, secondary benchmark datasets and cross-sectional prevalent-disease classification in one performance ranking. AUC/AP differences across different populations, target coding, feature panels, missing-data rules and thresholds are not head-to-head algorithm comparisons.

## Extraction fields

`literature/literature_matrix.csv` records source class, citation/DOI, population, outcome, predictors, validation, reported metrics, calibration/threshold, survey-design handling, limitations, relevance, verification status and screening decision. `literature/screening_log.csv` records source-level decisions. The blank `screening_log_template.csv` is retained as a reusable template.

For the next pass, extract the full methods/results for the uncertain records, check exact `_MICHD` coding, identify all annual sample sizes and exclusion counts, and record threshold/calibration/weighting details. Do not enter unreported values as zero or infer that an analysis was absent merely because it was not visible in the abstract.

## Key scientific cautions

- `_MICHD` concerns **prevalent self-reported MI and/or CHD**, not incident/future disease.
- Noh et al. (2026) means BRFSS + MI/CHD classification + leakage-aware modeling is not unique.
- Kung et al. (2026) means later-year validation across annual BRFSS samples is already demonstrated for a different cross-sectional outcome.
- The current project's survey-weighted metrics are point estimates only; no full complex-design uncertainty intervals were established.
- CDC currently lists 345 variables for the downloadable 2023 XPT and 284 for 2025. The project provenance records local files with 350 and 283 observed columns, respectively. Their SHA-256 fingerprints are recorded in `artifacts/provenance/dataset_provenance.json`. These discrepancies remain unresolved; preserve the locked experiment and do not silently substitute current downloads.
- Search scope is exploratory and incomplete. No “first study” or exhaustive novelty claim is justified.

## Actions proposed at the end of the first pass (superseded by the close-out below)

The first pass proposed further full-text extraction, database-specific exports, deduplication and checklist appraisal. The second pass completed the scoped source verification and created the appraisal/reporting artifacts to the extent supported by accessible sources. Database-specific exports and independent dual screening were not performed, so the final product is explicitly a targeted narrative/scoping review rather than a systematic review.


## Second-pass targeted verification and final disposition

**Date:** 2026-10-25. The following targeted queries and page-level checks were used to verify core comparator details and reporting guidance. They supplement Q01–Q15 above; they do not constitute a database-export search.

| Search label | Query / check | Outcome |
|---|---|---|
| Q16 | `Noh 2026 "Occupational and socioeconomic predictors" BRFSS myocardial infarction coronary heart disease 10.1186/s12889-026-27570-3 full text` | Rechecked publisher full text, methods, outcome, holdout, calibration and weighted sensitivity sections. |
| Q17 | `Kung 2026 "Machine Learning with Social Determinants of Health for Cross-Sectional Diabetes Classification" BRFSS 2023 2024` | Confirmed a BRFSS 2023-to-2024 frozen temporal-validation analogue from the indexed publisher page/search result; direct full-page retrieval was blocked, so detailed numerical extraction is not claimed. |
| Q18 | `Imani 2026 "Predicting cardiovascular diseases using imbalanced data" BRFSS 2022 XGBoost 10.1016/j.ahjo.2026.100719 full text` | Reviewed accessible PubMed/PMC/ScienceDirect text; flagged the abstract/table accuracy conflict and sample-count arithmetic mismatch. |
| Q19 | `Chavda Hyun 2024 "Using broad health-related survey questions to predict the presence of coronary heart disease" full text` | Reviewed the full 9-page PDF; extracted source/preprocessed counts, holdout/CV design, MCC/accuracy and limitations. |
| Q20 | `Wanyonyi 2025 BRFSS CHD machine learning SMOTE e0328338 PLOS ONE` | Reviewed methods and split/resampling passages; retained a conditional possible-leakage concern, not a confirmed error. |
| Q21 | `TRIPOD+AI checklist 27 items PROBAST+AI 2025 official BMJ` and official BMJ/EQUATOR checklist results | Confirmed TRIPOD+AI's 27 main items/52 subitems and PROBAST+AI's distinction between development quality and evaluation risk of bias. |
| Q22 | `CDC BRFSS 2023 annual data variables 345 update February 2025 2025 variables 284` | Rechecked official annual pages; preserved the unresolved local-versus-current source fingerprint/column-count discrepancy. |
| Q23 | `Survey-Aware Machine Learning guideline population health inference scoping review PMLR 333 198 2026` | Reviewed PMLR article page and abstract; reinforced the limitation of treating weighted point estimates as full design-based inference. |
| Q24 | `site:pubmed.ncbi.nlm.nih.gov BRFSS coronary heart disease machine learning classification survey data calibration 2024 2025` and `site:pubmed.ncbi.nlm.nih.gov "BRFSS" "myocardial infarction" machine learning classification 2022 2023` | Targeted PubMed-indexed searching surfaced relevant BRFSS and broader CVD prediction papers; no complete export or total result count was available. |
| Q25 | `"A systematic review and meta-analysis of machine learning-based prediction models for cardiovascular disease risk using electronic health records data" ztae080` and `"Artificial intelligence in the risk prediction models of cardiovascular disease" BMC Medicine 2024` | Reviewed broader systematic reviews as methodological context; their prospective/EHR questions are not direct comparators to cross-sectional BRFSS classification. |

### Final screening disposition

The working matrix contains 16 core evidence records. The seed source list has been deduplicated. Full text was reviewed for the closest comparator Noh et al., Chavda and Hyun, Wanyonyi et al., and the accessible Imani et al. article text. The Kung article was identified as a relevant temporal analogue but detailed full-text extraction remained limited by page access; Wu et al. remains primarily abstract-level evidence. These access limitations are recorded per source.

This review is complete as a **targeted critical narrative/scoping review**. It is not a systematic review: no complete Scopus/Web of Science/Embase/IEEE exports, full search-result counts, dual independent screening, or PRISMA flow were produced. A PRISMA diagram would imply a level of systematic retrieval and screening that was not performed, so none is included.

## Phase 2 close-out

The final synthesis is in `related_work_synthesis.md`; references are in `references.bib`; the appraisal and manuscript-readiness artifacts are `probast_ai_appraisal.csv` and `tripod_ai_reporting_audit.csv`. The next phase is manuscript drafting, not additional model training. Do not silently alter the locked Phase 1 model or outputs to address literature findings.
