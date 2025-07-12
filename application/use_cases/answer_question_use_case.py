class AnswerQuestionUseCase:
    def __init__(self, repo, embedding, llm_chain):
        self.repo = repo
        self.embedding = embedding
        self.llm_chain = llm_chain

    def execute(self, user_id: str, question: str):
        vectorstore = self.repo.load(user_id, self.embedding)
        chain = self.llm_chain(vectorstore)
        return chain({"question": question, "chat_history": []})