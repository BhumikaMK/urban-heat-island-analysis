import streamlit as st


def render_about_page():

    st.title("🌿 About the Project")

    st.caption(
        "Understanding and analysing Urban Heat Island "
        "effects across Bengaluru."
    )

    st.divider()

    # Project Introduction
    st.subheader("Project Introduction")

    st.write(
        """
        Urban Heat Island Analysis is an environmental
        monitoring project focused on understanding
        temperature variations across Bengaluru.

        Urban areas often experience higher temperatures
        than surrounding green spaces due to buildings,
        roads, reduced vegetation and human activities.

        This project aims to analyse these variations
        and provide insights that support sustainable
        urban planning.
        """
    )

    st.divider()

    # Objectives
    st.subheader("Project Objectives")

    objectives = [
        "Analyse temperature variations across Bengaluru.",
        "Compare built-up areas and green spaces.",
        "Visualise geographical temperature distribution.",
        "Identify areas experiencing higher temperatures.",
        "Provide environmental recommendations."
    ]

    for objective in objectives:
        st.markdown(f"- {objective}")

    st.divider()

    # Project Scope
    st.subheader("Project Scope")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📊 Data Analysis")

        st.write(
            """
            Processing temperature datasets,
            identifying patterns and comparing
            different types of urban areas.
            """
        )

    with col2:
        st.markdown("### 🗺️ Geographical Analysis")

        st.write(
            """
            Mapping temperature observations
            and exploring geographical
            temperature distribution.
            """
        )

    st.divider()

    # Technology Stack
    st.subheader("Technology Stack")

    technologies = [
        "Python",
        "Streamlit",
        "Pandas",
        "Plotly",
        "Folium"
    ]

    cols = st.columns(len(technologies))

    for col, technology in zip(cols, technologies):

        with col:
            st.info(technology)

    st.divider()

    st.caption(
        "Urban Heat Island Analysis | Bengaluru, Karnataka"
    )