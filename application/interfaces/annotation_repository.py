from abc import ABC, abstractmethod
from typing import List
from domain.entities.annotation import Annotation


class AnnotationRepository(ABC):

    @abstractmethod
    def save(self, user_id: str, annotation: Annotation):
        pass

    @abstractmethod
    def load_by_document(self, user_id: str, doc_name: str) -> List[Annotation]:
        pass
