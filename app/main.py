from typing import Generator

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import app.crud as crud
import app.schemas as schemas
from app.database import get_session, setup_engine
from app.env import get_app_config

# We use alembic to manage table creation so don't use this
# Base.metadata.create_all(engine)

app = FastAPI()


def get_db() -> Generator[Session, None, None]:
    engine = setup_engine(get_app_config())
    SessionLocal = get_session(engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/notebooks/", response_model=schemas.Notebook)
def create_notebook(notebook: schemas.NotebookCreate, db: Session = Depends(get_db)):
    notebook = crud.create_notebook(db=db, notebook=notebook)
    return crud.get_notebook_ordered_steps(db=db, notebook_id=notebook.id)


@app.get("/notebooks/{notebook_id}", response_model=schemas.Notebook)
def read_notebook(notebook_id: int, db: Session = Depends(get_db)):
    db_notebook = crud.get_notebook_ordered_steps(db, notebook_id=notebook_id)
    if db_notebook is None:
        raise HTTPException(status_code=404, detail="Notebook not found")
    return db_notebook


@app.post("/notebooks/{notebook_id}/steps/", response_model=schemas.NotebookStep)
def create_step_for_notebook(
    notebook_id: int, step: schemas.NotebookStepCreate, db: Session = Depends(get_db)
):
    return crud.create_step(db=db, step=step, notebook_id=notebook_id)


@app.get("/notebooks/{notebook_id}/steps/", response_model=list[schemas.NotebookStep])
def read_steps(notebook_id: int, db: Session = Depends(get_db)):
    return crud.get_steps(db, notebook_id=notebook_id)


@app.delete("/steps/{step_id}")
def delete_step(step_id: int, db: Session = Depends(get_db)):
    crud.delete_step(db, step_id=step_id)
    return {"message": "Step deleted"}
