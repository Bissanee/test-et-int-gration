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


def duel(
    team1: Team,
    team2: Team,
    target_selector: TargetSelector = random_target_selector,
) -> Team:
    """
    Simule un duel 2v2 tour par tour.
    Chaque personnage vivant attaque un ennemi vivant aléatoire.
    Retourne l'équipe gagnante.
    """
    while not team1.is_defeated() and not team2.is_defeated():
        attackers = team1.alive_members() + team2.alive_members()
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