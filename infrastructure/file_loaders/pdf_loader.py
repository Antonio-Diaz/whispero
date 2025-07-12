from langchain.document_loaders import PyPDFLoader

class PDFLoader:
    def load(self, path: str):
        return PyPDFLoader(path).load()
