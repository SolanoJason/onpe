from pydantic import BaseModel, computed_field, PostgresDsn, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal, Self
import urllib.parse
from fastapi.templating import Jinja2Templates


class DatabaseQuerySettings(BaseModel):
    SSLMODE: Literal[
        "disable", "allow", "prefer", "require", "verify-ca", "verify-full"
    ] = "prefer"
    APPLICATION_NAME: str = "onpe"


class DatabaseSettings(BaseModel):
    DRIVER: str = "postgresql+psycopg"
    HOST: str = "localhost"
    USER: str = "postgres"
    PORT: int = 5432
    PASSWORD: str
    NAME: str

    QUERY: DatabaseQuerySettings = DatabaseQuerySettings()

    @computed_field
    @property
    def URI(self) -> PostgresDsn:
        return PostgresDsn.build(
            scheme=self.DRIVER,
            host=self.HOST,
            password=self.PASSWORD,
            username=self.USER,
            port=self.PORT,
            path=self.NAME,
            query=urllib.parse.urlencode(
                {k.lower(): v for k, v in settings.DB.QUERY.model_dump().items()}
            ),
        )


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="forbid",
        frozen=True,
        case_sensitive=True,
        env_file_encoding="utf-8",
        env_ignore_empty=True,
        env_nested_delimiter="__",
    )

    DEBUG: bool

    DB: DatabaseSettings

    TEMPLATES_DIR: str = "templates"
    STATIC_DIR: str = "static"

    ONPE_URL: str = "https://resultadoelectoral.onpe.gob.pe"

    @model_validator(mode="after")
    def check_environment(self) -> Self:
        if not self.DEBUG and self.DB.QUERY.SSLMODE in ("disable", "allow", "prefer"):
            raise ValueError("SSL is required in production")
        return self
    
    @property
    def templates(self) -> Jinja2Templates:
        templates = Jinja2Templates(directory=self.TEMPLATES_DIR)
        return templates


settings = Settings()  # type: ignore
