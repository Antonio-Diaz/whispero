from application.interfaces.annotation_repository import AnnotationRepository
from domain.entities.annotation import Annotation
from typing import List
from datetime import datetime


class AnnotationUseCase:
    def __init__(self, repository: AnnotationRepository):
        self.repository = repository

    def add_annotation(
        self, user_id: str, doc_name: str, selected_text: str, note: str
    ):
        annotation = Annotation(
            doc_name=doc_name,
            selected_text=selected_text,
            note=note,
            created_at=datetime.now(),
        )
        self.repository.save(user_id, annotation)

    def get_annotations(self, user_id: str, doc_name: str) -> List[Annotation]:
        return self.repository.load_by_document(user_id, doc_name)
