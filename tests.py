"""Tests Gobblet

Ce module contient des tests unitaires pour le projet Gobblet.
"""
from gobblet import Gobblet
from joueur import Joueur
from plateau import Plateau


def test_classe_joueur():
    """Test d'initialisation de la classe Joueur"""
    état_joueur_attendu = {
        "nom": "Alfred",
        "piles": [[1, 3], [1, 3], [1, 3]],
    }

    joueur = Joueur(état_joueur_attendu["nom"], 1, état_joueur_attendu["piles"])

    état_joueur = joueur.état_joueur()

    assert état_joueur == état_joueur_attendu, "Échec du test de la classe Joueur"


def test_classe_gobblet():
    """Test d'initialisation de la classe Gobblet"""
    gobblet_attendu = [1, 2]

    gobblet = Gobblet(gobblet_attendu[1], gobblet_attendu[0])

    état_gobblet = gobblet.état_gobblet()

    assert état_gobblet == gobblet_attendu, "Échec du test de la classe Gobblet"


def test_classe_plateau():
    """Test d'initialisation de la classe Plateau"""
    plateau_attendu = [
        [[], [], [], []],
        [[], [], [2, 3], []],
        [[], [], [], []],
        [[], [], [], []],
    ]

    plateau = Plateau(plateau_attendu)

    état_plateau = plateau.état_plateau()

    assert état_plateau == plateau_attendu, "Échec du test de la classe Plateau"


if __name__ == "__main__":
    test_classe_joueur()
    print("Test d'initialisation de la classe Joueur réussi")
    test_classe_gobblet()
    print("Test d'initialisation de la classe Gobblet réussi")
    test_classe_plateau()
    print("Test d'initialisation de la classe Plateau réussi")
    print("Test de formater_un_jeu réussi")
