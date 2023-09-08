import os
import openai
from dotenv import load_dotenv
from langchain.chat_models import AzureChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import AzureSearch
from langchain.document_loaders import DirectoryLoader
from langchain.document_loaders import TextLoader
from langchain.text_splitter import TokenTextSplitter
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate
from azure.search.documents.indexes.models import SearchableField, SimpleField, SearchFieldDataType


# Load environment variables
load_dotenv('.env')


# Configure OpenAI API
openai.api_type = "azure"
openai.api_base ="https://htioaiservice.openai.azure.com/"
openai.api_key = "a4e7007a05654dcc97722d1671249ece"
openai.api_version ="2023-05-15"

# Initialize gpt-35-turbo and our embedding model
llm = AzureChatOpenAI(deployment_name="htiOaiDEP", openai_api_base=openai.api_base,openai_api_key=openai.api_key,openai_api_version=openai.api_version)
embeddings = OpenAIEmbeddings(deployment_id="htiOaiDEPte",openai_api_base=openai.api_base,openai_api_key=openai.api_key,openai_api_version=openai.api_version ,chunk_size=1)

# Connect to Azure Cognitive Search
acs = AzureSearch(azure_search_endpoint="https://hticogservice.search.windows.net",
                 azure_search_key="4AVSwBPXcPmRbdsf4uy19ItWWsZy2AbK4n9wIZcse1AzSeBz6z8D",
                 index_name="app",
                 embedding_function=embeddings.embed_query)



loader = DirectoryLoader("C:\\Users\\acer\\OneDrive\\Desktop\\Final\\chatbot-llm\\data\\App", glob="*.txt", loader_cls=TextLoader, loader_kwargs={'autodetect_encoding': True})
documents = loader.load()
text_splitter = TokenTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

# Add documents to Azure Search
acs.add_documents(documents=docs)

