Feature: Système de combat

  Scenario: Un personnage en attaque un autre
    Given deux personnages
    When l'un attaque l'autre
    Then l'autre perd 1 point de vie
