import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate




# Load API keys from environment variables
load_dotenv()
SERPER_API_KEY = os.getenv('SERPER_API_KEY')
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
HF_TOKEN = os.getenv("HF_TOKEN")


def search_articles(query):
    """
    Searches for articles related to the query using Serper API.
    Returns a list of dictionaries containing article URLs, headings, and text.
    """
    
    url="https://google.serper.dev/search?q={}&apiKey={}".format(query,SERPER_API_KEY)
    response = requests.get(url)
    article_links = [link['link'] for link in response.json()['organic'][:5]]   #Total 10 links are retrieved, Im using only 5. More text, more embeddings so more time.
    return article_links


def fetch_article_content(url):
    """
    Fetches the article content, extracting headings and text.
    """
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
    webpage  = requests.get(url,headers=headers).text
    soup = BeautifulSoup(webpage,'html.parser')
    content = ""

    # implementation of fetching headings and content from the articles
    for tag in soup.find_all(['h1','p']):
        content = content + ' ' + tag.text.strip()

    return content.strip()


def concatenate_content(articles):
    """
    Concatenates the content of the provided articles into a single string.
    """
    full_text = ""
    # formatting + concatenation of the string is implemented here
    for article in articles:
        full_text = full_text+ ' ' +article
        full_text = full_text + '\n\n'

    return full_text


def generate_answer(content, query):
    """
    Generates an answer from the concatenated content using GPT-4.
    The content and the user's query are used to generate a contextual answer.
    """
    splitter = RecursiveCharacterTextSplitter(chunk_size = 500,chunk_overlap=50)
    docs = splitter.create_documents([content])

    model_name = "sentence-transformers/all-mpnet-base-v2"
    model_kwargs = {'device': 'cpu'}
    encode_kwargs = {'normalize_embeddings': False}
    embeddings = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs)
    
    db = FAISS.from_documents(docs,embeddings)
    retriever = db.as_retriever()
    llm = ChatGroq(groq_api_key = GROQ_API_KEY, model_name = 'Gemma-7b-it')

    # Create the prompt based on the content and the query
    prompt=ChatPromptTemplate.from_template(
    """
    Generate a detailed, accurate, and concise response to the following query based on the provided context.
    <context>
    {context}
    <context>
    Query:{input}

    """
    )


    # implement openai call logic and get back the response
    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)
    response = rag_chain.invoke({"input": query})
    return response
