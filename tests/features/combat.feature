Feature: Système de combat

  Scenario: Un personnage en attaque un autre
    Given deux personnages
    When l'un attaque l'autre
    Then l'autre perd 1 point de vie

  Scenario: Deux personnages s'attaquent mutuellement
    Given deux personnages
    When l'un attaque l'autre
    And l'autre riposte
    Then les deux personnages ont 9 points de vie
