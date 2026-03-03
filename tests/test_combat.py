import pytest
from pytest_bdd import scenario, given, when, then
from rpg.character import Character


@pytest.fixture
def context():
    return {}


@scenario('features/combat.feature', 'Un personnage en attaque un autre')
def test_attack():
    pass
