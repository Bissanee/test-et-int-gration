import pytest
from pytest_bdd import scenario, given, when, then
from rpg.character import Character

@pytest.fixture
def context():
    return {}

@scenario('features/combat.feature', 'A character attacks another')
def test_attack():
    pass

@given("two characters")
def two_characters(context):
    context["attacker"] = Character("Alice")
    context["defender"] = Character("Bob")

@when("one character attacks the other")
def attack(context):
    context["attacker"].attack(context["defender"])

@then("the other character should lose 1 health point")
def check_damage(context):
    assert context["defender"].health == 9