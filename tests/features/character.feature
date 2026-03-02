Feature: Character

  Scenario: A new character has 10 health points
    Given a new character
    Then the character should have 10 health points

  Scenario: A character dies at 0 health
    Given a new character
    When the character loses all health
    Then the character should be dead