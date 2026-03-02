Feature: Combat system

  Scenario: A character attacks another
    Given two characters
    When one character attacks the other
    Then the other character should lose 1 health point
    