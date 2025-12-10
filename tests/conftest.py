import pytest
from fastapi.testclient import TestClient
from src.api_app import app
from src.db import FakeDB

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def fake_db():
    return FakeDB()
