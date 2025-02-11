## qwen_model.py 


from langchain.chat_models import init_chat_model
from langchain_ollama import OllamaEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_ollama import OllamaLLM
from langchain_community.llms import Ollama

from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

from typing import List
from langchain_core.documents import Document
from langchain_core.runnables import chain


from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate , AIMessagePromptTemplate , PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

import PyPDF2




class qwen_model():
    def __init__(self, model, temperature , model_provider , embed_model):
        self.model = 'qwen2.5'
        self.model_provider = 'ollama'
        self.temperature = 0 
        self.embed_model = "nomic-embed-text"

    def calling(self , filepath , chuncksize , chunckoverlap , k):
        llm = init_chat_model(model=self.model, model_provider=self.model_provider, temperature=self.temperature)
        embeddings = OllamaEmbeddings(model=self.embed_model)
        vector_store = InMemoryVectorStore(embeddings)
        #return vector_store
    #def pdfloader(vector_store , filepath , chuncksize , chunckoverlap , k):
        loader = PyMuPDFLoader(filepath)
        docs = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chuncksize, chunk_overlap=chunckoverlap, add_start_index=True)
        all_splits = text_splitter.split_documents(docs)
        ids = vector_store.add_documents(documents=all_splits)
        retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": k})
        return llm , ids , retriever

    def apply_template(llm , retriever):
        system_prompt = """
                       You are a information retrieval AI. Format the retrieved information as a table or text
                       Use only the context for your answers, do not make up information
                       {context} 
                        """
        prompt = ChatPromptTemplate.from_messages([
                  ("system", system_prompt),
                  ("human", "{query}"),
                  ])
        rag_chain = ({"context":retriever,"query":RunnablePassthrough()} | prompt  | llm | StrOutputParser())
        return rag_chain

    def response(rag_chain , user_question):
        response = rag_chain.invoke(user_question)
        return response 

    def gui_calling(self):
        llm = init_chat_model(model=self.model, model_provider=self.model_provider, temperature=self.temperature)
        embeddings = OllamaEmbeddings(model=self.embed_model)
        vector_store = InMemoryVectorStore(embeddings)
        return llm , vector_store









