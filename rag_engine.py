import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

def process_pdf_and_create_rag(pdf_path):
    # 1. Load the PDF
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    
    # 2. Split the text into manageable chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(documents)
    
    # 3. Create LOCAL Ollama Embeddings (Using the dedicated embedding model)
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vectorstore = Chroma.from_documents(documents=chunks, embedding=embeddings)
    
    # 4. Initialize the LOCAL Ollama LLM (Using the dedicated generative model)
    llm = Ollama(model="llama3.2", temperature=0)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    
    # 5. Create the Prompt Template
    prompt = ChatPromptTemplate.from_template(
        """You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know.
        
        Context: {context}
        
        Question: {question}
        
        Helpful Answer:"""
    )
    
    # 6. Build the RAG Chain using LCEL (Modern LangChain Syntax)
    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    return rag_chain, retriever

def ask_question(rag_chain, retriever, question):
    answer = rag_chain.invoke(question)
    source_docs = retriever.invoke(question)
    return answer, source_docs
