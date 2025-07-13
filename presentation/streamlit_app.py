import streamlit as st

from presentation.ui.query_section import render_query_section
from presentation.ui.upload_section import render_upload_section
from presentation.ui.annotations_section import render_annotation_section
from presentation.ui.sidebar import render_sidebar


def render_header():
    st.set_page_config(page_title="Whispero", page_icon=":microphone:", layout="wide")
    st.markdown("## Whispero: Your Personal Whisper Assistant")
    st.markdown(
        """
        Welcome to Whispero! This is your personal assistant for managing and querying your files.
        Please confirm your user ID to get started.
        """
    )


def render_footer():
    st.markdown("---")
    st.caption("Made with ❤️ by Jose")


def run():
    render_header()

    uploaded_file, user_id = render_sidebar()

    if user_id and uploaded_file:
        st.title("📄 Vista del documento")
        render_upload_section(uploaded_file, user_id)

        st.markdown("## 📌 Anotaciones")
        render_annotation_section(user_id, uploaded_file.name)

        st.markdown("## 💬 Consulta")
        query = st.text_input("Haz una pregunta:")
        if query:
            render_query_section(user_id, query)

    render_footer()
