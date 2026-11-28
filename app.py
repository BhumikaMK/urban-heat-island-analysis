from components.dataset_info import render_dataset_info
from components.data_upload import render_data_upload
from components.dataset_summary import render_dataset_summary
from components.header import render_header
from utils.validation import validate_csv
from components.about_page import render_about_page
from components.recommendations_page import render_recommendations_page
from components.heat_map_page import render_heat_map_page
from components.visualization_page import render_visualization_page
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
# SESSION STATE INITIALIZATION
# --------------------------------

if "validated_df" not in st.session_state:
    st.session_state["validated_df"] = None

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

    if uploaded_file is not None:

        df, errors = validate_csv(uploaded_file)

        if errors:

            st.session_state["validated_df"] = None

            st.error("Dataset validation failed.")

            for error in errors:
                st.warning(error)

        else:

            st.success("Dataset validation successful!")

            st.session_state["validated_df"] = df

            render_dataset_info(uploaded_file)

            render_dataset_summary(df)


    # Session State verification

    if st.session_state.get("validated_df") is not None:

        st.success("Dataset is available in session memory.")

        st.write(
            "Stored records:",
            len(st.session_state["validated_df"])
        )

# --------------------------------
# VISUALIZATIONS PAGE
# --------------------------------

elif selected_page == "Visualizations":

    df = st.session_state.get("validated_df")

    render_visualization_page(df)

# --------------------------------
# HEAT MAP PAGE
# --------------------------------

elif selected_page == "Bengaluru Heat Map":

    df = st.session_state.get("validated_df")

    render_heat_map_page(df)

# --------------------------------
# RECOMMENDATIONS PAGE
# --------------------------------

elif selected_page == "Recommendations":

    df = st.session_state.get("validated_df")

    render_recommendations_page(df)

# --------------------------------
# ABOUT PAGE
# --------------------------------

elif selected_page == "About":

    render_about_page()