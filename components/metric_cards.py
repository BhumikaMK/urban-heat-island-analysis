import streamlit as st


def render_metric_cards(
    built_up="-- °C",
    green_area="-- °C",
    difference="-- °C"
):

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="🌡️ Built-up Area Temperature",
            value=built_up,
            help="Average temperature of built-up locations."
        )

    with col2:
        st.metric(
            label="🌳 Green Area Temperature",
            value=green_area,
            help="Average temperature of green locations."
        )

    with col3:
        st.metric(
            label="📊 Temperature Difference",
            value=difference,
            help="Temperature difference between the two area types."
        )