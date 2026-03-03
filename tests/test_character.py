import pytest
from pytest_bdd import scenario, given, when, then
from rpg.character import Character


@pytest.fixture
def context():
    return {}


@scenario('features/character.feature', 'Un nouveau personnage a 10 points de vie')
def test_new_character():
    pass


@scenario('features/character.feature', 'Un personnage meurt à 0 point de vie')
def test_character_dies():
    pass


@given("un nouveau personnage")
def new_character(context):
    context["char"] = Character("Alice")


@when("le personnage perd toute sa vie")
def lose_all_health(context):
    context["char"].health = 0


@then("le personnage a 10 points de vie")
def check_10hp(context):
    assert context["char"].health == 10


@then("le personnage est mort")
def check_dead(context):
    assert context["char"].is_dead()
