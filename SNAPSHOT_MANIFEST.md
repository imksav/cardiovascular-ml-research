# Phase 2 Final Source Snapshot Manifest

**Snapshot date:** 25 October 2026
**Project:** Cardiovascular Machine Learning Research: BRFSS-Based Classification of Prevalent Self-Reported Myocardial Infarction and Coronary Heart Disease with Temporal Validation
**Supplied branch:** `phase/02-literature-review` (as identified by the project owner)
**Archive type:** source snapshot, not a Git bundle. The uploaded ZIP did not contain `.git` metadata, so this manifest does not claim a commit hash or that the branch was pushed.

## Snapshot contents

The snapshot includes the supplied repository source tree, Phase 1 notebook, existing model artifacts, tables and figures, project documentation, Phase 2 literature artifacts, and a Phase 2 PDF summary. Raw BRFSS source data, `.git`, virtual environments and transient caches are excluded. Phase 1 model outputs and figures were not retrained or replaced during Phase 2.

## Final Phase 2 deliverables

- `literature/literature_matrix.csv`
- `literature/verified_seed_sources.csv`
- `literature/screening_log.csv`
- `literature/search_strategy.md`
- `literature/related_work_synthesis.md`
- `literature/references.bib`
- `literature/probast_ai_appraisal.csv`
- `literature/tripod_ai_reporting_audit.csv`
- `docs/PHASE2_RESEARCH_POSITIONING.md`
- `docs/PHASE2_FINAL_REPORT.md`
- `docs/PROJECT_STATUS.md`
- `README.md`
- `CHANGELOG.md`
- `research_log.md`
- `reports/PHASE2_FINAL_REPORT.pdf`

## File inventory and SHA-256 checksums

| Relative path | Bytes | SHA-256 |
|---|---:|---|
| `.github/ISSUE_TEMPLATE/bug-report.yml` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `.github/ISSUE_TEMPLATE/research-task.yml` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `.github/PULL_REQUEST_TEMPLATE.md` | 1254 | `3f40c3a3d4fdb97e452d0d220ec218c021dca48bcaab4c40a798ed194e31bcd6` |
| `.github/dependabot.yml` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `.github/workflows/repository-checks.yml` | 922 | `2482340ccf0f0419ef48a395ce3d95e987e660ed90e72517caa0fb17bce2382c` |
| `.gitignore` | 1667 | `15fdd2c90faaa3b98527f28657a18109bfc47fc8e7eddb48a479c33a582799f7` |
| `CHANGELOG.md` | 4278 | `43322789f569913a00569724aee81df73317414436c21b1a7bc120dfc3dacbf0` |
| `CITATION.cff` | 1307 | `7e863bc1c7581a8b122e9053d77dd0b36c173dac91e3e3cce43306fd6ad3adca` |
| `CONTRIBUTING.md` | 2624 | `23e25ac0ecc3beac77a3ef9c8eb7b0633383a5cef2bf531294395cc9a1f6bc0f` |
| `LICENSE` | 1071 | `8b126b3c789f88b2388edcf90587acbce2d5b2d71073f9e96cba5594952043d1` |
| `README.md` | 9688 | `90c1ecc8cd299c4232ca936bd1c9adb7eb3ebe884888eb6894dd760b33ffa4db` |
| `SECURITY.md` | 1134 | `0bbc060740c49a7fb3521fa9d1ddf268e6dc1cb431b6f61eb3f1b674bbc6a55e` |
| `artifacts/artifact_inventory.csv` | 1250 | `38241766709ff0077045db3cccaf0917192a8ee2703ebaea889ab9199c3fa1ad` |
| `artifacts/figures/calibration_internal_vs_temporal.png` | 165360 | `4b95a841296a2228a112496f4f81935afc55ec80557114015a2fea18c92a5afd` |
| `artifacts/figures/permutation_importance_cross_year.png` | 117939 | `9da17559594f4e2a8b59d7fabc84eb5be1154fb844065ed86b6d80fdba1c179d` |
| `artifacts/figures/roc_internal_vs_temporal.png` | 214114 | `ee4073f68df9fb170e1034ebe9a7e6ae2870d1ec9b941d54a2c93e4ffc416192` |
| `artifacts/models/brfss_2023_gradient_boosting_locked.joblib` | 208957 | `a9056ba281d5b8b8ba83c52b5ef5245f88496c9ca8acdbed76092acc7d4920b7` |
| `artifacts/models/brfss_2023_logistic_regression_locked.joblib` | 4934 | `3959d712d03955a70fd9e437d62381afd8f5de8387e96c66c1d90da75b05a916` |
| `artifacts/provenance/dataset_provenance.csv` | 531 | `b185b81a2833f64ccacf8b60b6d233b26a86e5005d0422b4af667523060721e8` |
| `artifacts/provenance/dataset_provenance.json` | 763 | `f43d4eb53bf7d682fd18fe1daf2affa06939d9bc9533fe425141330733f532f3` |
| `artifacts/provenance/git_provenance.json` | 76 | `af37fb0859a3fe088de17cbcc88f42fe4020aaf5f47278c007f4cac4b4b2996e` |
| `artifacts/provenance/research_manifest.json` | 2088 | `bf56668d59306759ddc301f9a6d804f35f0b4e969c0977501e8dd227942d6d17` |
| `artifacts/provenance/saved_model_provenance.csv` | 309 | `916bdfa1391da04459752526ed991d10b3e6ee151ee3bad83753d128b82fdc4e` |
| `artifacts/provenance/software_versions.json` | 436 | `9fbb612b65dd3ff13314bb29f8393d3c3c5796c85f59a8d1407af830231c3128` |
| `artifacts/provenance/software_versions.txt` | 356 | `6713910cf2ba508cbe46c4c4b803eb4a6a7954e15ce6e64c17cb3e70eb85672f` |
| `artifacts/tables/age_performance.csv` | 2432 | `952f5569331b567e16998e2a896e755e5db1c16643937dd5db79955e72c55d30` |
| `artifacts/tables/age_temporal_stability.csv` | 2094 | `92a34c27ca0f0706edd7f1ca3c00d23a4ed58afbc8f6aad0deb085de5773bc11` |
| `artifacts/tables/algorithm_comparison.csv` | 439 | `bf04d0726eb3b9fd106845e300a5b6b4a43381c22129ce4e92050bf8bee7a22c` |
| `artifacts/tables/bmi_distribution_shift.csv` | 209 | `295a1c4dc07bb9bfcf0fd2c7d1ac872e49f132a1d92d2c11576348581d045319` |
| `artifacts/tables/calibration_summary.csv` | 484 | `459679532ae69bacb427a71952271104bda7ae668c4db0e8bc47550d58591860` |
| `artifacts/tables/categorical_distribution_shift.csv` | 338 | `985959b1449b9a3777d7a64c7ea1005f3d6575f95d5689b50e0aaa6873ded4ca` |
| `artifacts/tables/evaluation_missingness_shift.csv` | 512 | `6cf3b514386ee4eca91557a0bd6b3e701bc055a77475d006159bb6cbaaec9cd0` |
| `artifacts/tables/feature_importance.csv` | 566 | `0356838fde4fbb8c1618a87fa9dcb43889430f7a53b086bd7c74aa5250333416` |
| `artifacts/tables/final_model_specification.csv` | 428 | `b8544f4bad32d26e495b95a5230dbd2a85f04098e19352151f586222f22f3622` |
| `artifacts/tables/manuscript_primary_results.csv` | 463 | `789c784ecb4b0ae8a336608a5324f5b93d5f535bbbfed093843100c382c1594d` |
| `artifacts/tables/missing_count_performance.csv` | 1450 | `f7d6946c0c01dd6b2ba2ec5ea629f4cd8caacbbdd6d9e440b94e2af5b783d59d` |
| `artifacts/tables/missingness_performance.csv` | 1063 | `f73cb0a58f0e617b1b28e50d84089a98d21b058ae1c9ef3abf89512706c5d24b` |
| `artifacts/tables/performance_change.csv` | 708 | `0d5994dc806677018dcaa8e1654d87b9fe6b3eaca2ffaaad8cd7b67c2c89b418` |
| `artifacts/tables/predictor_subgroup_performance.csv` | 7648 | `0a4e0e61e5123cbdfa9f75d2dbc394aade30ae5e0721ecaa7d37eae7b2dbec1c` |
| `artifacts/tables/primary_performance.csv` | 517 | `ba58ea485b73cecc7bfdd8e2f92ad7ea779e05846add3f0984f49b4c784929ea` |
| `artifacts/tables/survey_weighted_results.csv` | 581 | `a6384a936fa3ec770b81bf917a8d4f1e12f5e1ded34d86bc8517b06355374fce` |
| `artifacts/tables/temporal_stability.csv` | 428 | `d56e5efb4d4ef3912a827241ded5bb7f1a6880fcffa9624b3a3738bb63bc4e51` |
| `artifacts/tables/threshold_robustness.csv` | 1644 | `bcb23bf6fd6e4db561350e1b1f87012e34b0b753cdc627c3ee174e724e025fa4` |
| `data/README.md` | 1882 | `1324a1eb46ad534cbd809f64f0da4b63566f7ecb3946f068ebe1c88dc6a2432d` |
| `data/interim/.gitkeep` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `data/processed/.gitkeep` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `docs/PHASE2_FINAL_REPORT.md` | 7636 | `23e0242e490a72c7eba3828462d1d5b8b02007f58bc8100ad9b62d5597530057` |
| `docs/PHASE2_RESEARCH_POSITIONING.md` | 11251 | `f392964ffdd0f1204a1737207e0e4167d75f7e3d987a90e759253f8a016ef4af` |
| `docs/PROJECT_STATUS.md` | 12164 | `0f422dcb839acc048cf2a3fa3f1ad4ccb9d10a0d862f07ddabb80653065329a8` |
| `docs/data_dictionary.md` | 4796 | `40ff705e6ce5161dd31ee41b0a64dd4a20a9465fd631aa3e4c983b4860939b2e` |
| `docs/dataset_selection.md` | 3569 | `9cc8378820aea4ed51131e519e07f83cca13da1fb08d7bfc87b6a4aa4b529817` |
| `docs/research_protocol.md` | 6081 | `f8966ae526deafca307255e81b4ddfd35484f4adf194ce821ed25c7adb318a7e` |
| `docs/research_questions.md` | 2477 | `8c4f389d02ec05d30ca9222c6d88b52db9220c2e3901cecbec67282e51d140af` |
| `literature/literature_matrix.csv` | 23740 | `c1c27143d0ed5d8e83c76bcecfa9d272b4e8c580207a8ca9d0fde9f23e77d585` |
| `literature/probast_ai_appraisal.csv` | 5221 | `30a5b8aa15c6f2696c6b64ce8e0e2e44d877276711de24fea72816ea9582c305` |
| `literature/references.bib` | 7190 | `2498bcfad298f73abfb8cb4f375e825e1af5a25f1199cf5fc97a44fa5f1f187f` |
| `literature/related_work_synthesis.md` | 17110 | `46fbefac3042cd3a1f244aea637378efa719f38c7750b21f0977615cfff4b2b4` |
| `literature/screening_log.csv` | 6247 | `158981864458355d28083b52bc8039de9fb6d06a0fab998ed75ffd9882e460d3` |
| `literature/screening_log_template.csv` | 147 | `553f63624d0dd7817f32f9390732ee86c4354d7dd5e7d27aa7c82ebc2dc6e511` |
| `literature/search_strategy.md` | 13571 | `d4f7f491304f4ed08ba66c27ba1bfdaa76658e8e238464289b11cfe9b81f0b16` |
| `literature/tripod_ai_reporting_audit.csv` | 12984 | `87b6b14569dffe2fc755851f75585b6ce502fa332acdf012f0e6815ffbb55617` |
| `literature/verified_seed_sources.csv` | 9522 | `335daa36ceb47af5e0c8b926eafc255b0936654ead00821cdf0a10cd64dff816` |
| `notebooks/03_brfss_2023_first_look_optimised.ipynb` | 2377312 | `a7c2bb48383d47baef6391657b114aa3995ecf77af4d0dc64fe447194a24c313` |
| `paper/.gitkeep` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `reports/03_brfss_2023_first_look_optimised.html` | 2131217 | `720da9e90ef6def265c97ff0d06b97519d7e52addd81a535863390b2cd7f8a69` |
| `reports/PHASE2_FINAL_REPORT.pdf` | 51885 | `f39fc3bb6df391a9b2e94ad2466573f789e16ac0d308ed115a180e5dd851ec16` |
| `requirements.txt` | 430 | `5262d21e863c78476d7419d58471d0f30f751e33310cb1409b1479f026733bd3` |
| `research_log.md` | 17918 | `aed998450734ba1ef9d9fe13631ac74f94c14754a684be15178fa5175741df1b` |
| `scripts/check_repository.py` | 7515 | `cafa34ab945800cc7e79f7ca4267a4565d70b2a50b920b38ca680646fcd6218e` |
| `tests/.gitkeep` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |

## Validation notes

- Notebook JSON parses successfully; 459 cells, including 223 code cells.
- The literature matrix has 16 records; the source-level screening log has 16 records; the deduplicated seed list has 14 unique sources.
- The TRIPOD+AI pre-manuscript audit has 52 subitems; the provisional PROBAST+AI appraisal has 8 records (seven comparator studies plus the current project).
- CSV parsing and PDF metadata/text extraction were checked.
- `scripts/check_repository.py` requires Git metadata for its Git candidate-file audit. The supplied ZIP has no `.git`; the audit was therefore tested separately in a temporary initialized Git checkout. Its existing `git_provenance.json` warning remains for review against the project owner's actual branch history.
- The literature review is a targeted critical narrative/scoping review, not a systematic review; no PRISMA flow is claimed.
- The CDC source-file/column-count discrepancy and author-confirmation items remain explicitly documented for Phase 3/reproducibility review.
