import streamlit as st


def render_heat_map_page(df=None):

    st.title("🗺️ Bengaluru Heat Map")

    st.caption(
        "Explore geographical temperature distribution "
        "across Bengaluru."
    )

    st.divider()

    if df is None or df.empty:

        st.warning(
            "Please upload and validate a temperature "
            "dataset from the Overview page."
        )

        return

    st.success(
        f"Dataset connected successfully: {len(df)} records."
    )

    # Map filters
    st.subheader("Map Filters")

    col1, col2 = st.columns(2)

    with col1:

        area_types = ["All Areas", "Built-up", "Green"]

        selected_area = st.selectbox(
            "Select Area Type",
            area_types,
            key="heatmap_area"
        )

    with col2:

        locations = ["All Locations"] + sorted(
            df["location"].dropna().unique().tolist()
        )

        selected_location = st.selectbox(
            "Select Location",
            locations,
            key="heatmap_location"
        )

    st.divider()

    st.subheader("Geographical Temperature Distribution")

    st.info(
        "Interactive Bengaluru temperature map "
        "will be integrated here."
    )

    st.divider()

    st.subheader("Map Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Records", len(df))

    with col2:
        st.metric(
            "Built-up Records",
            (df["area_type"].str.lower() == "built-up").sum()
        )

    with col3:
        st.metric(
            "Green Records",
            (df["area_type"].str.lower() == "green").sum()
        )