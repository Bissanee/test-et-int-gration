import pytest
from unittest.mock import patch
from pytest_bdd import scenario, given, when, then
from rpg.character import Character
from rpg.team import Team, duel, target_weight


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


@scenario("features/combat.feature", "Le personnage avec la plus grande AGI attaque en premier")
def test_highest_agility_attacks_first():
    pass


@scenario("features/combat.feature", "Les chances d'être attaqué dépendent de CHN")
def test_targeting_depends_on_chance():
    pass


@scenario("features/combat.feature", "Une cible avec moins de 30 pourcents de PV est prioritaire")
def test_low_hp_target_is_priority():
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


@given("deux équipes de deux personnages avec agilités différentes")
def two_teams_with_agility(context):
    fast = Character("Rapide", agility=10)
    ally = Character("Allié", agility=1)
    enemy1 = Character("Enemy1", agility=2)
    enemy2 = Character("Enemy2", agility=3)
    context["team1"] = Team("Équipe A", [fast, ally])
    context["team2"] = Team("Équipe B", [enemy1, enemy2])
    context["fast"] = fast


@given("deux cibles avec des CHN différentes")
def two_targets_with_different_chance(context):
    low_chance = Character("LowCHN", chance=0)
    high_chance = Character("HighCHN", chance=5)
    context["low_chance_target"] = low_chance
    context["high_chance_target"] = high_chance


@given("deux cibles dont une a moins de 30 pourcents de PV")
def two_targets_one_low_hp(context):
    healthy = Character("Healthy")
    low_hp = Character("LowHP")
    low_hp.health = 2  # 20% de 10 PV
    context["healthy_target"] = healthy
    context["low_hp_target"] = low_hp


# --- When ---

@when("l'un attaque l'autre")
def attack(context):
    with patch("rpg.random_gen.randint", return_value=1):
        context["attacker"].attack(context["defender"])


@when("l'autre riposte")
def attack_back(context):
    with patch("rpg.random_gen.randint", return_value=1):
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


@when("le duel est simulé pour un seul tour")
def simulate_one_turn_duel(context):
    original_attack = Character.attack
    context["first_attacker"] = None

    def tracking_attack(self, other):
        if context["first_attacker"] is None:
            context["first_attacker"] = self
        other.health = 0
        original_attack(self, other)

    Character.attack = tracking_attack
    try:
        duel(context["team1"], context["team2"])
    finally:
        Character.attack = original_attack


@when("on calcule leur poids de ciblage")
def compute_weights(context):
    if "low_chance_target" in context:
        context["low_chance_weight"] = target_weight(context["low_chance_target"])
        context["high_chance_weight"] = target_weight(context["high_chance_target"])
    else:
        context["healthy_weight"] = target_weight(context["healthy_target"])
        context["low_hp_weight"] = target_weight(context["low_hp_target"])


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


@then("le premier attaquant est celui avec la plus grande AGI")
def check_first_attacker(context):
    assert context["first_attacker"] is context["fast"]


@then("la cible avec la plus grande CHN a un poids plus faible")
def check_chance_weight(context):
    assert context["high_chance_weight"] < context["low_chance_weight"]


@then("la cible sous 30 pourcents a un poids plus grand")
def check_low_hp_priority(context):
    assert context["low_hp_weight"] > context["healthy_weight"]
