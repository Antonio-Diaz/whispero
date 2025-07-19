class AnswerQuestionUseCase:
    def __init__(self, repo, embedding, llm_chain, chat_history_repo):
        self.repo = repo
        self.embedding = embedding
        self.llm_chain = llm_chain
        self.chat_history_repo = chat_history_repo

    def execute(self, user_id: str, question: str):
        history = self.chat_history_repo.get_history(user_id)
        vectorstore = self.repo.load(user_id, self.embedding)
        chain = self.llm_chain(vectorstore)

        result = chain({"question": question, "chat_history": history})
        self.chat_history_repo.save_history(user_id, result["chat_history"])
        return result
