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
async def ask_ai_route(request: Request, data: ChatRequest):
    client_host = request.client.host
    forwarded_for = request.headers.get("x-forwarded-for")
    user_ip = forwarded_for.split(",")[0].strip() if forwarded_for else client_host
    log_prompt(data.prompt, user_ip)
    response = ask_ai(data.prompt)
    return {"response": response}





