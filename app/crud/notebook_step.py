from fastapi import HTTPException
from sqlalchemy.orm import Session

import app.db_models as dbm
import app.schemas as schemas
from app.constants import NOTEBOOK_LIMIT


def get_last_step(db: Session, notebook_id: int) -> int:
    model = (
        db.query(dbm.NotebookStepModel)
        .filter(dbm.NotebookStepModel.notebook_id == notebook_id)
        .order_by(dbm.NotebookStepModel.index.desc())
        .first()
    )
    if model:
        return model.index
    return 0


def get_step(db: Session, step_id: int) -> dbm.NotebookStepModel | None:
    model = (
        db.query(dbm.NotebookStepModel)
        .filter(dbm.NotebookStepModel.id == step_id)
        .first()
    )
    return model


def get_step_by_index(db: Session, index: int) -> dbm.NotebookStepModel | None:
    model = (
        db.query(dbm.NotebookStepModel)
        .filter(dbm.NotebookStepModel.index == index)
        .first()
    )
    return model


def increment_steps(db: Session, notebook_id: int, step_onwards: int):
    (
        db.query(dbm.NotebookStepModel)
        .filter(
            dbm.NotebookStepModel.notebook_id == notebook_id,
            dbm.NotebookStepModel.index >= step_onwards,
        )
        .update({dbm.NotebookStepModel.index: dbm.NotebookStepModel.index + 1})
    )


def decrement_steps(db: Session, notebook_id: int, step_onwards: int):
    (
        db.query(dbm.NotebookStepModel)
        .filter(
            dbm.NotebookStepModel.notebook_id == notebook_id,
            dbm.NotebookStepModel.index >= step_onwards,
        )
        .update({dbm.NotebookStepModel.index: dbm.NotebookStepModel.index - 1})
    )


def create_step(db: Session, step: schemas.NotebookStepCreate, notebook_id: int):

    last_step_index = get_last_step(db, notebook_id)
    if last_step_index >= NOTEBOOK_LIMIT:
        # == should be fine here
        raise HTTPException(
            status_code=400, detail=f"Notebook has too many steps. Max {NOTEBOOK_LIMIT}"
        )

    prev_step_index = last_step_index
    if step.prev_step_id:
        prev_step = get_step(db, step.prev_step_id)
        if prev_step is None:
            raise HTTPException(status_code=400, detail="That step does not exist")
        prev_step_index = prev_step.index

    step_index = prev_step_index + 1
    increment_steps(db, notebook_id, step_index)

    # add new step, removing prev_step_index, and adding new index
    data = step.model_dump()
    del data["prev_step_id"]
    data["index"] = step_index
    db_step = dbm.NotebookStepModel(**data, notebook_id=notebook_id)
    db.add(db_step)

    db.commit()
    db.refresh(db_step)
    return db_step


def get_steps(db: Session, notebook_id: int) -> list[dbm.NotebookStepModel]:
    models = (
        db.query(dbm.NotebookStepModel)
        .filter(dbm.NotebookStepModel.notebook_id == notebook_id)
        .order_by(dbm.NotebookStepModel.index)
        .all()
    )
    return models


def delete_step(db: Session, step_id: int):
    model = (
        db.query(dbm.NotebookStepModel)
        .filter(
            dbm.NotebookStepModel.id == step_id,
        )
        .first()
    )
    if model is None:
        raise HTTPException(status_code=404, detail="Step not found")

    index = model.index
    notebook_id = model.notebook_id

    # perform actual delete here
    db.query(dbm.NotebookStepModel).filter(
        dbm.NotebookStepModel.id == step_id,
    ).delete()

    decrement_steps(db, notebook_id, index)
    db.commit()


def move_step(db: Session, step_id: int, move_up: bool = True):

    step = get_step(db, step_id)
    if step is None:
        raise HTTPException(status_code=400, detail="That step does not exist")

    index = step.index

    if move_up:
        if index == 1:
            # we're the top step already
            return step
        switch_index = index - 1
    else:
        switch_index = index + 1

    other_step = get_step_by_index(db, switch_index)
    if other_step is None:
        # the assumption here is we're already on the last step
        return step

    # This is performed in a nested transaction to
    # avoid the DB ending up in a strange state
    # everything will be rolled back unless it reaches the db.commit()
    # This faff with the temporary index is to avoid violating
    # the unique constraint on index
    temp1 = NOTEBOOK_LIMIT + 1000
    temp2 = NOTEBOOK_LIMIT + 1001
    with db.begin_nested():
        step.index = temp1
        other_step.index = temp2
        db.flush()
        step.index = switch_index
        other_step.index = index
        db.flush()
        db.commit()

    db.commit()
    return step
