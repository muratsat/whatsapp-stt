import base64
from io import BytesIO
from openai import OpenAI
from config import settings

client = OpenAI(api_key=settings.openai_api_key)

def speech_to_text(base64_audio: str) -> str:
    audio_bytes = base64.b64decode(base64_audio)
    audio_file = BytesIO(audio_bytes)
    audio_file.name = "audio.mp3"

    transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file
    )

    return transcription.text
