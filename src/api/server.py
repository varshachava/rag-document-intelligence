from fastapi import FastAPI

app = FastAPI()

@app.get("/health")

def health_check():

    return {"status": "RAG API running"}

@app.get("/query")

def query(question: str):

    return {

        "question": question,

        "answer": "RAG pipeline response placeholder"

    }
