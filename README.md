

# An example FastAPI CRUD application

The idea is to demonstrate a basic production server application containing
- Dependency management.
- Secrets management.
- A sensible database schema.
- A database migration framework with tested migrations.
- A clean API.
- Application logic.
- Input validation.
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
- Secrets management.
- Set up dependency management.
- Set up FastAPI app.
- Setup DB models.
- Setup migration framework.
- Build first API calls - create and get, with tests.
- Iterate over other entities.
- Documentation.

## Things we won't cover

- Authentication and authorisation.

## The task
Manage a set of Jupyter-like "Notebooks" and their "Steps."

## Local dev setup
- Install `poetry` following their [instructions](https://python-poetry.org/docs/#installation).

- Install Python environment manager of your choice, and create Python=3.11 environment eg.
```sh
conda create --name fastapicrud python=3.11
conda activate fastapicrud
poetry install
```

## Add a dependency 
There's 2 ways:
1. `poetry add foo`
2. Add package and version manually to `pyproject.toml` and run `poetry update`.
