class Character:
    def __init__(self, name: str, endurance: int = 0):
        self.name = name
        self.endurance = endurance
        self.health = 10

    def attack(self, other: "Character") -> None:
        if self.is_dead():
            raise ValueError(f"{self.name} est mort et ne peut pas attaquer.")
        other.health = max(0, other.health - 1)

    def is_dead(self) -> bool:
        return self.health <= 0
