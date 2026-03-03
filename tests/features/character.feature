Feature: Gestion des personnages

  Scenario: Un nouveau personnage a 10 points de vie
    Given un nouveau personnage
    Then le personnage a 10 points de vie
