Feature: Gestion des personnages

  Scenario: Un nouveau personnage a 10 points de vie
    Given un nouveau personnage
    Then le personnage a 10 points de vie

  Scenario: Un personnage meurt à 0 point de vie
    Given un nouveau personnage
    When le personnage perd toute sa vie
    Then le personnage est mort

  Scenario: Un personnage perd 1 HP quand il est attaqué
    Given un nouveau personnage
    When le personnage est attaqué
    Then le personnage a 9 points de vie

  Scenario: Les HP ne peuvent pas descendre sous zéro
    Given un personnage mort
    When le personnage est attaqué
    Then les HP du personnage sont toujours à 0

  Scenario: Un personnage mort ne peut pas attaquer
    Given un personnage mort
    When le personnage mort tente d'attaquer
    Then une erreur est levée

  Scenario: Un personnage a une endurance de 0 par défaut
    Given un nouveau personnage
    Then son endurance est de 0
