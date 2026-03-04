import pytest
from unittest.mock import patch
from pytest_bdd import scenario, given, when, then
from rpg.character import Character
from rpg.team import Team, duel


@pytest.fixture
def context():
    return {}


@scenario('features/combat.feature', 'Un personnage en attaque un autre')
def test_attack():
    pass


@scenario('features/combat.feature', "Deux personnages s'attaquent mutuellement")
def test_mutual_attack():
    pass


@scenario('features/combat.feature', 'Un duel 2v2 se termine quand une équipe est éliminée')
def test_duel_ends():
    pass


@scenario('features/combat.feature', 'Une équipe avec tous ses membres morts perd le duel')
def test_duel_winner_has_survivor():
    pass


@scenario('features/combat.feature', "Un personnage mort ne participe plus au duel")
def test_dead_dont_attack():
    pass


# --- Given ---

@given("deux personnages")
def two_characters(context):
    context["attacker"] = Character("Alice")
    context["defender"] = Character("Bob")


@given("deux équipes de deux personnages")
def two_teams(context):
    context["team1"] = Team("Équipe A", [Character("Alice"), Character("Bob")])
    context["team2"] = Team("Équipe B", [Character("Charlie"), Character("Dave")])
    context["attacked_by_dead"] = False


# --- When ---

@when("l'un attaque l'autre")
def attack(context):
    with patch("rpg.character.randint", return_value=1):
        context["attacker"].attack(context["defender"])


@when("l'autre riposte")
def attack_back(context):
    with patch("rpg.character.randint", return_value=1):
        context["defender"].attack(context["attacker"])


@when("le duel est simulé jusqu'à la fin")
def simulate_duel(context):
    original_attack = Character.attack

    def tracking_attack(self, other):
        if self.is_dead():
            context["attacked_by_dead"] = True
        original_attack(self, other)

    Character.attack = tracking_attack
    context["winner"] = duel(context["team1"], context["team2"])
    Character.attack = original_attack


# --- Then ---

@then("l'autre perd 1 point de vie")
def check_damage(context):
    assert context["defender"].health == 9


@then("les deux personnages ont 9 points de vie")
def check_mutual_damage(context):
    assert context["attacker"].health == 9
    assert context["defender"].health == 9


@then("une équipe a tous ses membres morts")
def check_one_team_eliminated(context):
    assert context["team1"].is_defeated() or context["team2"].is_defeated()


@then("l'équipe gagnante a au moins un survivant")
def check_winner_has_survivor(context):
    assert not context["winner"].is_defeated()


@then("aucun personnage mort n'a attaqué")
def check_dead_didnt_attack(context):
    assert context["attacked_by_dead"] is False