from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url = 'sqlite:///./db.sqlite3'

settings = Settings()