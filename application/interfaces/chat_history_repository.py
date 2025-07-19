from abc import ABC, abstractmethod
from typing import List
from domain.entities.chat_turn import ChatTurn


class ChatHistoryRepository(ABC):

    @abstractmethod
    def get_history(self, user_id: str) -> list:
        pass

    @abstractmethod
    def save_history(self, user_id: str, history: list) -> None:
        pass


class ChatHistoryRepository(ABC):
    @abstractmethod
    def get_history(self, user_id: str) -> List[ChatTurn]:
        # Validate or sanitize user_id to prevent path traversal or invalid characters
        user_id = "".join(c for c in user_id if c.isalnum() or c in ("-", "_"))

    @abstractmethod
    def save_history(self, user_id: str, history: List[ChatTurn]) -> None:
        pass
