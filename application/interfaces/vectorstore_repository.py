from abc import ABC, abstractmethod

class VectorStoreRepository(ABC):
    @abstractmethod
    def save(self, user_id: str, chunks, embedding):
        pass

    @abstractmethod
    def load(self, user_id: str, embedding):
        pass