from sqlalchemy.orm import Session

import app.db_models as dbm
import app.schemas as schemas
from app.crud.notebook_step import get_steps


def get_notebook(db: Session, notebook_id: int) -> dbm.NotebookModel:
    return (
        db.query(dbm.NotebookModel).filter(dbm.NotebookModel.id == notebook_id).first()
    )


def get_notebook_ordered_steps(db: Session, notebook_id: int) -> schemas.Notebook:
    steps = get_steps(db, notebook_id)
    notebook = get_notebook(db, notebook_id)
    schema_nb = schemas.Notebook.model_validate(notebook, from_attributes=True)
    schema_nb.steps = steps
    return schema_nb


def create_notebook(db: Session, notebook: schemas.NotebookCreate) -> dbm.NotebookModel:
    db_notebook = dbm.NotebookModel(name=notebook.name)
    db.add(db_notebook)
    db.commit()
    db.refresh(db_notebook)
    return db_notebook
