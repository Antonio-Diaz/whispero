from typing import Optional


class Document:
    def __init__(self, content: str, metadata: Optional[dict] = None):
        self.content = content
        self.metadata = metadata or {}
