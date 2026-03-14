import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_core.output_parsers import StrOutputParser


from dotenv import load_dotenv
load_dotenv()

os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")
os.environ['HF_TOKEN'] = os.getenv('HF_TOKEN')

groq_api_key = os.getenv('GROQ_API_KEY')

llm =ChatGroq(model='openai/gpt-oss-120b',api_key=groq_api_key)

prompt = ChatPromptTemplate.from_template(
    """
        Answer the questions based on the provided contexxt only.
        Please provide the most accurate response based on the question
        <context>
        {context}
        <context>
        Question:{input}
    """
)

def create_vector_embedding():
    if "vectors" not in st.session_state:
        st.session_state.embeddings = HuggingFaceEmbeddings(model="all-MiniLM-L6-v2")
        st.session_state.loader = PyPDFDirectoryLoader("research_papers")   ## Data Ingestion
        st.session_state.docs = st.session_state.loader.load()
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
        st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs)
        st.session_state.vectors = FAISS.from_documents(st.session_state.final_documents,st.session_state.embeddings)

st.title("RAG Document Q&A with Groq and Llama3")
user_prompt = st.text_input("Enter your query from the research paper")

if st.button("Document Embedding"):
    create_vector_embedding()
    st.write("Vector Database is ready")

import time
output_parser = StrOutputParser()
if user_prompt:

    if "vectors" not in st.session_state:
        st.warning("Please click 'Document Embedding' first.")
        st.stop()

    retriver = st.session_state.vectors.as_retriever()
    docs = retriver.invoke(user_prompt)
    context = "\n".join([doc.page_content for doc in docs])
    chain = prompt | llm | output_parser
    start = time.process_time()
    response = chain.invoke({"context":context,"input":user_prompt})
    print(f"response time :{time.process_time() - start}")

    st.write(response)

    ## With a streamlit expander
    with st.expander("Document similarity search"):
        for i,doc in enumerate(docs):
            st.write(doc.page_content)
            st.write('----------------------')

