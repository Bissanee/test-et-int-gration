class Character:
    def __init__(self, name: str):
        self.name = name
        self.health = 10

    def attack(self, other: "Character") -> None:
        other.health = max(0, other.health - 1)

    def is_dead(self) -> bool:
        return self.health <= 0
