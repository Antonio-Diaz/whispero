from infrastructure.llm.embeddings_provider import OpenAIEmbeddingsProvider
from infrastructure.vectorstores.faiss_repository import FAISSVectorStoreRepository
from infrastructure.llm.chat_model import LangChainQAChain
from application.use_cases.answer_question_use_case import AnswerQuestionUseCase
import streamlit as st
from config.settings import get_settings
settings = get_settings()


def render_query_section(user_id, query):
    embedding = OpenAIEmbeddingsProvider().get()
    repo = FAISSVectorStoreRepository(allow_dangerous_deserialization=settings.allow_dangerous_deserialization)
    answer_use_case = AnswerQuestionUseCase(repo, embedding, LangChainQAChain())
    result = answer_use_case.execute(user_id, query)
    st.write("🧾 Answer:", result["answer"])