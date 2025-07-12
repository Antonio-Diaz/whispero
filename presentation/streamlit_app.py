import streamlit as st
from presentation.ui.upload_section import render_upload_section
from presentation.ui.query_section import render_query_section

st.title("🧠 TalkingWithYourFiles")
user_id = st.text_input("Enter User ID")

uploaded_file = st.file_uploader("Upload your file", type=["pdf", "docx", "csv"])
if uploaded_file and user_id:
    render_upload_section(uploaded_file, user_id)

query = st.text_input("Ask a question about your files:")
if query and user_id:
    render_query_section(user_id, query)