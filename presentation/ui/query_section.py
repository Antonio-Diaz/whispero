import streamlit as st
from infrastructure.llm.embeddings_provider import OpenAIEmbeddingsProvider
from infrastructure.vectorstores.faiss_repository import FAISSVectorStoreRepository
from infrastructure.llm.chat_model import LangChainQAChain
from infrastructure.memory.chat_history_file_repository import (
    ChatHistoryFileRepository,
)
from application.use_cases.answer_question_use_case import AnswerQuestionUseCase
from config.settings import get_settings

settings = get_settings()


def render_query_section(user_id):
    embedding = OpenAIEmbeddingsProvider().get()
    repo = FAISSVectorStoreRepository(
        allow_dangerous_deserialization=settings.allow_dangerous_deserialization
    )
    chat_history_repo = ChatHistoryFileRepository()
    use_case = AnswerQuestionUseCase(
        repo, embedding, LangChainQAChain(), chat_history_repo
    )

    # Captura input tipo chat
    if "pending_question" not in st.session_state:
        st.session_state.pending_question = None

    prompt = st.chat_input("Haz una pregunta sobre tus archivos...")
    if prompt:
        st.session_state.pending_question = prompt

    if st.session_state.pending_question:
        result = use_case.execute(user_id, st.session_state.pending_question)
        st.session_state.pending_question = None

    # Mostrar historial tipo chat
    history = chat_history_repo.get_history(user_id)
    for turn in history[-20:]:  # Limita los últimos 20 turnos para mejorar rendimiento
        st.chat_message("user").markdown(turn.user_message)
        st.chat_message("assistant").markdown(turn.assistant_response)
