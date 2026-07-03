import copy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Reset in-memory activity state around each test for isolation."""
    original_state = copy.deepcopy(app_module.activities)
    try:
        yield
    finally:
        app_module.activities.clear()
        app_module.activities.update(original_state)


@pytest.fixture
def client():
    return TestClient(app_module.app)