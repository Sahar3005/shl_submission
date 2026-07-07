# SHL Conversational Assessment Recommendation Agent

## Overview

The SHL Conversational Assessment Recommendation Agent is a FastAPI-based AI service that recommends relevant SHL assessments based on hiring requirements.

The application uses semantic search with Sentence Transformers and FAISS to retrieve the most relevant assessments from the official SHL Product Catalog. It also supports clarification questions, assessment comparison, and safe handling of off-topic or invalid requests.

---

## Features

- FastAPI REST API
- GET /health endpoint
- POST /chat endpoint
- Semantic search using Sentence Transformers
- FAISS vector similarity search
- SHL Product Catalog integration
- Clarification questions for incomplete hiring requirements
- Assessment comparison
- Off-topic request handling
- Prompt injection protection

---

## Tech Stack

- Python 3.10
- FastAPI
- Uvicorn
- Sentence Transformers
- FAISS
- NumPy
- Pydantic

---

## Project Structure

```
shl_sadaf/
│
├── app.py
├── README.md
├── requirements.txt
├── test.py
│
├── data/
│   ├── shl_product_catalog.json
│   ├── embeddings.npy
│   └── faiss.index
│
├── models/
│   └── schemas.py
│
├── routes/
│   └── chat.py
│
├── services/
│   ├── compare.py
│   ├── conversation.py
│   ├── embeddings.py
│   ├── recommendation.py
│   └── retrieval.py
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/shl-conversational-agent.git
```

Move into the project directory

```bash
cd shl-conversational-agent
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Generate Embeddings

If embeddings are not already available, generate them using:

```bash
python services/embeddings.py
```

---

## Run the Application

```bash
uvicorn app:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Health Check

**GET**

```
/health
```

Response

```json
{
  "status": "ok"
}
```

---

### Chat Endpoint

**POST**

```
/chat
```

Sample Request

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Hiring Java Developer with 4 years experience"
    }
  ]
}
```

Sample Response

```json
{
  "reply": "I found 10 SHL assessments matching your requirements.",
  "recommendations": [
    {
      "name": "Core Java (Entry Level)",
      "url": "https://www.shl.com/products/product-catalog/view/core-java-entry-level-new/",
      "test_type": "Knowledge & Skills"
    }
  ],
  "end_of_conversation": true
}
```

---

## Search Workflow

```
User Query
      │
      ▼
Sentence Transformer Embedding
      │
      ▼
FAISS Similarity Search
      │
      ▼
Relevant SHL Assessments
      │
      ▼
Recommendation Response
```

---

## Example Queries

- Hiring Java Developer with 4 years experience
- Need personality assessment for Sales Executive
- Recommend assessments for Python Developer
- Compare OPQ32r and GSA
- Hiring Data Analyst with communication skills

---

## Safety Features

- Rejects off-topic requests
- Handles prompt injection attempts
- Recommends only official SHL catalog assessments

---

## Future Improvements

- Multi-turn conversation memory
- LLM-powered ranking
- Advanced filtering
- Deployment on Render
- Conversation history support

---
##Live
https://shl-submission-2.onrender.com
