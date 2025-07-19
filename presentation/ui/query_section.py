# src/presentation/ui/query_section.py
import streamlit as st
from infrastructure.llm.embeddings_provider import OpenAIEmbeddingsProvider
from infrastructure.vectorstores.faiss_repository import FAISSVectorStoreRepository
from infrastructure.llm.chat_model import LangChainQAChain
from infrastructure.memory.chat_history_file_repository import ChatHistoryFileRepository
from application.use_cases.answer_question_use_case import AnswerQuestionUseCase
from config.settings import get_settings

settings = get_settings()

def render_query_section(user_id):
    embedding = OpenAIEmbeddingsProvider().get()
    repo = FAISSVectorStoreRepository(allow_dangerous_deserialization=settings.allow_dangerous_deserialization)
    chat_history_repo = ChatHistoryFileRepository()
    use_case = AnswerQuestionUseCase(repo, embedding, LangChainQAChain(), chat_history_repo)

    history = chat_history_repo.get_history(user_id)

    for turn in history:
        if isinstance(turn, tuple) and len(turn) == 2:
            st.chat_message("user").markdown(turn[0])
            st.chat_message("assistant").markdown(turn[1])
            

    if prompt := st.chat_input("Haz una pregunta sobre tus archivos..."):
        result = use_case.execute(user_id, prompt)
        st.chat_message("user").markdown(prompt)
        st.chat_message("assistant").markdown(result["answer"])




