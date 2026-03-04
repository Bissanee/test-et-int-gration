from random import randint


class Character:
    def __init__(self, name: str, endurance: int = 0, level: int = 0, force: int = 0):
        self.name = name
        self.endurance = endurance
        self.level = level
        self.force = force
        self.health = 10 + endurance + 2 * level

    def attack(self, other: "Character") -> None:
        if self.is_dead():
            raise ValueError(f"{self.name} est mort et ne peut pas attaquer.")
        max_damage = 1 + self.force + 2 * self.level
        damage = randint(0, max_damage)
        other.health = max(0, other.health - damage)

    def is_dead(self) -> bool:
        return self.health <= 0