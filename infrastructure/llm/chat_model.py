from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from config.settings import get_settings


class LangChainQAChain:
    def __call__(self, vectorstore):
        settings = get_settings()
        return ConversationalRetrievalChain.from_llm(
            ChatOpenAI(temperature=0, api_key=settings.openai_api_key),
            retriever=vectorstore.as_retriever(),
            return_source_documents=True,
        )
