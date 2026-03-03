import pytest
from pytest_bdd import scenario, given, when, then
from rpg.character import Character


@pytest.fixture
def context():
    return {}
