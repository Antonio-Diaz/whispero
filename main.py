import streamlit as st

from presentation.ui.sidebar import sidebar
from presentation.ui.upload_section import render_upload_section
from presentation.ui.query_section import render_query_section
from presentation.ui.annotations_section import render_annotation_section


def main():
    st.set_page_config(page_title="Whispero", page_icon="🧠", layout="wide")

    uploaded_file, user_id = sidebar()

    if uploaded_file and user_id:
        if st.session_state.get("processed_file") != uploaded_file.name:
            render_upload_section(uploaded_file, user_id)
            st.session_state.processed_file = uploaded_file.name

        col1, col2 = st.columns([1, 2])
        with col1:
            st.subheader("📝 Resumen del archivo")
            st.write(f"**{uploaded_file.name}** cargado.")
            if uploaded_file.name.lower().endswith(".csv"):
                import pandas as pd

                uploaded_file.seek(0)
                df = pd.read_csv(uploaded_file)
                st.dataframe(df.head())
            render_annotation_section(user_id, uploaded_file.name)

        with col2:
            render_query_section(user_id)
    else:
        st.info("Confirma tu User ID y sube un archivo para comenzar.")


if __name__ == "__main__":
    main()
