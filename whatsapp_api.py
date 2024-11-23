import asyncio
import requests

from config import settings

API_KEY = settings.whatsapp_api_key
BASE_URL = settings.whatsapp_api_url
SESSION_ID = settings.whatsapp_session_id
HEADERS = {
    "Content-Type": "application/json",
    "x-api-key": API_KEY,
}


async def send_message(message: str, chat_id: str):
    print(f"Sending message to {chat_id}: {message}")

    url = f"{BASE_URL}/client/sendMessage/{SESSION_ID}"

    data = {
        "chatId": chat_id,
        "contentType": "string",
        "content": message,
    }

    req = requests.post(url, json=data, headers=HEADERS)
    print(req.json())
