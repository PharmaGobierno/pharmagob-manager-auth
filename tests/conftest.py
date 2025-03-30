from typing import Generator
from unittest.mock import Mock

from infra.mongodb import MongoDbManager
from pytest import fixture
from starlette.testclient import TestClient

from main import app


@fixture
def mocked_repository(mocker) -> Mock:
    mocked_repo = Mock()
    mocker.patch.object(MongoDbManager, "__new__", return_value=mocked_repo)
    return mocked_repo


@fixture
def client() -> Generator:
    with TestClient(app) as test_client:
        yield test_client
