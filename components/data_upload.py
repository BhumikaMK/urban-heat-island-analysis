import streamlit as st


def render_data_upload():

    st.subheader("📂 Upload Temperature Dataset")

    st.write(
        "Upload a CSV file containing temperature "
        "and location information for analysis."
    )

    uploaded_file = st.file_uploader(
        "Choose your CSV file",
        type=["csv"],
        help="Upload a CSV dataset containing urban temperature data.",
        key="temperature_dataset"
    )

    if uploaded_file is not None:

        st.success("Dataset uploaded successfully!")

        col1, col2 = st.columns(2)

        with col1:
            st.write("**File name:**")
            st.write(uploaded_file.name)

        with col2:
            st.write("**File size:**")
            st.write(f"{uploaded_file.size / 1024:.2f} KB")

    return uploaded_file