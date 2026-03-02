Feature: Character system

  Scenario: A new character has 10 health points
    Given a new character
    Then the character should have 10 health points