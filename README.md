
# Product Manual Q&A Bot

A simple Streamlit app that lets users upload a product manual (PDF) and ask natural language questions about its content — powered by OpenAI and FAISS vector search.

---

## 🔍 Features

- Semantic search over uploaded product manuals
- PDF text extraction + chunking
- FAISS in-memory vector store
- Natural question answering with GPT
- Clean and interactive Streamlit interface
- Deployable on Hugging Face Spaces

---

## 📸 Demo

[Live Demo on Hugging Face Spaces](https://huggingface.co/spaces/your-username/product-manual-bot)


---

## Tech Stack

| Layer | Tools |
|-------|-------|
| Embedding | `OpenAIEmbeddings` |
| Vector Store | `FAISS` |
| LLM | `ChatOpenAI` |
| UI | `Streamlit` |
| PDF Parsing | `pdfplumber` |

---

## How to Run Locally

### 1. Clone this repo

git clone https://github.com/kajalkb/product-manual-qa-bot.git

cd product-manual-qa-bot


### 2. Install Dependencies

pip install -r requirements.txt

### 3. Set your OpenAI API key

export OPENAI_API_KEY=your-openai-api-key (Alternatively, use .env file or Hugging Face Secrets)

### 4. Run the app

streamlit run app.py


## How it works

1. PDF is uploaded and parsed with pdfplumber

2. Text is split into chunks using RecursiveCharacterTextSplitter

3. Chunks are embedded using OpenAIEmbeddings

4. A FAISS vector store is built on the fly

5. User question is processed through RetrievalQA using GPT

