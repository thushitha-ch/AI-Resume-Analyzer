# AI Resume Analyzer

An AI-powered Resume Analyzer built using **FastAPI**, **Streamlit**, **LangChain**, **ChromaDB**, **HuggingFace Embeddings**, and **Groq LLM**.

## Features

- Upload a PDF resume
- Extract resume text using PyPDFLoader
- Generate embeddings using HuggingFace
- Store embeddings in ChromaDB
- Retrieve relevant resume information using RAG
- Analyze resumes using Groq Llama 3.3 70B
- Display AI-generated resume insights through Streamlit

## Technologies Used

- Python
- FastAPI
- Streamlit
- LangChain
- ChromaDB
- HuggingFace Embeddings
- Groq LLM
- PyPDF

## Installation

Clone the repository:

```bash
git clone https://github.com/thushitha-ch/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
```

Install the required packages:

```bash
pip install fastapi uvicorn streamlit requests
pip install langchain langchain-core langchain-community
pip install langchain-chroma langchain-text-splitters
pip install langchain-huggingface langchain-groq
pip install sentence-transformers
pip install python-multipart
pip install pypdf
```

## Configure Groq API Key

Open **be.py** and replace:

```python
api_key="YOUR_GROQ_API_KEY"
```

with your own Groq API key.

## Run the Backend

```bash
python -m uvicorn be:fast_api_obj --reload
```

## Run the Frontend

Open another terminal and run:

```bash
python -m streamlit run fe.py
```

## Project Files

- **be.py** – FastAPI backend with RAG pipeline and Groq LLM integration.
- **fe.py** – Streamlit frontend for uploading resumes and displaying analysis.

## Output

The application generates:

- Candidate Summary
- Education
- Technical Skills
- Experience
- Projects
- Certifications
- Strengths
- Weaknesses
- Suitable Job Roles
- Resume Score
- Resume Improvement Suggestions

## Author

**Thushitha Changana**

GitHub: https://github.com/thushitha-ch
