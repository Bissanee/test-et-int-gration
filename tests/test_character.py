import pytest
from pytest_bdd import scenario, given, when, then
from rpg.character import Character


@pytest.fixture
def context():
    return {}


@scenario('features/character.feature', 'Un nouveau personnage a 10 points de vie')
def test_new_character():
    pass


@scenario('features/character.feature', 'Un personnage meurt à 0 point de vie')
def test_character_dies():
    pass


@scenario('features/character.feature', 'Un personnage perd 1 HP quand il est attaqué')
def test_character_attacked():
    pass


@scenario('features/character.feature', 'Les HP ne peuvent pas descendre sous zéro')
def test_health_floor():
    pass


@scenario('features/character.feature', 'Un personnage mort ne peut pas attaquer')
def test_dead_cannot_attack():
    pass


@scenario('features/character.feature', 'Un personnage a une endurance de 0 par défaut')
def test_default_endurance():
    pass


@scenario('features/character.feature', 'Les HP dépendent de l\'endurance')
def test_hp_depends_on_endurance():
    pass


@scenario('features/character.feature', 'Un personnage a un niveau 0 par défaut')
def test_default_level():
    pass


@given("un nouveau personnage")
def new_character(context):
    context["char"] = Character("Alice")


@given("un personnage mort")
def dead_character(context):
    c = Character("Alice")
    c.health = 0
    context["char"] = c


@given("un personnage avec une endurance de 5")
def character_with_endurance(context):
    context["char"] = Character("Alice", endurance=5)


@when("le personnage perd toute sa vie")
def lose_all_health(context):
    context["char"].health = 0


@when("le personnage est attaqué")
def character_is_attacked(context):
    attacker = Character("Bob")
    attacker.attack(context["char"])


@when("le personnage mort tente d'attaquer")
def dead_attacks(context):
    target = Character("Bob")
    try:
        context["char"].attack(target)
        context["error"] = None
    except ValueError as e:
        context["error"] = e


@then("le personnage a 10 points de vie")
def check_10hp(context):
    assert context["char"].health == 10


@then("le personnage est mort")
def check_dead(context):
    assert context["char"].is_dead()


@then("le personnage a 9 points de vie")
def check_9hp(context):
    assert context["char"].health == 9


@then("les HP du personnage sont toujours à 0")
def check_hp_floor(context):
    assert context["char"].health == 0


@then("une erreur est levée")
def check_error(context):
    assert context["error"] is not None
    assert isinstance(context["error"], ValueError)


@then("son endurance est de 0")
def check_default_endurance(context):
    assert context["char"].endurance == 0


@then("le personnage a 15 points de vie")
def check_15hp(context):
    assert context["char"].health == 15


@then("son niveau est 0")
def check_default_level(context):
    assert context["char"].level == 0
