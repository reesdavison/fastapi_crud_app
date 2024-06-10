from typing import Annotated, Generator

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import app.crud as crud
import app.schemas as schemas
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


# @app.get("/info")
# async def info(settings: Annotated[AppConfig, Depends(get_app_config)]):
#     return {
#         "db_url": settings.DATABASE_URL,
#     }


@app.post("/notebooks/", response_model=schemas.Notebook)
def create_notebook(notebook: schemas.NotebookCreate, db: Session = Depends(get_db)):
    return crud.create_notebook(db=db, notebook=notebook)


@app.get("/notebooks/{notebook_id}", response_model=schemas.Notebook)
def read_notebook(notebook_id: int, db: Session = Depends(get_db)):
    db_notebook = crud.get_notebook(db, notebook_id=notebook_id)
    if db_notebook is None:
        raise HTTPException(status_code=404, detail="Notebook not found")
    return db_notebook
