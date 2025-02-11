# How to set up a Local RAG(Only for PDF or any textfile etc)

### There are two ways to create and achieve this : 

#### Prequisite , Download Ollama and LLM model as well as Embedding Model

In ollama , be sure to download both LLM model and some good embedding models , 
LLM models can also be visual model for image processing but... depends on hardware and
not tested. 
Embedding Models also affect the way you get your output. 

Now , back to the two ways to set up Log PDF RAG , 

+ With Anything LLM (Minimal Effort)

+ Creating a web base application using Langchain and Streamlit along with ollama (Highly technical)

Since I have used all local models and not cloud , I need not worry about APIs

### Method 1 : Anything LLM 

+ **Step 1** Do the basic things like pulling ollama models , then click on setting below , open AI providers 

             - Change the LLM and choose ollama and respective LLM model you want to use say Qwen2.5 


             - In Vector Database (this is where your documents will be stored in forms of numbers and matrices) , don't Change LanceDB since it doesn't require API key etc 


             - Go to Embedder , Select provider as ollama and chose the embedding model


             - Go text chuncking and Overlap size and set it accordingly 


             - For web based search go to Agent Skills and turn on web search and select the search engine (Optional)

             - Go to privacy and settings and turn off the data sharing option


        Now , the Overall set up is done , so we shall move to workspace setup now. 

+ **Step 2**  - Create a new workspace 

              - as you hover over it a setting icon will appear press it 

              -  Chat settings ,  provider= Ollama , LLM = your choice , ChatMode = Query (for RAG) , LLM_Temperature = 0 (for most consice response) [The higher the number i.e. closer to 1 , more the creativity of the model , temperature controls the creativity of the model] , You can customize the prompt too , the default is very good. (optional , technical)

              - Go to vector database , Search preference=Accurately Optimized , Document_threshold_Similary = According to your preference 

              - Agent Configuration - Ollama (Optional , technical)

          Now , the last step , to load the docs! 

+ **Step 3** - As you hover over workspace press the upload icon 

             - In Documents toggle tab, upload your document (pdf etc) , then 

             - move it to workspace and click on save and embed 

             - After the file embedded , select on the pin icon (IMP) [if you don't pin this won't work , most IMP step] 

             - Go back and feel free to chat with the pdf or text docs as much as you want. 

So , this is the most easiest and less time consuming method , so you don't have to waste 4 days to create a RAG , but use your private RAG Application , though one must play and have knowledge foundation to judge the accuracy of this and even to combine or adjust the parameter to get a better response.  
             