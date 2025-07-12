from langchain.embeddings import OpenAIEmbeddings

class OpenAIEmbeddingsProvider:
    def get(self):
        return OpenAIEmbeddings()