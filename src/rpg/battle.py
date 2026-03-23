from rpg.character import Character


def first_attacker(c1: Character, c2: Character) -> Character:
    """
    Détermine qui attaque en premier en duel 1v1.
    Le personnage avec la plus grande agilité (agility) commence.
    En cas d'égalité, le premier argument est choisi.
    """
    if c1.agility > c2.agility:
        return c1
    if c2.agility > c1.agility:
        return c2
    return c1

