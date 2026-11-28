import streamlit as st


def render_recommendations_page(df=None):

    st.title("🌳 Environmental Recommendations")

    st.caption(
        "Explore possible strategies for reducing "
        "urban heat across Bengaluru."
    )

    st.divider()

    # Check dataset availability

    if df is None or df.empty:

        st.warning(
            "Please upload and validate a temperature "
            "dataset from the Overview page."
        )

        return

    st.success(
        f"Dataset connected successfully: {len(df)} records."
    )

    # Introduction
    st.subheader("Reducing Urban Heat")

    st.write(
        """
        Urban Heat Island effects can be reduced through
        sustainable urban planning, increased vegetation,
        improved building materials and better land management.
        """
    )

    st.divider()

    # Recommendation categories
    st.subheader("Recommended Environmental Interventions")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### 🌳 Urban Greening")

        st.write(
            """
            - Increase tree plantation.
            - Develop urban parks.
            - Protect existing green spaces.
            - Introduce rooftop gardens.
            """
        )

    with col2:

        st.markdown("### 🏢 Sustainable Buildings")

        st.write(
            """
            - Use reflective roofing materials.
            - Introduce green roofs.
            - Improve building ventilation.
            - Encourage energy-efficient designs.
            """
        )

    st.divider()

    col3, col4 = st.columns(2)

    with col3:

        st.markdown("### 🛣️ Cool Infrastructure")

        st.write(
            """
            - Use cool pavement materials.
            - Increase shaded pedestrian pathways.
            - Reduce heat-absorbing surfaces.
            """
        )

    with col4:

        st.markdown("### 💧 Water Management")

        st.write(
            """
            - Develop urban water bodies.
            - Improve rainwater harvesting.
            - Preserve natural drainage systems.
            """
        )

    st.divider()

    # Dataset information
    st.subheader("Dataset Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Observations", len(df))

    with col2:
        st.metric(
            "Unique Locations",
            df["location"].nunique()
        )

    with col3:
        st.metric(
            "Area Types",
            df["area_type"].nunique()
        )

    st.divider()

    # Backend integration placeholder
    st.subheader("Data-driven Recommendations")

    st.info(
        """
        Location-specific recommendations based on
        temperature analysis will be generated here
        using the backend analysis module.
        """
    )