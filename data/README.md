# BRFSS Source Data

This study uses public-use survey data from the **U.S. Centers for Disease Control and Prevention (CDC) Behavioral Risk Factor Surveillance System (BRFSS)**. Obtain the original annual data files and the corresponding questionnaires/codebooks from the official [CDC BRFSS annual data page](https://www.cdc.gov/brfss/annual_data/annual_data.htm).

## Expected local file layout

```text
data/raw/brfss/
├── 2023/LLCP2023.XPT
├── 2024/LLCP2024.XPT
└── 2025/LLCP2025.XPT
```

- **2023:** Development, training, validation and held-out testing.
- **2024:** Investigated for compatibility; not used for the locked six-predictor temporal evaluation because the required blood-pressure measure was unavailable in the compatible form.
- **2025:** Frozen-model evaluation across an independent later annual survey sample.

**Do not commit the XPT files.** Download them locally into the indicated directories. The raw files remain unchanged; derived features, predictions and results belong in the separate analysis/artifact workflow.

## Research scope

The outcome `_MICHD` is based on self-reported history of myocardial infarction and/or coronary heart disease. These are cross-sectional survey observations, **not** future cardiovascular events or clinical diagnoses. BRFSS survey weights are retained for separate weighted evaluation rather than used as predictive features.

## Provenance and reproducibility

The `artifacts/provenance/` folder contains recorded dataset and analysis metadata. Consult `docs/data_dictionary.md`, `docs/dataset_selection.md`, and `docs/research_protocol.md` for selected variables, processing rules and validation decisions. Check official annual source documentation for changes across survey years. Reproduction requires compatible source files and software; no data have been redistributed in this repository.
