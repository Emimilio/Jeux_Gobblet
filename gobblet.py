"""Module Gobblet

Attributes:
    GOBBLET_REPRÉSENTATION (dict): Constante représentant les gobelets des joueurs.

Functions:
    * Gobblet - Classe représentant un Gobblet.
    * GobbletError - Classe gérant les exceptions GobbletError.
    * interpréteur_de_commande - Génère un interpréteur de commande.
    * formater_jeu - Formater la représentation graphique d'un jeu.
    * formater_les_parties - Formater la liste des dernières parties.
"""

from argparse import ArgumentParser


# Voici la représentation des Gobblets, n'hésitez pas à l'utiliser.
# 1 pour le joueur 1, 2 pour le joueur 2.
GOBBLET_REPRÉSENTATION = {
    1: [" ▫ ", " ◇ ", " ◯ ", " □ "],
    2: [" ▪ ", " ◆ ", " ● ", " ■ "],
}


class GobbletError(Exception):
    '''Erreur gobblet'''
    def __str__(self):
        return f"GobbletError: {self.args[0]}"


class Gobblet:
    """
    Gobblet
    """


    def __init__(self, grosseur, no_joueur):
        """Constructeur de gobelet.

        Ne PAS modifier cette méthode.

        Args:
            grosseur (int): Grosseur du Gobblet [0, 1, 2, 3].
            no_joueur (int): Numéro du joueur [1, 2].
        """
        self.grosseur, self.no_joueur = self.valider_gobblet(grosseur, no_joueur)


    def valider_gobblet(self, grosseur, no_joueur):
        """Validateur de gobelet.

        Args:
            grosseur (int): la grosseur du gobelet [0, 1, 2, 3].
            no_joueur (int): le numéro du joueur [1, 2].

        Returns:
            tuple[int, int]: un tuple contenant la grosseur et le numéro du joueur.

        Raises:
            GobbletError: La grosseur doit être un entier.
            GobbletError: La grosseur doit être comprise entre 0 et 3.
            GobbletError: Le numéro du joueur doit être un entier.
            GobbletError: Le numéro du joueur doit être 1 ou 2.
        """

        if isinstance(grosseur, int) is False:
            raise GobbletError('La grosseur doit être un entier.')

        if not 0 <= grosseur <= 3:
            raise GobbletError('La grosseur doit être comprise entre 0 et 3.')

        if isinstance(no_joueur, int) is False:
            raise GobbletError('Le numéro du joueur doit être un entier.')

        if no_joueur not in (1,2):
            raise GobbletError('Le numéro du joueur doit être 1 ou 2.')

        return (grosseur, no_joueur)


    def __str__(self):
        """Formater un gobelet.

        Returns:
            str: Représentation du gobelet pour le joueur.
        """
        return GOBBLET_REPRÉSENTATION[self.no_joueur][self.grosseur]


    def __eq__(self, autre):
        """Comparer l'équivalence de deux gobelets.

        Args:
            autre (Gobblet | None): None ou Gobblet à comparer.

        Returns:
            bool: si les deux gobelets sont de même taille.
        """
        if isinstance(self, Gobblet) and isinstance(autre, Gobblet):
            if self.grosseur == autre.grosseur:
                return True
        return False


    def __gt__(self, autre):
        """Comparer la grosseur de deux gobelets.

        Args:
            autre (Gobblet | None): None ou Gobblet à comparer.

        Returns:
            bool: si ce gobelet est plus gros que l'autre.
        """
        return not (self.__lt__(autre) or self.__eq__(autre))


    def __lt__(self, autre):
        """Comparer la grosseur de deux gobelets.

        Args:
            autre (Gobblet | None): None ou Gobblet à comparer.

        Returns:
            bool: si ce gobelet est plus petit que l'autre.
        """
        if isinstance(self, Gobblet) and isinstance(autre, Gobblet):
            if self.grosseur < autre.grosseur:
                return True
        return False


    def __ne__(self, autre):
        """Comparer l'équivalence de deux gobelets.

        Args:
            autre (Gobblet | None): None ou Gobblet à comparer.

        Returns:
            bool: si ce gobelet n'est pas équivalent à l'autre.
        """
        return not self.__eq__(autre)


    def __ge__(self, autre):
        """Comparer la grosseur de deux gobelets.

        Args:
            autre (Gobblet | None): None ou Gobblet à comparer.

        Returns:
            bool: si ce gobelet est plus grand ou égal à l'autre.
        """
        return not self.__lt__(autre)


    def __le__(self, autre):
        """Comparer la grosseur de deux gobelets.

        Args:
            autre (Gobblet | None): None ou Gobblet à comparer.

        Returns:
            bool: si ce gobelet est plus petit ou égal à l'autre.
        """
        return self.__lt__(autre) or self.__eq__(autre)


    def état_gobblet(self):
        """Obtenir l'état du gobelet.

        Returns:
            list: la paire d'entiers représentant l'état du gobelet
            (numéro du joueur et grosseur du gobelet).
        """
        return [self.no_joueur, self.grosseur]


def interpréteur_de_commande():
    """Interpreteur de commande.

    Returns:
        Namespace: Un objet Namespace tel que retourné par parser.parse_args().
                   Cette objet aura l'attribut IDUL représentant l'idul du joueur
                   et l'attribut lister qui est un booléen True/False.
    """

    parser = ArgumentParser(description="Gobblet")

    parser.add_argument(
        'IDUL', metavar='IDUL', help="IDUL du joueur"
    )
    parser.add_argument(
        '-l', '--lister', action='store_true', help="Lister les parties existantes"
    )
    parser.add_argument(
        '-a', '--automatique', action='store_true', help="Activer le mode automatique"
    )
    return parser.parse_args()


def formater_les_parties(parties):
    """Formater une liste de parties.

    L'ordre doit être exactement la même que ce qui est passé en paramètre.

    Args:
        parties (list): une liste des parties.

    Returns:
        str: Représentation des parties.
    """

    k = 0
    games = ''
    indice = 1
    for i in parties:
        k += 1
        if k >= 10:
            indice = 0
        games += f'{k}{indice*" "}: {i["date"]}, {i["joueurs"][0]} vs {i["joueurs"][1]}'
        if i["gagnant"] is not None:
            games += f', gagnant: {i["gagnant"]}\n'
        else:
            games += '\n'
    return games
