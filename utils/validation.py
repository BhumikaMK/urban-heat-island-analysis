import pandas as pd
from io import BytesIO

from backend.data_contract import (
    REQUIRED_COLUMNS,
    NUMERIC_COLUMNS,
    VALID_AREA_TYPES,
    LATITUDE_RANGE,
    LONGITUDE_RANGE
)


def validate_csv(uploaded_file):

    errors = []

    if uploaded_file is None:
        return None, ["No file uploaded."]

    try:

        df = pd.read_csv(
            BytesIO(uploaded_file.getvalue())
        )

    except Exception:
        return None, ["Unable to read the CSV file."]

    # Check required columns

    missing_columns = [
        col for col in REQUIRED_COLUMNS
        if col not in df.columns
    ]

    if missing_columns:

        errors.append(
            f"Missing required columns: {', '.join(missing_columns)}"
        )

        return df, errors

    # Check empty dataset

    if df.empty:

        errors.append("The uploaded dataset is empty.")

        return df, errors

    # Check missing values

    if df[REQUIRED_COLUMNS].isnull().any().any():

        errors.append(
            "The dataset contains missing values "
            "in required columns."
        )

    # Standardise location

    df["location"] = (
        df["location"]
        .astype(str)
        .str.strip()
    )

    if df["location"].eq("").any():

        errors.append(
            "Location contains empty values."
        )

    # Standardise area types

    area_types = (
        df["area_type"]
        .astype(str)
        .str.strip()
        .str.lower()
    )

    invalid_types = ~area_types.isin(
        VALID_AREA_TYPES
    )

    if invalid_types.any():

        errors.append(
            "Area type must be either Built-up or Green."
        )

    else:

        df["area_type"] = area_types.map(
            VALID_AREA_TYPES
        )

    # Convert numeric columns

    for col in NUMERIC_COLUMNS:

        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

        if df[col].isnull().any():

            errors.append(
                f"{col} must contain valid numeric values."
            )

    # Validate latitude

    latitude = df["latitude"]

    if (
        (latitude < LATITUDE_RANGE[0]) |
        (latitude > LATITUDE_RANGE[1])
    ).any():

        errors.append(
            "Latitude must be between -90 and 90."
        )

    # Validate longitude

    longitude = df["longitude"]

    if (
        (longitude < LONGITUDE_RANGE[0]) |
        (longitude > LONGITUDE_RANGE[1])
    ).any():

        errors.append(
            "Longitude must be between -180 and 180."
        )

    # Validate and convert dates

    df["date"] = pd.to_datetime(
        df["date"],
        errors="coerce"
    )

    if df["date"].isnull().any():

        errors.append(
            "Date contains invalid values."
        )

    return df, errors