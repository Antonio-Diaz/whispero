from langchain.document_loaders import UnstructuredWordDocumentLoader

class DOCXLoader:
    def load(self, path: str):
        return UnstructuredWordDocumentLoader(path).load()