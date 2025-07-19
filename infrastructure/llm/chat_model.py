from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from config.settings import get_settings

settings = get_settings()


class LangChainQAChain:
    def __call__(self, vectorstore):
        return ConversationalRetrievalChain.from_llm(
            ChatOpenAI(temperature=0, openai_api_key=settings.openai_api_key),
            retriever=vectorstore.as_retriever(),
            return_source_documents=True,
        )
