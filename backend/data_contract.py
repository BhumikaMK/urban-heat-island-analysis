# --------------------------------
# DATA CONTRACT
# --------------------------------

# Required dataset columns

REQUIRED_COLUMNS = [
    "location",
    "area_type",
    "latitude",
    "longitude",
    "temperature_c",
    "date"
]


# Numeric columns

NUMERIC_COLUMNS = [
    "latitude",
    "longitude",
    "temperature_c"
]


# Valid area types

VALID_AREA_TYPES = {
    "built-up": "Built-up",
    "green": "Green"
}


# Geographic coordinate limits

LATITUDE_RANGE = (-90, 90)

LONGITUDE_RANGE = (-180, 180)