import streamlit as st
from application.use_cases.session_use_case import SessionUseCase

session_use_case = SessionUseCase()


def render_sidebar():
    st.sidebar.title("📚 Whispero")

    if "user_id" not in st.session_state:
        user_input = st.sidebar.text_input("👤 User ID", key="user_id_input")
        if st.sidebar.button("✅ Confirmar") and user_input:
            st.session_state.user_id = user_input
            session_use_case.create_session(user_input)
            st.sidebar.success(f"Usuario {user_input} confirmado")

    uploaded_file = st.sidebar.file_uploader(
        "📤 Subir archivo", type=["pdf", "docx", "csv"]
    )
    if uploaded_file:
        session_use_case.set_file(uploaded_file.name)
        st.session_state.uploaded_file = uploaded_file
        st.sidebar.success(f"{uploaded_file.name} cargado")

    # 3. Reset
    st.sidebar.markdown("---")
    if st.sidebar.button("🧹 Limpiar sesión"):
        st.session_state.clear()

    return st.session_state.get("uploaded_file", None), st.session_state.get(
        "user_id", None
    )
