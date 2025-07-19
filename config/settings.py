from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    openai_api_key: str | None = None
    allow_dangerous_deserialization: bool = False

    class Config:
        env_file = ".env"
        extra = "allow"


def get_settings() -> Settings:
    return Settings()
