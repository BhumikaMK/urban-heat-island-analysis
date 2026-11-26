import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Urban Heat Island Analysis",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Application title
st.title("🌍 Urban Heat Island Analysis")

st.markdown("""
### Bengaluru Urban Heat Monitoring Dashboard

Analyse temperature variations between built-up
and green areas to understand the Urban Heat Island effect.
""")

st.divider()

# Dashboard metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Built-up Area Temperature", "-- °C")

with col2:
    st.metric("Green Area Temperature", "-- °C")

with col3:
    st.metric("Temperature Difference", "-- °C")

st.divider()

# Project introduction
st.subheader("About the Project")

st.write("""
This application analyses urban temperature patterns
across Bengaluru.

It compares built-up and green areas, visualises
temperature variations and provides environmental
insights to support sustainable urban planning.
""")

# Dataset upload
st.subheader("Upload Temperature Dataset")

uploaded_file = st.file_uploader(
    "Choose a CSV file",
    type=["csv"]
)

if uploaded_file:
    st.success("File uploaded successfully!")