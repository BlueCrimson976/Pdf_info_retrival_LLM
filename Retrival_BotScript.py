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

import markdown


llm = init_chat_model("qwen2.5", model_provider="ollama", temperature=0)

embeddings = OllamaEmbeddings(model="nomic-embed-text")

vector_store = InMemoryVectorStore(embeddings)


filepath = 'Datafiles/Publication606.pdf'
loader = PyMuPDFLoader(filepath)
docs = loader.load()



text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200, add_start_index=True)
all_splits = text_splitter.split_documents(docs)


ids = vector_store.add_documents(documents=all_splits)


retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 3})



system_prompt = """

You are a information retrieval AI. Format the retrieved information as a table or text


Use only the context for your answers, do not make up information

{context} 
"""

# Converts the prompt into a prompt template
prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{query}"),
    ])

rag_chain = ({"context":retriever,"query":RunnablePassthrough()} | prompt  | llm | StrOutputParser())

response = rag_chain.invoke(""" Find the Dispersion Relation of Homogenous Bose Einstein Condenstate """)

print(markdown.markdown(response))
