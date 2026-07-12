from pydantic import model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    APP_NAME: str = "FocusFlow"

    VERSION: str = "1.0"

    API_PREFIX: str = "/api/v1"

    DEBUG: bool = True

    DATABASE_HOST: str

    DATABASE_PORT: int

    DATABASE_NAME: str

    DATABASE_USER: str

    DATABASE_PASSWORD: str

    DATABASE_URL: str | None = None

    @model_validator(mode="after")
    def build_database_url(self) -> "Settings":
        if not self.DATABASE_URL:
            self.DATABASE_URL = (
                f"postgresql://{self.DATABASE_USER}:{self.DATABASE_PASSWORD}"
                f"@{self.DATABASE_HOST}:{self.DATABASE_PORT}/{self.DATABASE_NAME}"
            )
        return self


settings = Settings()