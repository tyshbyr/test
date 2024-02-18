from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    project_name: str = "project_name"
    sqlalchemy_database_url: str = "database_url"

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


app_config = AppSettings()
