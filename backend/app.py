from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from chatbot import ask_ai
from sheets_logger import log_prompt

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://funny-beijinho-d8d7ce.netlify.app", "https://startgenie.co.in"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    prompt: str

@app.get("/")
def home():
    return {"message": "🚀 SmartGenie backend is up and running!"}

@app.post("/ask_ai")
async def ask_ai_route(data: ChatRequest):
    log_prompt(data.prompt)
    response = ask_ai(data.prompt)
    return {"response": response}




