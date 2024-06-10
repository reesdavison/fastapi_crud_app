from typing import Annotated, Generator

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app.config import AppConfig
from app.database import get_session, setup_engine
from app.db_models import Base
from app.env import get_app_config

engine = setup_engine(get_app_config())

# We use alembic to manage table creation so don't use this
# Base.metadata.create_all(engine)

app = FastAPI()


def get_db() -> Generator[Session, None, None]:
    SessionLocal = get_session(engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/info")
async def info(settings: Annotated[AppConfig, Depends(get_app_config)]):
    return {
        "db_url": settings.DATABASE_URL,
    }
