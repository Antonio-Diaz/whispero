"""UI components for the application sidebar."""

import streamlit as st
from application.use_cases.session_use_case import SessionUseCase

session_use_case = SessionUseCase()


def sidebar():
    """Render the application sidebar.

    Returns
    -------
    tuple
        Uploaded file and confirmed user ID if available.
    """

    with st.sidebar:
        st.markdown("## 🧠 Whispero")
        st.markdown("---")

        user_id = st.session_state.get("user_id")
        if not user_id:
            user_input = st.text_input("👤 User ID")
            if st.button("✅ Confirmar") and user_input:
                st.session_state.user_id = user_input
                session_use_case.create_session(user_input)
                user_id = user_input
                st.success(f"Usuario {user_input} confirmado")
        else:
            st.write(f"**Usuario:** {user_id}")

        uploaded_file = st.file_uploader(
            "📤 Subir archivo", type=["pdf", "docx", "csv"]
        )
        if uploaded_file:
            session_use_case.set_file(uploaded_file.name)
            st.session_state.uploaded_file = uploaded_file
            st.success(f"{uploaded_file.name} cargado")

        st.markdown("---")
        if st.button("🧹 Limpiar sesión"):
            st.session_state.clear()

        st.markdown("### ⚡ Acciones rápidas")
        st.info("Espacio reservado para acciones rápidas")

    return (
        st.session_state.get("uploaded_file"),
        st.session_state.get("user_id"),
    )


# Backwards compatibility
render_sidebar = sidebar
