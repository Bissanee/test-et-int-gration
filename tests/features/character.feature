Feature: Gestion des personnages

  Scenario: Un nouveau personnage a 10 points de vie
    Given un nouveau personnage
    Then le personnage a 10 points de vie

  Scenario: Un personnage meurt à 0 point de vie
    Given un nouveau personnage
    When le personnage perd toute sa vie
    Then le personnage est mort
