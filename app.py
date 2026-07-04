from fastapi import FastAPI
from routes.chat import router

app = FastAPI(title="SHL Conversational Agent")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/")
def home():
    return {
        "message": "SHL Conversational Agent Running"
    }


app.include_router(router)