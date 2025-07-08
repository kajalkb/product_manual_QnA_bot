import streamlit as st
import pdfplumber
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
#from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
import os

# Streamlit UI
st.title("Product Manual Q&A Bot")

uploaded_file = st.file_uploader("Upload a Product Manual PDF", type="pdf")

# Initialize embedding model
embeddings = OpenAIEmbeddings()

if uploaded_file is not None:
    # Extract text from PDF
    with pdfplumber.open(uploaded_file) as pdf:
        full_text = "\n".join(page.extract_text() or "" for page in pdf.pages)

    # Split text into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = splitter.split_text(full_text)

    # Create FAISS vector store (in memory)
    vectordb = FAISS.from_texts(chunks, embedding=embeddings)


    # Create or load vector store
    # db_dir = "./chroma_store"
    # vectordb = Chroma.from_texts(chunks, embedding=embeddings, persist_directory=db_dir)
    # vectordb.persist()

    # Setup retriever
    retriever = vectordb.as_retriever()

    # Setup Retrieval QA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(temperature=0),
        chain_type="stuff",
        retriever=retriever
    )

    # Input and display answer
    question = st.text_input("Ask a question about the manual:")
    if question:
        answer = qa_chain.run(question)
        st.write("Answer: ", answer)
