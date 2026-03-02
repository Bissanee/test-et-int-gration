# src/rpg/character.py
class Character:
    def __init__(self, name: str):
        self.name = name
        self.health = 10  # 10 points de vie

    def attack(self, other):
        other.health -= 1

    def is_dead(self):
        return self.health <= 0