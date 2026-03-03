import pytest
from pytest_bdd import scenario, given, when, then
from rpg.character import Character


@pytest.fixture
def context():
    return {}


@scenario('features/character.feature', 'Un nouveau personnage a 10 points de vie')
def test_new_character():
    pass


@given("un nouveau personnage")
def new_character(context):
    context["char"] = Character("Alice")


@then("le personnage a 10 points de vie")
def check_10hp(context):
    assert context["char"].health == 10
