# Urban Heat Island Analysis – Dataset Guide

## 1. Purpose

This dataset contains temperature observations
from built-up and green areas across Bengaluru.

It is used to analyse Urban Heat Island effects
and compare temperature variations between
different types of urban areas.

## 2. Required Columns

| Column | Data Type | Description |
|---|---|---|
| location | String | Bengaluru location name |
| area_type | String | Built-up or Green |
| latitude | Float | Geographic latitude |
| longitude | Float | Geographic longitude |
| temperature_c | Float | Temperature in Celsius |
| date | Date | Observation date |

## 3. Accepted Area Types

- Built-up
- Green

## 4. Sample Data

| location | area_type | temperature_c |
|---|---|---|
| Jayanagar | Built-up | 34.5 |
| Jayanagar | Green | 29.2 |
| Whitefield | Built-up | 36.1 |
| Whitefield | Green | 30.4 |

## 5. Validation Rules

- All required columns must exist.
- Temperature must be numeric.
- Latitude must be between -90 and 90.
- Longitude must be between -180 and 180.
- Dates must be valid.
- Required fields must not contain missing values.

## 6. Important Notes

- Upload files in CSV format.
- Use the specified column names.
- Sample data is synthetic and intended only for testing.
- Actual analysis requires verified temperature observations.