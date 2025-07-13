from dataclasses import dataclass
from datetime import datetime


@dataclass
class Annotation:
    doc_name: str
    selected_text: str
    note: str
    created_at: datetime
