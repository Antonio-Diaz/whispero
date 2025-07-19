from domain.entities.chat_turn import ChatTurn


class AnswerQuestionUseCase:
    """Use case for answering questions based on a user's chat history and vector store."""

    def __init__(self, repo, embedding, llm_chain, chat_history_repo):
        self.repo = repo
        self.embedding = embedding
        self.llm_chain = llm_chain
        self.chat_history_repo = chat_history_repo

    def execute(self, user_id: str, question: str):
        """
        Executes the conversational retrieval use case.
        Since this method modifies persistent chat state, it could be extended to log each
        interaction (question and response) to a dedicated audit trail or external logging service
        for traceability in long-lived or production sessions.
        """
        history = self.chat_history_repo.get_history(user_id)
        chat_history_list = (
            [(turn.user_message, turn.assistant_response) for turn in history]
            if history
            else []
        )

        vectorstore = self.repo.load(user_id, self.embedding)
        chain = self.llm_chain(vectorstore)
        result = chain({"question": question, "chat_history": chat_history_list})

        updated_history = history + [ChatTurn(question, result["answer"])]
        self.chat_history_repo.save_history(user_id, updated_history)

        return result
