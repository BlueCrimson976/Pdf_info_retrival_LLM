##app2.py 
import streamlit as st
from langchain_core.messages import HumanMessage , AIMessage  
from langchain.prompts import ChatPromptTemplate
from qwen_model import qwen_model
import PyPDF2
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.output_parsers import StrOutputParser
from langchain.chains import create_retrieval_chain

qm=qwen_model('qwen2.5' , 'ollama' , 0 , "nomic-embed-text")
llm , retriever = qwen_model.gui_calling(self=qm)

st.set_page_config(page_title='PDF Retrival Bot' , page_icon="📖")
st.title("Retriver Bot")

def get_response(query):
        system_prompt = """
                       You are a information retrieval AI. You can answer any question from the given document and can 
                       even retrive any quote or mathematical equation given in the file. Answer the question asked but 
                       say I don't know if you don't know context. 

                       Question : {query}
                        """
        prompt = ChatPromptTemplate.from_messages([("system",system_prompt) , ("human" , "{query}")])
        #document_chain = create_stuff_documents_chain(llm, prompt=prompt)          
        rag_chain =  prompt  | llm | StrOutputParser()
        #rag_chain = create_retrieval_chain(retriever, document_chain)
        return rag_chain.invoke(user_query)

with st.sidebar:
        st.subheader("Your Pdf files")
        filepdf=st.file_uploader("Upload your pdf files here and click proceed" , type='pdf')

        if filepdf is not None:
             pdf_reader = PyPDF2.PdfReader(filepdf)
             content = ""
             for page in range(len(pdf_reader.pages)):
                 content += pdf_reader.pages[page].extract_text()
             text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=500, length_function=len ,add_start_index=True)
             chuncks = text_splitter.split_text(text=content)
             st.write(chuncks)    
      



user_query = st.chat_input('What are you looking for in the paper ? ')
if user_query is not None and user_query != "":
       with st.chat_message("Human"):
        st.markdown(user_query)

       with st.chat_message("AI"):
        #ai_response= get_response(user_query , retriever)
        ai_response = get_response(user_query)
        st.markdown(ai_response)
       
       