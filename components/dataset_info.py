import streamlit as st
import pandas as pd


def render_dataset_info(uploaded_file):

    if uploaded_file is None:
        return

    try:
        df = pd.read_csv(uploaded_file)

        st.divider()

        st.subheader("📊 Dataset Information")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Total Records",
                len(df)
            )

        with col2:
            st.metric(
                "Unique Locations",
                df["location"].nunique()
                if "location" in df.columns else "N/A"
            )

        with col3:
            st.metric(
                "Area Types",
                df["area_type"].nunique()
                if "area_type" in df.columns else "N/A"
            )

        st.subheader("Dataset Preview")

        st.dataframe(
            df.head(10),
            use_container_width=True
        )

    except Exception as e:

        st.error(f"Unable to read dataset: {e}")