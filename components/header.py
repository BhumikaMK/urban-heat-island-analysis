import streamlit as st


def render_header():

    st.title("🌿 Urban Heat Island Analysis")

    st.subheader(
        "Bengaluru Urban Heat Monitoring Dashboard"
    )

    st.caption(
        "Monitor temperature variations between "
        "built-up and green areas across Bengaluru."
    )

    st.divider()