class BuildVectorStoreUseCase:
    def __init__(self, loader, splitter, embedding, repo):
        self.loader = loader
        self.splitter = splitter
        self.embedding = embedding
        self.repo = repo

    def execute(self, file_path: str, user_id: str):
        documents = self.loader.load(file_path)
        chunks = self.splitter.split(documents)
        vector_db = self.repo.save(user_id, chunks, self.embedding)
        return vector_db
