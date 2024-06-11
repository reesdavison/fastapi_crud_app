from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.config import AppConfig
from app.db_models.base import Base


def setup_engine(cfg: AppConfig) -> Engine:
    engine = create_engine(cfg.DATABASE_URL)
    return engine


def get_session(engine: Engine) -> Session:
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal
