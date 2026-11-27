import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.markdown(
            """
            <h2 style="color:#2E8B57;">
                🌿 Urban Heat
            </h2>
            <p style="color:gray;">
                Island Analysis
            </p>
            """,
            unsafe_allow_html=True
        )

        st.divider()

        st.markdown("### Navigation")

        selected_page = st.radio(
            "Go to",
            [
                "Overview",
                "Visualizations",
                "Bengaluru Heat Map",
                "Recommendations",
                "About"
            ],
            label_visibility="collapsed"
        )

        st.divider()

        st.caption("Urban Heat Island Analysis")
        st.caption("Bengaluru, Karnataka")

        return selected_page