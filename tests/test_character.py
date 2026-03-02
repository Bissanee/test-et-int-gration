import pytest
from pytest_bdd import scenario, given, when, then
from rpg.character import Character

@pytest.fixture
def context():
    return {}



# Lier les scenarios du feature
@scenario('features/character.feature', 'A new character has 10 health points')
def test_new_character():
    pass

@scenario('features/character.feature', 'A character dies at 0 health')
def test_character_dies():
    pass

@given("a new character")
def new_character(context):
    context["char"] = Character("Alice")  # <- ajoute un nom

@given("two characters")
def two_characters(context):
    context["attacker"] = Character("Alice")
    context["defender"] = Character("Bob")

@when("the character loses all health")
def lose_all_health(context):
    context["char"].health = 0

@then("the character should have 10 health points")
def check_hp(context):
    assert context["char"].health == 10

@then("the character should be dead")
def check_dead(context):
    assert context["char"].is_dead()