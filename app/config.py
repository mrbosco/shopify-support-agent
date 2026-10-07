from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    app_name: str = "Shopify Support Agent"
    app_version: str = "0.1.0"
    anthropic_api_key: SecretStr | None = None


settings = Settings()
