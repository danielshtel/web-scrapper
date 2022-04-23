from pydantic import BaseSettings


class Settings(BaseSettings):
    BOT_TOKEN: str
    CHANNEL_ID: str


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8'
)
