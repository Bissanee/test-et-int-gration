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

  Scenario: Un duel 2v2 se termine quand une équipe est éliminée
    Given deux équipes de deux personnages
    When le duel est simulé jusqu'à la fin
    Then une équipe a tous ses membres morts

  Scenario: Une équipe avec tous ses membres morts perd le duel
    Given deux équipes de deux personnages
    When le duel est simulé jusqu'à la fin
    Then l'équipe gagnante a au moins un survivant

  Scenario: Un personnage mort ne participe plus au duel
    Given deux équipes de deux personnages
    When le duel est simulé jusqu'à la fin
    Then aucun personnage mort n'a attaqué

  Scenario: Le personnage avec la plus grande AGI attaque en premier
    Given deux équipes de deux personnages avec agilités différentes
    When le duel est simulé pour un seul tour
    Then le premier attaquant est celui avec la plus grande AGI

  Scenario: Les chances d'être attaqué dépendent de CHN
    Given deux cibles avec des CHN différentes
    When on calcule leur poids de ciblage
    Then la cible avec la plus grande CHN a un poids plus faible

  Scenario: Une cible avec moins de 30 pourcents de PV est prioritaire
    Given deux cibles dont une a moins de 30 pourcents de PV
    When on calcule leur poids de ciblage
    Then la cible sous 30 pourcents a un poids plus grand