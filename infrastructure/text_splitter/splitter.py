from langchain.text_splitter import RecursiveCharacterTextSplitter


class Splitter:
    def split(self, documents):
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        return splitter.split_documents(documents)
