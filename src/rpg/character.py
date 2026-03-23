from typing import Optional

from rpg.random_gen import DEFAULT_RNG, RandomGenerator


class Character:
    def __init__(self, name: str, endurance: int = 0, level: int = 0, force: int = 0):
        self.name = name
        self.endurance = endurance
        self.level = level
        self.force = force
        self.health = 10 + endurance + 2 * level
        self.equipment = []
        self.weapon = None

    @property
    def armor(self) -> int:
        return sum(e.armor for e in self.equipment)

    @property
    def max_damage(self) -> int:
        base = self.weapon.damage if self.weapon else 1
        return base + self.force + 2 * self.level

    def attack(self, other: "Character", rng: Optional[RandomGenerator] = None) -> None:
        if self.is_dead():
            raise ValueError(f"{self.name} est mort et ne peut pas attaquer.")
        random_generator = rng if rng is not None else DEFAULT_RNG
        raw_damage = random_generator.pick_between_zero_and(self.max_damage)
        damage = max(0, raw_damage - other.armor)
        other.health = max(0, other.health - damage)

    def is_dead(self) -> bool:
        return self.health <= 0