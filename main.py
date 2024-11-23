from fastapi import FastAPI, HTTPException, Request
from config import settings
from speech_to_text import speech_to_text
from whatsapp_api import send_message

app = FastAPI()


@app.post("/webhook")
async def webhook(request: Request, payload: dict):
    api_key = request.headers.get("x-api-key")
    if api_key != settings.whatsapp_api_key:
        raise HTTPException(status_code=401, detail="Invalid API key")

    is_voice_message = (
        "dataType" in payload and payload["dataType"] == "media" 
        and "data" in payload and "messageMedia" in payload["data"]
        and "mimetype" in payload["data"]["messageMedia"] and payload["data"]["messageMedia"]["mimetype"] == "audio/ogg; codecs=opus"
        and "data" in payload["data"]["messageMedia"] and type(payload["data"]["messageMedia"]["data"]) == str
    )

    has_recepient = (
        "data" in payload 
        and "message" in payload["data"]
        and "from" in payload["data"]["message"]
        and type(payload["data"]["message"]["from"]) == str
    )

    if is_voice_message and has_recepient:
        base64_audio = payload["data"]["messageMedia"]["data"]
        text = speech_to_text(base64_audio)
        recepient = payload["data"]["message"]["from"]
        await send_message(message="Transcribed message:\n" + text, chat_id=recepient)

    return { "success": True }
