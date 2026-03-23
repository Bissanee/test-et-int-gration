from random import randint
from typing import Protocol


class RandomGenerator(Protocol):
    def pick_between_zero_and(self, maximum: int) -> int:
        ...


class SystemRandomGenerator:
    def pick_between_zero_and(self, maximum: int) -> int:
        return randint(0, maximum)


class FixedRandomGenerator:
    def __init__(self, value: int):
        self.value = value

    def pick_between_zero_and(self, maximum: int) -> int:
        return max(0, min(self.value, maximum))


DEFAULT_RNG = SystemRandomGenerator()
