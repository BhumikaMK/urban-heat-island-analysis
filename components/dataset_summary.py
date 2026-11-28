import streamlit as st
import pandas as pd


def render_dataset_summary(df):

    if df is None or df.empty:
        return

    st.divider()

    st.subheader("📈 Dataset Summary")

    # Standardise area type values
    area_types = (
        df["area_type"]
        .astype(str)
        .str.strip()
        .str.lower()
    )

    built_up_count = (area_types == "built-up").sum()

    green_count = (area_types == "green").sum()

    # Get observation date range
    dates = pd.to_datetime(
        df["date"],
        errors="coerce"
    ).dropna()

    if not dates.empty:
        date_range = (
            f"{dates.min().strftime('%d %b %Y')} - "
            f"{dates.max().strftime('%d %b %Y')}"
        )
    else:
        date_range = "Unavailable"

    # Display summary cards
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🏙️ Built-up Observations",
            built_up_count
        )

    with col2:
        st.metric(
            "🌳 Green Area Observations",
            green_count
        )

    with col3:
        st.metric(
            "📅 Observation Period",
            date_range
        )