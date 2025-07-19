from abc import ABC, abstractmethod
from typing import List

from domain.entities.chat_turn import ChatTurn


class ChatHistoryRepository(ABC):
    """Interface for persisting and retrieving chat history."""

    @abstractmethod
    def get_history(self, user_id: str) -> List[ChatTurn]:
        """Return the stored chat history for ``user_id``."""
        pass

    @abstractmethod
    def save_history(self, user_id: str, history: List[ChatTurn]) -> None:
        """Persist the chat ``history`` for ``user_id``."""
        pass
