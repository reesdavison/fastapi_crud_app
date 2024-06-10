

# An example FastAPI CRUD application

The idea is to demonstrate a basic production server application containing
- Dependency management.
- A sensible database schema.
- A database migration framework with tested migrations.
- A clean API.
- Application logic.
- Error handling.
- Test cases.
- Documentation.
- Deployment with Docker Compose.

The core libraries we're going to use:
- FastAPI
- SQLAlchemy
- Alembic

Order of execution:
- Set up version control.
- Set up dependency management.
- Set up FastAPI app.
- Setup DB models.
- Setup migration framework.
- Build first API calls - create and get, with tests.
- Iterate over other entities.
- Documentation.

## The task
Manage a set of Jupyter-like "Notebooks" and their "Steps."

## Local dev
Install `poetry` following instructions

Install Python environment manager of your choice, and create Python=3.11 environment eg.
```sh
conda create --name fastapicrud python=3.11
conda activate fastapicrud
```

