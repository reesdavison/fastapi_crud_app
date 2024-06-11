

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

## Future things

- There's more CRUD to be done. delete notebook, reorder steps. It would re-use a lot of the same code.
- Github action test pipeline

## The task
Manage a set of Jupyter like `Notebooks` and their `Steps`.

## Local dev

### Setup
- Install `poetry` following their [instructions](https://python-poetry.org/docs/#installation).

- Install Python environment manager of your choice, and create Python=3.11 environment eg.
```sh
conda create --name fastapicrud python=3.11
conda activate fastapicrud
poetry install
```

### Add a dependency 
There's 2 ways:
1. `poetry add foo`
2. Add package and version manually to `pyproject.toml` and run `poetry update`.


### Migrations
To generate a new migration the simple way after updating the declarative schema:
```
alembic revision --autogenerate -m "<message>"
```

To upgrade the DB to the latest version.
```
alembic upgrade head
```

### Running in dev mode
After migrating your DB to the latest. Run postgres in one terminal with
```
docker-compose up db
```
In another terminal, run the dev server with
```
fastapi dev app/main.py
```


## Production
If you just want to build the container
```
docker build . --tag fastapi_crud_app-web
```
If you want to build and run all the services together, we're using docker-compose to serve our app.
```
docker-compose up --build
```