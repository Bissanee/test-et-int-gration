import pytest
from pytest_bdd import scenario, given, when, then
from rpg.character import Character

@pytest.fixture
def context():
    return {}

@scenario('features/character.feature', 'A new character has 10 health points')
def test_new_character():
    pass

@scenario('features/character.feature', 'A character dies at 0 health')
def test_character_dies():
    pass

@scenario('features/character.feature', 'A character loses 1 HP when attacked')
def test_character_attacked():
    pass

@given("a new character")
def new_character(context):
    context["char"] = Character("Alice")

@when("the character loses all health")
def lose_all_health(context):
    context["char"].health = 0

@when("the character is attacked")
def character_is_attacked(context):
    attacker = Character("Bob")
    attacker.attack(context["char"])

@then("the character should have 10 health points")
def check_hp(context):
    assert context["char"].health == 10

@then("the character should be dead")
def check_dead(context):
    assert context["char"].is_dead()

@then("the character has 9 HP")
def check_9hp(context):
    assert context["char"].health == 9