from pydantic import BaseSettings


class Settings(BaseSettings):
    BOT_TOKEN: str
    CHANNEL_ID: str
    USERNAME: str
    PASSWORD: str
    USER_AGENT: str


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8'
)
