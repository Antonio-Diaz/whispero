from langchain.vectorstores import FAISS
import os


class FAISSVectorStoreRepository:

    def __init__(self, allow_dangerous_deserialization: bool = False):
        self.allow_dangerous_deserialization = allow_dangerous_deserialization

    def save(self, user_id, chunks, embedding):
        path = f"db/data/users/{user_id}"
        os.makedirs(path, exist_ok=True)
        db = FAISS.from_documents(chunks, embedding)
        db.save_local(path)
        return db

    def load(self, user_id, embedding):
        path = f"db/data/users/{user_id}"
        return FAISS.load_local(
            path,
            embedding,
            allow_dangerous_deserialization=self.allow_dangerous_deserialization,
        )
