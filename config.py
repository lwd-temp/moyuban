from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    holidays_file: str = "data/holidays.json"
    holidays_file_url: str = "https://raw.githubusercontent.com/dreamhunter2333/moyuban/main/data/holidays.json"
    holidays_file_cron: str = "0 0 * * 1"

    class Config:
        env_file = ".env"


settings = Settings()