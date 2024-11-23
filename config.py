from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    whatsapp_api_url: str
    whatsapp_api_key: str
    whatsapp_session_id: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
