import os
import json
from application.interfaces.chat_history_repository import ChatHistoryRepository
from domain.entities.chat_turn import ChatTurn
from typing import List


class ChatHistoryFileRepository(ChatHistoryRepository):
    """
    File-based implementation of the ChatHistoryRepository.
    This class should be injected at a higher level (e.g. via a factory or settings config),
    so it can be swapped with an in-memory or database-backed implementation without changing use cases.
    """

    def __init__(self, storage_dir="db/data/chat_histories"):
        self.storage_dir = storage_dir
        os.makedirs(self.storage_dir, exist_ok=True)

    def _get_file_path(self, user_id: str) -> str:
        return os.path.join(self.storage_dir, f"{user_id}.json")

    def get_history(self, user_id: str) -> List[ChatTurn]:
        path = self._get_file_path(user_id)
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                raw = json.load(f)
                return [ChatTurn(**turn) for turn in raw]
        return []

    def save_history(self, user_id: str, history: List[ChatTurn]) -> None:
        path = self._get_file_path(user_id)
        serializable = [turn.__dict__ for turn in history]
        with open(path, "w", encoding="utf-8") as f:
            json.dump(serializable, f, ensure_ascii=False, indent=2)
