from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    allow_dangerous_deserialization: bool = False

    class Config:
        env_file = ".env"
        extra = "allow"

def get_settings():
    return Settings()
