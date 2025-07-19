import os
import json
from application.interfaces.chat_history_repository import ChatHistoryRepository

class ChatHistoryFileRepository(ChatHistoryRepository):
    def __init__(self, storage_dir="db/data/chat_histories"):
        self.storage_dir = storage_dir
        os.makedirs(self.storage_dir, exist_ok=True)

    def _get_file_path(self, user_id: str) -> str:
        return os.path.join(self.storage_dir, f"{user_id}.json")

    def get_history(self, user_id: str) -> list:
        path = self._get_file_path(user_id)
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def save_history(self, user_id: str, history: list) -> None:
        path = self._get_file_path(user_id)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(history, f, ensure_ascii=False, indent=2)
