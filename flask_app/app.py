
from flask import Flask,request,jsonify
import utils
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Load API keys from environment variables
load_dotenv()
SERPER_API_KEY = os.getenv('SERPER_API_KEY')
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
HF_TOKEN = os.getenv("HF_TOKEN")


@app.route('/query', methods=['POST'])
def query():
    """
    Handles the POST request to '/query'. Extracts the query from the request,
    processes it through the search, concatenate, and generate functions,
    and returns the generated answer.
    """
    # get the data/query from streamlit app
    query = request.get_json()['query']
    
    # Step 1: Search and scrape articles based on the query
    links = utils.search_articles(query)
    articles_content_list = [utils.fetch_article_content(link) for link in links]
    
    # Step 2: Concatenate content from the scraped articles
    text = utils.concatenate_content(articles_content_list)   

    # Step 3: Generate an answer using the LLM
    response= utils.generate_answer(text,query)

    # return the jsonified text back to streamlit
    return jsonify({'answer':response['answer']})

if __name__ == '__main__':
    app.run(host='localhost', port=5001,debug=True)
