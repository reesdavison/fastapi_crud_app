from app.config import AppConfig
from app.db_models.base import Base
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker


def setup_engine(cfg: AppConfig) -> Engine:
    engine = create_engine(cfg.DATABASE_URL, connect_args={"check_same_thread": False})
    return engine


def get_session(engine: Engine) -> Session:
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal
