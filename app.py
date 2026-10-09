import streamlit as st
from rag_engine import process_pdf_and_create_rag, ask_question
import tempfile
import os

st.set_page_config(page_title="RAG Assistant", page_icon="📄")
st.title("📄 Free RAG Document Assistant")
st.markdown("Powered by Llama 3 (Groq) & Local Hugging Face Embeddings. Upload a PDF and ask questions!")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    if "rag_chain" not in st.session_state:
        with st.spinner("Processing PDF and building knowledge graph... (First time may take a minute to download local models)"):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                tmp_file.write(uploaded_file.getvalue())
                tmp_path = tmp_file.name
            
            st.session_state.rag_chain, st.session_state.retriever = process_pdf_and_create_rag(tmp_path)
            os.unlink(tmp_path)
            st.success("PDF processed successfully! You can now ask questions.")

    if "rag_chain" in st.session_state:
        user_question = st.chat_input("Ask a question about the PDF...")
        
        if user_question:
            st.chat_message("user").write(user_question)
            
            with st.spinner("Thinking..."):
                answer, sources = ask_question(st.session_state.rag_chain, st.session_state.retriever, user_question)
                
            st.chat_message("assistant").write(answer)
            
            with st.expander("See Source Documents"):
                for i, doc in enumerate(sources):
                    st.write(f"**Source {i+1} (Page {doc.metadata.get('page', 'Unknown')}):**")
                    st.write(doc.page_content[:500] + "...")
