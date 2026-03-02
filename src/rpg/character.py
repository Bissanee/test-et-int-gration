class Character:
    def __init__(self):
        self.health = 10

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def is_dead(self):
        return self.health == 0