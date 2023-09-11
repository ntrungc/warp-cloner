from typing import Any
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    BASE_KEYS: list[str] = Field(
        env='BASE_KEYS',
        default=[
            '469u0LcP-3g6pw70T-FXU587E9',
            '2O78XsU5-c46Y7v9K-9v6I78Pc',
            '65ICO3z7-e2J816WV-b59fN6Z7',
        ]
    )
    THREADS_COUNT: int = Field(env='THREADS_COUNT', default=3)
    PROXY_FILE: str | None = Field(env='PROXY_FILE', default=None)
    DEVICE_MODELS: list[str] = Field(env='DEVICE_MODELS', default=[])
    SAVE_WIREGUARD_VARIABLES: bool = Field(env='SAVE_WIREGUARD_VARIABLES', default=False)
    DELAY: int = Field(env='DELAY', default=25)
    OUTPUT_FILE: str = Field(env='OUTPUT_FILE', default='output.txt')
    OUTPUT_FORMAT: str = Field(env='OUTPUT_FORMAT', default='{key} | {referral_count}')
    RETRY_COUNT: int = Field(env='RETRY_COUNT', default=3)

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

        @classmethod
        def parse_env_var(cls, field: str, raw_val: str) -> Any:
            if field == 'BASE_KEYS' or field == 'DEVICE_MODELS':
                if isinstance(raw_val, str):
                    return str(raw_val).split(',')

            return cls.json_loads(raw_val) # type: ignore

config = Settings()
