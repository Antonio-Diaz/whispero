import tempfile
import os
import streamlit as st
from infrastructure.file_loaders import pdf_loader, docx_loader, csv_loader
from infrastructure.text_splitter.splitter import Splitter
from infrastructure.llm.embeddings_provider import OpenAIEmbeddingsProvider
from infrastructure.vectorstores.faiss_repository import FAISSVectorStoreRepository
from application.use_cases.build_vectorstore_use_case import BuildVectorStoreUseCase
from config.settings import get_settings

settings = get_settings()


def render_upload_section(uploaded_file, user_id):
    extension = uploaded_file.name.split(".")[-1].lower()
    loader_map = {
        "pdf": pdf_loader.PDFLoader(),
        "docx": docx_loader.DOCXLoader(),
        "csv": csv_loader.CSVLoader(),
    }

    if extension not in loader_map:
        st.error(f"Unsupported file type: .{extension}")
        return

    try:
        with tempfile.NamedTemporaryFile(
            delete=False, suffix=f".{extension}"
        ) as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_file_path = tmp_file.name

        loader = loader_map[extension]
        splitter = Splitter()
        embedding = OpenAIEmbeddingsProvider().get()
        repo = FAISSVectorStoreRepository(
            allow_dangerous_deserialization=settings.allow_dangerous_deserialization
        )

        use_case = BuildVectorStoreUseCase(loader, splitter, embedding, repo)
        use_case.execute(tmp_file_path, user_id)

        st.success("✅ Vector store updated successfully!")

    except Exception as e:
        st.error(f"❌ Error processing file: {str(e)}")

    finally:
        if os.path.exists(tmp_file_path):
            os.remove(tmp_file_path)
