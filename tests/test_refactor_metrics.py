from rpg.battle import first_attacker
from rpg.character import Character
from rpg.random_gen import FixedRandomGenerator
from unittest.mock import patch

from rpg.team import Team, duel, random_target_selector


def test_fixed_random_generator_bounds_value():
    rng = FixedRandomGenerator(99)
    assert rng.pick_between_zero_and(3) == 999
    rng = FixedRandomGenerator(-5)
    assert rng.pick_between_zero_and(3) == 0


def test_first_attacker_uses_agility_and_tie_break():
    c1 = Character("A")
    c2 = Character("B")
    c1.agility = 4
    c2.agility = 3
    assert first_attacker(c1, c2) is c1
    c1.agility = 1
    c2.agility = 3
    assert first_attacker(c1, c2) is c2
    c2.agility = 1
    assert first_attacker(c1, c2) is c1


def test_duel_breaks_when_no_enemy_left_in_round():
    team1 = Team("A", [Character("A1"), Character("A2")])
    team2 = Team("B", [Character("B1")])

    original_attack = Character.attack

    def kill_attack(self, other, rng=None):
        other.health = 0

    Character.attack = kill_attack
    try:
        winner = duel(team1, team2)
    finally:
        Character.attack = original_attack

    assert winner is team1


def test_random_target_selector_delegates_to_random_choice():
    attacker = Character("A")
    enemies = [Character("E1"), Character("E2")]
    with patch("rpg.team.random.choice", return_value=enemies[1]):
        selected = random_target_selector(attacker, enemies)
    assert selected is enemies[1]
