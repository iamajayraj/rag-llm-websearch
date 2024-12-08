
# LLM-Based Retrieval-Augmented Generation (RAG) System  

This project implements a **Retrieval-Augmented Generation (RAG)** system using a **Large Language Model (LLM)**. The system fetches content from the web, processes it, and generates contextual answers to user queries. It integrates multiple technologies including web scraping, embeddings, API communication, and full-stack development with **Flask** and **Streamlit**.

---

## Features  

1. **End-to-End Query Handling**: Users input their queries through a simple Streamlit-based interface, and the system returns precise, LLM-generated answers.  
2. **Web Search and Content Scraping**: Retrieves top articles related to the query using the **Serper API**, extracts headings and paragraphs, and preprocesses the content.  
3. **LLM-Powered Answer Generation**: Generates context-aware answers using embeddings from **HuggingFace** and **ChatGroq**.  
4. **Seamless API Integration**: Flask backend manages API communication and orchestrates the query processing pipeline.  
5. **Interactive Front-End**: A clean and intuitive Streamlit interface for user interaction.  

---

## Architecture  

### 1. **Streamlit Interface**  
- Allows users to input their queries.  
- Displays the generated answers received from the Flask API.  

### 2. **Flask Backend**  
- Handles the query from the front-end via API calls.  
- Performs the following steps:  
  - Searches for articles using the **Serper API**.  
  - Scrapes and processes article content with **BeautifulSoup**.  
  - Uses embeddings and a retrieval model to generate answers.  

### 3. **Answer Generation Pipeline**  
- **Search Articles**: Retrieves top results for the query using the Serper API.  
- **Scrape Content**: Extracts headings and paragraphs using BeautifulSoup.  
- **Generate Answer**: Uses embeddings, vector search (FAISS), and ChatGroq for LLM-driven answer generation.

---

## Requirements  

To run this project, install the dependencies listed in `requirements.txt`:  

```plaintext
python-dotenv
flask
requests
streamlit
beautifulsoup4
langchain_community
langchain_huggingface
langchain_groq
faiss-cpu
```

Install them with:  
```bash
pip install -r requirements.txt
```

---

## How to Run  

### 1. Set Up Environment Variables  
Create a `.env` file in the project directory with the following keys:  

```plaintext
SERPER_API_KEY=<Your Serper API Key>
GROQ_API_KEY=<Your Groq API Key>
HF_TOKEN=<Your HuggingFace Token>
```

### 2. Start the Flask Backend  
Run the Flask server:  
```bash
python flask_app/app.py
```

### 3. Launch the Streamlit App  
Start the Streamlit front-end:  
```bash
streamlit run streamlit_app/app.py
```

### 4. Interact with the System  
- Enter your query in the Streamlit interface.  
- Receive a contextual, LLM-generated answer.  

---

## Future Enhancements  

- Add support for multi-language queries.  
- Optimize embeddings for faster processing.  
- Expand scraping capabilities to include more sources.  

---

## Acknowledgments  

This project utilizes the following tools and frameworks:  
- [LangChain](https://langchain.com)  
- [HuggingFace](https://huggingface.co)  
- [FAISS](https://faiss.ai)  
- [Streamlit](https://streamlit.io)  
- [Flask](https://flask.palletsprojects.com)  

---
