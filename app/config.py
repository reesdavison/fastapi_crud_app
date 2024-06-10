from pydantic import BaseModel, Field


class AppConfig(BaseModel):
    DATABASE_URL: str = Field(
        description="eg postgresql://user:password@postgresserver/db"
    )
