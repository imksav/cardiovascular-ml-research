from __future__ import annotations



import argparse

import csv

import hashlib

import json

import subprocess

from collections import Counter

from datetime import datetime, timezone

from html.parser import HTMLParser

from pathlib import Path



import pyreadstat





ROOT = Path(__file__).resolve().parents[1]

PROVENANCE_JSON = ROOT / "artifacts" / "provenance" / "dataset_provenance.json"

OUTPUT_DIR = ROOT / "artifacts" / "provenance"



CDC_LAYOUT_2025 = (

    ROOT / "docs" / "references" / "cdc"

    / "llcp_varlayout_25_onecolumn.html"

)



CDC_SUMMARY = {

    2023: {

        "records": 433323,

        "variables": 350,

        "url": "https://www.cdc.gov/brfss/annual_data/annual_2023.html",

    },

    2024: {

        "records": 457670,

        "variables": 301,

        "url": "https://www.cdc.gov/brfss/annual_data/annual_2024.html",

    },

    2025: {

        "records": 356158,

        "variables": 284,

        "url": "https://www.cdc.gov/brfss/annual_data/annual_2025.html",

    },

}



PREDICTORS = {

    "_AGEG5YR": "AGE_GROUP",

    "EXERANY2": "PHYSICAL_ACTIVITY",

    "_SMOKER3": "SMOKING_STATUS",

    "BPHIGH6": "BLOOD_PRESSURE",

    "DIABETE4": "DIABETES_STATUS",

    "_BMI5": "BMI",

}



OUTCOME_FIELDS = ["_MICHD", "CVDINFR4", "CVDCRHD4"]

DESIGN_FIELDS = ["_LLCPWT", "_STSTR", "_PSU"]





def sha256_file(path: Path) -> str:

    digest = hashlib.sha256()

    with path.open("rb") as handle:

        for chunk in iter(lambda: handle.read(8 * 1024 * 1024), b""):

            digest.update(chunk)

    return digest.hexdigest()





class CDCLayoutParser(HTMLParser):

    def __init__(self):

        super().__init__(convert_charrefs=True)

        self.in_table = False

        self.rows = []

        self.row = None

        self.cell = None



    def handle_starttag(self, tag, attrs):

        tag = tag.lower()



        if tag == "table" and not self.in_table:

            self.in_table = True

        elif tag == "tr" and self.in_table:

            self.row = []

        elif tag in ("td", "th") and self.row is not None:

            self.cell = []



    def handle_data(self, data):

        if self.cell is not None:

            self.cell.append(data)



    def handle_endtag(self, tag):

        tag = tag.lower()



        if tag in ("td", "th") and self.cell is not None:

            self.row.append(" ".join(" ".join(self.cell).split()))

            self.cell = None

        elif tag == "tr" and self.row is not None:

            if any(self.row):

                self.rows.append(self.row)

            self.row = None

        elif tag == "table" and self.in_table:

            self.in_table = False





def read_cdc_layout(path: Path) -> list[str]:

    if not path.is_file():

        raise FileNotFoundError(f"CDC layout not found: {path}")



    parser = CDCLayoutParser()

    parser.feed(path.read_text(encoding="utf-8", errors="replace"))



    header_index = None

    variable_column = None



    for index, row in enumerate(parser.rows):

        if "Variable Name" in row:

            header_index = index

            variable_column = row.index("Variable Name")

            break



    if header_index is None:

        raise ValueError("Could not locate 'Variable Name' in CDC layout.")



    names = []

    for row in parser.rows[header_index + 1:]:

        if len(row) > variable_column and row[variable_column]:

            names.append(row[variable_column].strip())



    if not names:

        raise ValueError("No variable names were extracted from CDC layout.")



    return names





def git_value(*args):

    try:

        result = subprocess.run(

            ["git", *args],

            cwd=ROOT,

            capture_output=True,

            text=True,

            check=False,

        )

        if result.returncode == 0:

            return result.stdout.strip()

    except OSError:

        pass

    return None





def load_provenance() -> dict:

    if not PROVENANCE_JSON.is_file():

        raise FileNotFoundError(

            f"Existing provenance JSON not found: {PROVENANCE_JSON}"

        )



    records = json.loads(PROVENANCE_JSON.read_text(encoding="utf-8"))

    return {int(item["survey_year"]): item for item in records}





def audit_dataset(year: int, provenance: dict, cdc_layout_names=None):

    path = (

        ROOT / "data" / "raw" / "brfss"

        / str(year) / f"LLCP{year}.XPT"

    )



    if not path.is_file():

        raise FileNotFoundError(f"Dataset not found: {path}")



    print(f"Inspecting {year}: {path.name}")



    _, metadata = pyreadstat.read_xport(

        str(path),

        metadataonly=True,

        encoding="latin1",

    )



    names = list(metadata.column_names)

    name_set = set(names)

    duplicate_names = sorted(

        name for name, count in Counter(names).items() if count > 1

    )



    actual_size = path.stat().st_size

    actual_hash = sha256_file(path)

    # Metadata-only XPORT reads do not reliably provide respondent rows.

    # Read only the target column to count records with bounded memory.

    row_frame, _ = pyreadstat.read_xport(

        str(path),

        usecols=["_MICHD"],

        encoding="latin1",

    )

    actual_rows = int(len(row_frame))

    del row_frame

    actual_variables = len(names)



    published = CDC_SUMMARY[year]

    recorded = provenance.get(year, {})



    missing_predictors = [

        name for name in PREDICTORS if name not in name_set

    ]

    missing_outcomes = [

        name for name in OUTCOME_FIELDS if name not in name_set

    ]

    missing_design = [

        name for name in DESIGN_FIELDS if name not in name_set

    ]



    layout_count = None

    layout_match = None

    layout_missing = []

    local_not_in_layout = []



    if year == 2025:

        if cdc_layout_names is None:

            raise ValueError("2025 CDC layout names were not supplied.")



        layout_set = set(cdc_layout_names)

        layout_count = len(cdc_layout_names)

        layout_missing = sorted(layout_set - name_set)

        local_not_in_layout = sorted(name_set - layout_set)

        layout_match = (

            name_set == layout_set

            and len(cdc_layout_names) == len(layout_set)

        )



    provenance_size_match = (

        recorded.get("file_size_bytes") == actual_size

    )

    provenance_hash_match = (

        str(recorded.get("sha256", "")).lower() == actual_hash.lower()

    )



    row_count_match = actual_rows == published["records"]

    summary_variable_count_match = (

        actual_variables == published["variables"]

    )



    failures = []



    if duplicate_names:

        failures.append("Duplicate variable names detected.")

    if not row_count_match:

        failures.append("Respondent count differs from CDC published count.")

    if not provenance_size_match:

        failures.append("File size differs from recorded provenance.")

    if not provenance_hash_match:

        failures.append("SHA-256 differs from recorded provenance.")

    if missing_outcomes:

        failures.append("One or more outcome fields are missing.")

    if missing_design:

        failures.append("One or more survey-design fields are missing.")



    if year in (2023, 2025) and missing_predictors:

        failures.append("Required locked predictors are missing.")



    if year == 2024 and missing_predictors != ["BPHIGH6"]:

        failures.append(

            "2024 predictor incompatibility differs from the documented "

            "BPHIGH6 limitation."

        )



    if year in (2023, 2024) and not summary_variable_count_match:

        failures.append(

            "Variable count differs from the CDC published summary."

        )



    if year == 2025 and not layout_match:

        failures.append(

            "Local 2025 variable names do not exactly match CDC layout."

        )



    if failures:

        status = "REVIEW_REQUIRED"

    elif year == 2024:

        status = "COMPATIBILITY_AUDIT_ONLY"

    elif year == 2025 and not summary_variable_count_match:

        status = "PASS_WITH_DOCUMENTED_COUNT_DISCREPANCY"

    else:

        status = "PASS"



    labels = dict(zip(

        names,

        list(metadata.column_labels or []),

    ))



    return {

        "survey_year": year,

        "filename": path.name,

        "resolved_path": str(path.resolve()),

        "file_size_bytes": actual_size,

        "sha256": actual_hash,

        "respondent_count": actual_rows,

        "variable_count": actual_variables,

        "duplicate_variable_names": duplicate_names,

        "cdc_published_respondent_count": published["records"],

        "respondent_count_matches_cdc": row_count_match,

        "cdc_summary_variable_count": published["variables"],

        "variable_count_matches_cdc_summary": summary_variable_count_match,

        "cdc_layout_variable_count": layout_count,

        "cdc_layout_exact_match": layout_match,

        "cdc_layout_missing_from_local": layout_missing,

        "local_variables_not_in_cdc_layout": local_not_in_layout,

        "predictor_variables_present": [

            name for name in PREDICTORS if name in name_set

        ],

        "predictor_variables_missing": missing_predictors,

        "outcome_variables_present": [

            name for name in OUTCOME_FIELDS if name in name_set

        ],

        "outcome_variables_missing": missing_outcomes,

        "design_variables_present": [

            name for name in DESIGN_FIELDS if name in name_set

        ],

        "design_variables_missing": missing_design,

        "locked_predictor_compatible": not missing_predictors,

        "provenance_size_match": provenance_size_match,

        "provenance_sha256_match": provenance_hash_match,

        "variable_labels": {

            name: labels.get(name) for name in (

                list(PREDICTORS) + OUTCOME_FIELDS + DESIGN_FIELDS

            ) if name in name_set

        },

        "cdc_reference_url": published["url"],

        "metadata_encoding": "latin1",

        "status": status,

        "failures": failures,

    }





def value_labels_for(metadata, variable):

    direct = getattr(metadata, "variable_value_labels", {}) or {}

    if variable in direct:

        return direct[variable]



    variable_to_label = (

        getattr(metadata, "variable_to_label", {}) or {}

    )

    label_set_name = variable_to_label.get(variable)



    all_labels = getattr(metadata, "value_labels", {}) or {}

    if label_set_name:

        return all_labels.get(label_set_name, {})



    return {}





def code_label(labels, wanted_code):

    for code, label in labels.items():

        try:

            if float(code) == wanted_code:

                return str(label).strip().lower()

        except (TypeError, ValueError):

            continue

    return ""





def json_scalar(value):

    if hasattr(value, "item"):

        value = value.item()



    if value is None:

        return None



    if isinstance(value, float) and value != value:

        return None



    if isinstance(value, (str, int, float, bool)):

        return value



    return str(value)






def run_profile():
    import pandas as pd

    profile_rows = []
    consistency_results = []

    profile_variables = list(PREDICTORS) + OUTCOME_FIELDS

    cdc_documentation = {
        2023: (
            "https://www.cdc.gov/brfss/annual_data/2023/pdf/"
            "2023-calculated-variables-version4-508.pdf"
        ),
        2024: (
            "https://www.cdc.gov/brfss/annual_data/2024/pdf/"
            "2024-calculated-variables-version4-508.pdf"
        ),
        2025: (
            "https://www.cdc.gov/brfss/annual_data/2025/pdf/"
            "2025-calculated-variables-version4-508.pdf"
        ),
    }

    target_fields = ["_MICHD", "CVDINFR4", "CVDCRHD4"]

    for year in (2023, 2024, 2025):
        path = (
            ROOT / "data" / "raw" / "brfss"
            / str(year) / f"LLCP{year}.XPT"
        )

        _, metadata = pyreadstat.read_xport(
            str(path),
            metadataonly=True,
            encoding="latin1",
        )

        available = [
            name for name in profile_variables
            if name in metadata.column_names
        ]

        frame, data_metadata = pyreadstat.read_xport(
            str(path),
            usecols=available,
            encoding="latin1",
        )

        # XPT column labels are aligned with metadata.column_names,
        # not with the order of the requested usecols list.
        metadata_names = list(data_metadata.column_names or [])
        metadata_labels = list(data_metadata.column_labels or [])
        label_map = dict(zip(metadata_names, metadata_labels))

        for variable in available:
            series = frame[variable]
            top_values = []

            for value, count in series.value_counts(
                dropna=False
            ).head(20).items():
                top_values.append({
                    "value": json_scalar(value),
                    "count": int(count),
                })

            profile_rows.append({
                "survey_year": year,
                "variable": variable,
                "variable_label": label_map.get(variable),
                "row_count": len(series),
                "non_null_count": int(series.notna().sum()),
                "null_count": int(series.isna().sum()),
                "distinct_raw_values": int(series.nunique(dropna=True)),
                "top_raw_values_json": json.dumps(
                    top_values, ensure_ascii=False
                ),
            })

        missing_target_fields = [
            variable for variable in target_fields
            if variable not in frame.columns
        ]

        if missing_target_fields:
            raise RuntimeError(
                f"{year}: required target fields are missing: "
                f"{missing_target_fields}"
            )

        # CDC _MICHD calculated-variable rule:
        # 1 if either source variable equals 1;
        # 2 if both source variables equal 2;
        # missing otherwise.
        positive = (
            frame["CVDINFR4"].eq(1)
            | frame["CVDCRHD4"].eq(1)
        )

        negative = (
            frame["CVDINFR4"].eq(2)
            & frame["CVDCRHD4"].eq(2)
        )

        expected = pd.Series(
            pd.NA,
            index=frame.index,
            dtype="Int64",
        )
        expected.loc[positive] = 1
        expected.loc[negative] = 2

        observed = pd.to_numeric(
            frame["_MICHD"],
            errors="coerce",
        ).astype("Int64")

        both_missing = observed.isna() & expected.isna()

        both_defined_equal = (
            observed.notna()
            & expected.notna()
            & observed.eq(expected).fillna(False)
        )

        matches = both_missing | both_defined_equal
        mismatch_mask = ~matches

        mismatch_indices = frame.index[mismatch_mask][:10]
        mismatch_examples = []

        for row_index in mismatch_indices:
            row = frame.loc[row_index]
            expected_value = expected.loc[row_index]

            mismatch_examples.append({
                "row_number_1_based": int(row_index) + 1,
                "observed_MICHD": json_scalar(row["_MICHD"]),
                "CVDINFR4": json_scalar(row["CVDINFR4"]),
                "CVDCRHD4": json_scalar(row["CVDCRHD4"]),
                "expected_MICHD": (
                    None
                    if pd.isna(expected_value)
                    else int(expected_value)
                ),
            })

        mismatch_count = int(mismatch_mask.sum())

        result = {
            "survey_year": year,
            "status": (
                "CONSISTENT_WITH_CDC_FORMULA"
                if mismatch_count == 0
                else "MISMATCHES_FOUND"
            ),
            "rows_checked": int(len(frame)),
            "rows_with_defined_expected_value": int(
                expected.notna().sum()
            ),
            "rows_expected_missing": int(
                expected.isna().sum()
            ),
            "observed_target_missing_rows": int(
                observed.isna().sum()
            ),
            "mismatch_count": mismatch_count,
            "mismatch_examples": mismatch_examples,
            "formula": (
                "1 if CVDINFR4 == 1 or CVDCRHD4 == 1; "
                "2 if CVDINFR4 == 2 and CVDCRHD4 == 2; "
                "missing otherwise."
            ),
            "verification_basis": (
                "CDC calculated-variable documentation. "
                "XPT value labels were not used because they were "
                "not exposed in the source metadata."
            ),
            "cdc_documentation_url": cdc_documentation[year],
        }

        consistency_results.append(result)

    profile_path = OUTPUT_DIR / "phase3_core_variable_profile.csv"
    consistency_path = OUTPUT_DIR / "phase3_target_consistency.json"

    with profile_path.open(
        "w", newline="", encoding="utf-8-sig"
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "survey_year",
                "variable",
                "variable_label",
                "row_count",
                "non_null_count",
                "null_count",
                "distinct_raw_values",
                "top_raw_values_json",
            ],
        )
        writer.writeheader()
        writer.writerows(profile_rows)

    consistency_path.write_text(
        json.dumps(consistency_results, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    print("Profile CSV:", profile_path)
    print("Target consistency JSON:", consistency_path)

    for result in consistency_results:
        print(
            result["survey_year"],
            result["status"],
            "rows checked:", result["rows_checked"],
            "expected missing:", result["rows_expected_missing"],
            "mismatches:", result["mismatch_count"],
        )

def main():

    parser = argparse.ArgumentParser(

        description="Read-only BRFSS dataset provenance and schema audit."

    )

    parser.add_argument(

        "--profile",

        action="store_true",

        help="Also profile core raw variables and verify _MICHD "
             "against the CDC calculated-variable rule.",

    )

    args = parser.parse_args()



    if args.profile:

        output_paths = [

            OUTPUT_DIR / "phase3_core_variable_profile.csv",

            OUTPUT_DIR / "phase3_target_consistency.json",

        ]

    else:

        output_paths = [

            OUTPUT_DIR / "phase3_dataset_audit.json",

            OUTPUT_DIR / "phase3_dataset_audit.csv",

        ]



    existing = [str(path) for path in output_paths if path.exists()]

    if existing:

        raise FileExistsError(

            "Refusing to overwrite existing Phase 03 outputs: "

            + ", ".join(existing)

        )



    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)



    if args.profile:

        run_profile()

        return



    provenance = load_provenance()

    cdc_layout_names = read_cdc_layout(CDC_LAYOUT_2025)



    print("CDC 2025 layout variables:", len(cdc_layout_names))

    print("Starting read-only BRFSS audit...")



    datasets = [

        audit_dataset(

            year,

            provenance,

            cdc_layout_names if year == 2025 else None,

        )

        for year in (2023, 2024, 2025)

    ]



    failures = [

        f"{item['survey_year']}: {failure}"

        for item in datasets

        for failure in item["failures"]

    ]



    known_limitations = [

        "2024 is a compatibility audit only: BPHIGH6 is absent, "

        "so the locked six-predictor model cannot be evaluated on 2024.",

        "The 2025 CDC annual summary reports 284 variables, while the "

        "archived detailed layout and matching local XPT contain 283 "

        "variable names. Both counts are retained as a documented "

        "source discrepancy.",

        "The 2025 local XPT matches the archived detailed CDC layout "

        "by variable name; this is a schema comparison, not independent "

        "proof of the original download transaction.",

    ]



    overall_status = (

        "REVIEW_REQUIRED"

        if failures

        else "PASS_WITH_DOCUMENTED_LIMITATIONS"

    )



    git_status = git_value("status", "--porcelain")



    audit = {

        "audit_timestamp_utc": datetime.now(timezone.utc).isoformat(),

        "audit_script": str(Path(__file__).resolve()),

        "audit_status": overall_status,

        "audit_scope": (

            "Read-only source-file integrity, respondent counts, "

            "schema, predictor/outcome/design fields, CDC layout "

            "comparison and provenance-record comparison."

        ),

        "git": {

            "commit": git_value("rev-parse", "HEAD"),

            "branch": git_value("branch", "--show-current"),

            "working_tree_clean": (

                not bool(git_status) if git_status is not None else None

            ),

        },

        "cdc_2025_layout": {

            "path": str(CDC_LAYOUT_2025.resolve()),

            "sha256": sha256_file(CDC_LAYOUT_2025),

            "variable_count": len(cdc_layout_names),

        },

        "datasets": datasets,

        "known_limitations": known_limitations,

        "failures": failures,

    }



    json_path = OUTPUT_DIR / "phase3_dataset_audit.json"

    csv_path = OUTPUT_DIR / "phase3_dataset_audit.csv"



    json_path.write_text(

        json.dumps(audit, indent=2, ensure_ascii=False),

        encoding="utf-8",

    )



    csv_fields = [

        "survey_year",

        "filename",

        "file_size_bytes",

        "sha256",

        "respondent_count",

        "variable_count",

        "cdc_published_respondent_count",

        "respondent_count_matches_cdc",

        "cdc_summary_variable_count",

        "variable_count_matches_cdc_summary",

        "cdc_layout_variable_count",

        "cdc_layout_exact_match",

        "predictor_variables_missing",

        "outcome_variables_missing",

        "design_variables_missing",

        "locked_predictor_compatible",

        "provenance_size_match",

        "provenance_sha256_match",

        "status",

        "failures",

    ]



    with csv_path.open(

        "w", newline="", encoding="utf-8-sig"

    ) as handle:

        writer = csv.DictWriter(handle, fieldnames=csv_fields)

        writer.writeheader()



        for item in datasets:

            row = {field: item.get(field) for field in csv_fields}

            for field in (

                "predictor_variables_missing",

                "outcome_variables_missing",

                "design_variables_missing",

                "failures",

            ):

                row[field] = json.dumps(item.get(field, []))

            writer.writerow(row)



    print("\nAUDIT STATUS:", overall_status)



    for item in datasets:

        print(

            item["survey_year"],

            "| rows:", item["respondent_count"],

            "| variables:", item["variable_count"],

            "| missing predictors:", item["predictor_variables_missing"],

            "| status:", item["status"],

        )



    if failures:

        print("\nFAILURES:")

        for failure in failures:

            print("-", failure)



    print("\nCreated:")

    print(json_path)

    print(csv_path)



if __name__ == "__main__":

    main()

