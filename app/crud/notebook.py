from sqlalchemy.orm import Session

import app.db_models as dbm
import app.schemas as schemas


def get_notebook(db: Session, notebook_id: int) -> dbm.NotebookModel:
    return (
        db.query(dbm.NotebookModel).filter(dbm.NotebookModel.id == notebook_id).first()
    )


def create_notebook(db: Session, notebook: schemas.NotebookCreate) -> dbm.NotebookModel:
    db_notebook = dbm.NotebookModel(name=notebook.name)
    db.add(db_notebook)
    db.commit()
    db.refresh(db_notebook)
    return db_notebook
    return db_notebook
