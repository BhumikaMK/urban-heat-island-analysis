from components.data_upload import render_data_upload
from components.header import render_header
from components.metric_cards import render_metric_cards
import streamlit as st

from components.sidebar import render_sidebar


# --------------------------------
# PAGE CONFIGURATION
# --------------------------------

st.set_page_config(
    page_title="Urban Heat Island Analysis",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)


# --------------------------------
# CUSTOM CSS
# --------------------------------

st.markdown(
    """
    <style>

    /* Main application */
    .stApp {
        background-color: #F7FAF7;
    }

    /* Main headings */
    h1, h2, h3 {
        color: #234B35;
    }

    /* Metric cards */
    [data-testid="stMetric"] {
        background-color: #EAF2EB;
        padding: 22px;
        border-radius: 14px;
        border: 1px solid #D5E5D8;
    }

    /* Metric values */
    [data-testid="stMetricValue"] {
        color: #234B35;
        font-weight: 700;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #EDF4EE;
    }

    /* Dividers */
    hr {
        border-color: #D5E5D8;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------
# SIDEBAR NAVIGATION
# --------------------------------

selected_page = render_sidebar()


# --------------------------------
# OVERVIEW PAGE
# --------------------------------

if selected_page == "Overview":

    # Header component
    render_header()

    # Temperature metric cards
    render_metric_cards()

    st.divider()

    # Project introduction
    st.subheader("Project Overview")

    st.write(
        """
        Urban Heat Island is a phenomenon in which
        urban areas experience higher temperatures
        than surrounding less-developed areas.

        This application analyses temperature patterns,
        compares built-up and green areas and provides
        environmental insights for sustainable urban planning.
        """
    )

    st.divider()

    # CSV Data Upload
    uploaded_file = render_data_upload()


# --------------------------------
# VISUALIZATIONS PAGE
# --------------------------------

elif selected_page == "Visualizations":

    st.title("📊 Temperature Visualizations")

    st.write(
        "Explore temperature comparisons and trends."
    )

    st.info(
        "Interactive charts will be integrated here."
    )


# --------------------------------
# HEAT MAP PAGE
# --------------------------------

elif selected_page == "Bengaluru Heat Map":

    st.title("🗺️ Bengaluru Heat Map")

    st.write(
        "Explore geographical temperature distribution "
        "across Bengaluru."
    )

    st.info(
        "Geographical visualizations will be integrated here."
    )


# --------------------------------
# RECOMMENDATIONS PAGE
# --------------------------------

elif selected_page == "Recommendations":

    st.title("🌳 Environmental Recommendations")

    st.write(
        "Explore possible interventions for reducing "
        "urban heat."
    )

    st.info(
        "Recommendations will be generated using "
        "the backend analysis."
    )


# --------------------------------
# ABOUT PAGE
# --------------------------------

elif selected_page == "About":

    st.title("About the Project")

    st.write(
        """
        Urban Heat Island Analysis is an environmental
        monitoring project focused on Bengaluru.

        The application aims to analyse temperature
        variations between built-up and green areas
        and support sustainable urban development.
        """
    )