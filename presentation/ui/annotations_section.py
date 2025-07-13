import streamlit as st
from infrastructure.repositories.annotation_file_repository import (
    AnnotationFileRepository,
)
from application.use_cases.annotation_use_case import AnnotationUseCase


def render_annotation_section(user_id: str, doc_name: str):
    st.subheader("📌 Añadir Anotación")

    selected_text = st.text_area("Fragmento del documento")
    note = st.text_input("Comentario")

    repo = AnnotationFileRepository()
    use_case = AnnotationUseCase(repo)

    if st.button("Guardar anotación") and selected_text and note:
        use_case.add_annotation(user_id, doc_name, selected_text, note)
        st.success("Anotación guardada")

    st.subheader("📖 Anotaciones guardadas")
    annotations = use_case.get_annotations(user_id, doc_name)

    for ann in annotations:
        st.markdown(
            f"**{ann.selected_text}**\n\n📝 _{ann.note}_\n\n🕒 {ann.created_at.strftime('%Y-%m-%d %H:%M')}"
        )
