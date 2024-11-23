# Voice-to-Text echo bot

A FastAPI webhook for processing WhatsApp voice messages, converting them to text using OpenAI Whisper, and sending the transcription back via the WhatsApp API.

## How it works

- Converts WhatsApp voice messages to text.
- Sends transcriptions back to the sender.

## Setup

1. **Clone**:

   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Install**:

   ```bash
   # (optional) create a virtual environment
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Set up whatsapp api**

   Refer to [whatsapp api documentation](https://github.com/chrishubert/whatsapp-api) to get `WHATSAPP_API_URL`, `WHATSAPP_API_KEY`, and `WHATSAPP_SESSION_ID` and point webhook to our server http://localhost:8000/webhook

4. **Configure**:  
   Create a `.env` file:

   ```env
   WHATSAPP_API_URL=<WhatsApp API URL>
   WHATSAPP_API_KEY=<WhatsApp API Key>
   WHATSAPP_SESSION_ID=<Session ID>
   ```

5. **Run**:
   ```bash
   fastapi run
   ```

## Dependencies

- [FastAPI](https://fastapi.tiangolo.com/)
- [OpenAI Whisper](https://platform.openai.com/docs/models/whisper)
- [WhatsApp API](https://github.com/chrishubert/whatsapp-api)
