import streamlit as st
from application.interfaces.chat_history_repository import ChatHistoryRepository


class ChatHistorySessionRepository(ChatHistoryRepository):
    def __init__(self):
        if "chat_histories" not in st.session_state:
            st.session_state.chat_histories = {}

    def get_history(self, user_id: str) -> list:
        return st.session_state.chat_histories.get(user_id, [])

    def save_history(self, user_id: str, history: list) -> None:
        st.session_state.chat_histories[user_id] = history
