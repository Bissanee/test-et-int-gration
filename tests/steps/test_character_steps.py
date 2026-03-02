import pytest
from pytest_bdd import given, when, then

@when("the character takes 10 damage")
def take_damage(context):
    context["character"].take_damage(10)

@then("the character should be dead")
def check_dead(context):
    assert context["character"].is_dead()