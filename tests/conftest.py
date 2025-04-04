from typing import Generator

from main import app
from pytest import fixture
from starlette.testclient import TestClient


@fixture
def client() -> Generator:
    with TestClient(app) as test_client:
        yield test_client
