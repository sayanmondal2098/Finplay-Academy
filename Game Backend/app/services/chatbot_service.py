from sqlalchemy.orm import Session
from app.models.chatbot import ChatbotMessage

def get_bot_response(user_message: str) -> str:
    responses = {
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm just a bot, but I'm doing great!",
        "bye": "Goodbye! Have a nice day!"
    }
    for key, value in responses.items():
        if key in user_message.lower():
            return value
    return "Sorry, I didn't understand that."

def save_chat_message(db: Session, user_message: str, bot_response: str):
    chat_message = ChatbotMessage(user_message=user_message, bot_response=bot_response)
    db.add(chat_message)
    db.commit()
    db.refresh(chat_message)
    return chat_message
