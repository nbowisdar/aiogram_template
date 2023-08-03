from pydantic_settings import BaseSettings

WITH_ENV = False

language_file_path = "src/bot/db/language.json"


class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    token_bot: str

    class Config:
        env_file = ".env"


settings = Settings()


admins_id = [
    179738472,
    286365412,
]
