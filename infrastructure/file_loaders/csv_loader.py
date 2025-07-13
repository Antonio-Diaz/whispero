from langchain.document_loaders import CSVLoader


class CSVLoader:
    def load(self, path: str):
        return CSVLoader(path).load()
