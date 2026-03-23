import random
from typing import Callable

from rpg.character import Character


class Team:
    def __init__(self, name: str, members: list):
        self.name = name
        self.members = members

    def alive_members(self) -> list:
        return [m for m in self.members if not m.is_dead()]

    def is_defeated(self) -> bool:
        return len(self.alive_members()) == 0


TargetSelector = Callable[[Character, list[Character]], Character]


def random_target_selector(_: Character, enemies: list[Character]) -> Character:
    return random.choice(enemies)


def target_weight(target: Character) -> float:
    chance_factor = 1.0 / (1.0 + max(0, target.chance))
    low_hp_priority = 3.0 if (target.health / target.max_health) < 0.30 else 1.0
    return chance_factor * low_hp_priority


def priority_target_selector(_: Character, enemies: list[Character]) -> Character:
    weights = [target_weight(enemy) for enemy in enemies]
    return random.choices(enemies, weights=weights, k=1)[0]


def duel(
    team1: Team,
    team2: Team,
    target_selector: TargetSelector = priority_target_selector,
) -> Team:
    """
    Simule un duel 2v2 tour par tour.
    Chaque personnage vivant attaque un ennemi vivant aléatoire.
    Retourne l'équipe gagnante.
    """
    while not team1.is_defeated() and not team2.is_defeated():
        attackers = team1.alive_members() + team2.alive_members()
        attackers.sort(key=lambda c: c.agility, reverse=True)
        for attacker in attackers:
            if attacker.is_dead():
                continue

            if attacker in team1.members:
                enemies = team2.alive_members()
            else:
                enemies = team1.alive_members()

            if not enemies:
                break

            target = target_selector(attacker, enemies)
            attacker.attack(target)

    return team1 if not team1.is_defeated() else team2