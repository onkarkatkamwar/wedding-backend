from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Wedding Company Backend"
    MONGO_URL: str
    DB_NAME: str = "wedding_master_db"
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

settings = Settings()