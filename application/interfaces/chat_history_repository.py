from abc import ABC, abstractmethod


class ChatHistoryRepository(ABC):
    
    @abstractmethod
    def get_history(self, user_id: str) -> list:
        pass

    @abstractmethod
    def save_history(self, user_id: str, history: list) -> None:
        pass

class ChatHistoryFileRepository(ABC):

    @abstractmethod
    def _get_file_path(self, user_id: str) -> str:
        pass

    @abstractmethod
    def get_history(self, user_id: str) -> list:
        pass

    @abstractmethod
    def save_history(self, user_id: str, history: list) -> None:
        pass

