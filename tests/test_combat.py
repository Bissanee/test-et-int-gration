import pytest
from pytest_bdd import scenario, given, when, then
from rpg.character import Character


@pytest.fixture
def context():
    return {}


@scenario('features/combat.feature', 'Un personnage en attaque un autre')
def test_attack():
    pass


@scenario('features/combat.feature', "Deux personnages s'attaquent mutuellement")
def test_mutual_attack():
    pass


@given("deux personnages")
def two_characters(context):
    context["attacker"] = Character("Alice")
    context["defender"] = Character("Bob")


@when("l'un attaque l'autre")
def attack(context):
    context["attacker"].attack(context["defender"])


@when("l'autre riposte")
def attack_back(context):
    context["defender"].attack(context["attacker"])


@then("l'autre perd 1 point de vie")
def check_damage(context):
    assert context["defender"].health == 9


@then("les deux personnages ont 9 points de vie")
def check_mutual_damage(context):
    assert context["attacker"].health == 9
    assert context["defender"].health == 9
