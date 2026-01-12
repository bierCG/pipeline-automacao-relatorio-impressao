from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    INTERVALO_BUSCA: float
    TIMEOUT_BUSCA: int

    PG_PAUSE: float
    PG_GRAYSCALE: bool
    PG_CONFIDENCE: float

    PATH_PASTA_ASSETS: str
    PATH_PASTA_PROGRAMA_IMPRESSAO: str
    PATH_ARQUIVO_INTEGRACAO: str

    model_config = SettingsConfigDict(
        env_file = ".env"
    )