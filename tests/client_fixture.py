import psycopg
import pytest
from fastapi.testclient import TestClient
from pytest_mock import MockerFixture
from sqlalchemy import create_engine


def create_test_sync_engine(postgresql: psycopg.Connection, echo: bool = True):
    return create_engine(
        f"postgresql://{postgresql.info.user}:@{postgresql.info.host}:{postgresql.info.port}/{postgresql.info.dbname}",
        echo=echo,
    )


@pytest.fixture(scope="function")
def client(mocker: MockerFixture, postgresql: psycopg.Connection):
    from app.db_models import Base

    engine = create_test_sync_engine(postgresql)
    Base.metadata.create_all(engine)

    from app.main import app

    mocker.patch("app.main.setup_engine", return_value=engine)
    return TestClient(app)
