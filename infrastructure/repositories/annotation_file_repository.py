import json
from pathlib import Path
from typing import List
from datetime import datetime

from domain.entities.annotation import Annotation
from application.interfaces.annotation_repository import AnnotationRepository


class AnnotationFileRepository(AnnotationRepository):

    def __init__(self, base_path="app/data/users"):
        self.base_path = Path(base_path)

    def _file_path(self, user_id: str):
        return self.base_path / user_id / "annotations.json"

    def save(self, user_id: str, annotation: Annotation):
        path = self._file_path(user_id)
        path.parent.mkdir(parents=True, exist_ok=True)

        annotations = []
        if path.exists():
            annotations = json.loads(path.read_text())

        annotations.append(
            {
                "doc_name": annotation.doc_name,
                "selected_text": annotation.selected_text,
                "note": annotation.note,
                "created_at": annotation.created_at.isoformat(),
            }
        )

        path.write_text(json.dumps(annotations, indent=2))

    def load_by_document(self, user_id: str, doc_name: str) -> List[Annotation]:
        path = self._file_path(user_id)
        if not path.exists():
            return []

        raw = json.loads(path.read_text())
        return [
            Annotation(
                **{
                    "doc_name": a["doc_name"],
                    "selected_text": a["selected_text"],
                    "note": a["note"],
                    "created_at": datetime.fromisoformat(a["created_at"]),
                }
            )
            for a in raw
            if a["doc_name"] == doc_name
        ]
