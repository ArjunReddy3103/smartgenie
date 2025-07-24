from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
from chatbot import ask_ai
import os

app = FastAPI()
# -------------------- CORS Middleware --------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://zesty-halva-749f5e.netlify.app"],  # ✅ Set specific domain in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ------------------- Pydantic Schemas --------------------
class ChatRequest(BaseModel):
    prompt: str
    company_name: str
# -------------------- Routes --------------------
@app.get("/")
def home():
    return {"message": "🚀 SmartGenie backend is up and running!"}

@app.post("/ask_ai")
async def ask_ai_route(data: ChatRequest):
    response = ask_ai(data.prompt, data.company_name)
    return {"response": response}
