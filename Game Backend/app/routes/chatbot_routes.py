from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.chatbot import ChatRequest, ChatResponse
from app.services.chatbot_service import get_bot_response, save_chat_message

chatbot_router = APIRouter()

@chatbot_router.post("/ask", response_model=ChatResponse)
def chat_with_bot(request: ChatRequest, db: Session = Depends(get_db)):
    bot_response = get_bot_response(request.message)
    save_chat_message(db, request.message, bot_response)
    return {"response": bot_response}