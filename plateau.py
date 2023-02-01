"""Module Joueur

Functions:
    * Plateau - Classe représentant un Plateau.
"""

from gobblet import Gobblet, GobbletError


class Plateau:
    """
    Plateau
    """


    def __init__(self, plateau):
        """Constructeur de Plateau

        Vous ne devez PAS modifier cette méthode

        Args:
            plateau (list): Plateau à construire tel que représenté dans l'énoncé
        """
        self.plateau = self.valider_plateau(plateau)


    def valider_plateau(self, plateau):
        """Validateur de Plateau

        Args:
            plateau (list): Plateau tel que représenté dans l'énoncé

        Returns:
            list: Plateau composé de liste de Gobblets ou None pour l'absence de Gobblet

        Raises:
            GobbletError: Le plateau doit être une liste
            GobbletError: Le plateau ne possède pas le bon nombre de lignes
            GobbletError: Le plateau ne possède pas le bon nombre de colonne dans les lignes
            GobbletError: Les Gobblets doivent être des listes de paires ou une liste vide
        """
        if isinstance(plateau, list) is False:
            raise GobbletError("Le plateau doit être une liste")
        if len(plateau) != 4:
            raise GobbletError("Le plateau ne possède pas le bon nombre de ligne")
        plato = []
        for ligne in plateau:
            if len(ligne) != 4:
                raise GobbletError("Le plateau ne possède pas le "
                                   "bon nombre de colonne dans les lignes"
                                    )
            ligne_modif = []
            for case in ligne:
                if len(case) == 0:
                    ligne_modif.append([])
                else:
                    pile = []
                    for gobs in case:
                        if isinstance(gobs, list) is False or (len(gobs) != 2 and len(gobs) != 0):
                            raise GobbletError("Les Gobblets doivent être "
                                       "des listes de paires ou une liste vide"
                                       )
                        pile.append(Gobblet(gobs[1], gobs[0]))
                    ligne_modif.append(pile)
            plato.append(ligne_modif)

        return plato


    def __str__(self):
        """Formater un plateau

        Returns:
            str: Représentation du plateau avec ses Gobblet
        """
        num_ligne = 3
        patron_ligne = ''

        for ligne in self.plateau:
            patron_ligne += str(num_ligne)
            num_case = -1
            for case in ligne:
                num_case += 1
                if case == []:
                    patron_ligne += "   "
                if len(case) >= 1:
                    patron_ligne += case[-1].__str__()
                if num_case == 3 and num_ligne != 0:
                    patron_ligne += "\n ───┼───┼───┼───\n"
                else:
                    if num_ligne == 0 and num_case == 3:
                        patron_ligne += "\n  0   1   2   3 "
                    else:
                        patron_ligne += "|"

            num_ligne -= 1

        return patron_ligne


    def __getitem__(self, index):

        i, j = index
        return self.plateau[i][j]


    def retirer_gobblet(self, no_colonne, no_ligne):
        """Retirer un Gobblet du plateau

        Args:
            no_colonne (int): Numéro de la colonne
            no_ligne (int): Numéro de la ligne

        Returns:
            Gobblet: Gobblet retiré du plateau

        Raises:
            GobbletError: Ligne et colonne doivent être des entiers
            GobbletError: Le numéro de la ligne doit être 0, 1, 2 ou 3
            GobbletError: Le numéro de la colonne doit être 0, 1, 2 ou 3
            GobbletError: Le plateau ne possède pas de Gobblet pour la case demandée
        """
        z = [3, 2, 1, 0]
        if isinstance(no_colonne, int) is False or isinstance(no_ligne, int) is False:
            raise GobbletError("Ligne et colonne doivent être des entiers")
        if not 0 <= no_ligne <= 3:
            raise GobbletError("Le numéro de la ligne doit être 0, 1, 2 ou 3")
        if not 0 <= no_colonne <= 3:
            raise GobbletError("Le numéro de la colonne doit être 0, 1, 2 ou 3")
        if self.plateau[z[no_ligne]][no_colonne] == []:
            raise GobbletError("Le plateau ne possède pas de Gobblet pour la case demandée")

        return self.plateau[z[no_ligne]][no_colonne].pop()


    def placer_gobblet(self, no_colonne, no_ligne, gobblet):
        """Placer un Gobblet dans le plateau

        Args:
            no_colonne (int): Numéro de la colonne (0, 1, 2 ou 3)
            no_ligne (int): Numéro de la ligne (0, 1, 2 ou 3)
            gobblet (Gobblet): Gobblet à placer dans le plateau

        Raises:
            GobbletError: Ligne et colonne doivent être des entiers
            GobbletError: Le numéro de la ligne doit être 0, 1, 2 ou 3
            GobbletError: Le numéro de la colonne doit être 0, 1, 2 ou 3
            GobbletError: Le Gobblet ne peut pas être placé sur la case demandée
        """
        z = [3, 2, 1, 0]
        if isinstance(no_colonne, int) is False or isinstance(no_ligne, int) is False:
            raise GobbletError("Ligne et colonne doivent être des entiers")
        if not 0 <= no_ligne <= 3:
            raise GobbletError("Le numéro de la ligne doit être 0, 1, 2 ou 3")
        if not 0 <= no_colonne <= 3:
            raise GobbletError("Le numéro de la colonne doit être 0, 1, 2 ou 3")

        if self.plateau[z[no_ligne]][no_colonne] != []:
            if self.plateau[z[no_ligne]][no_colonne][-1].grosseur >= gobblet.grosseur:
                raise GobbletError("Le Gobblet ne peut pas être placé sur la case demandée")

        self.plateau[z[no_ligne]][no_colonne].append(gobblet)


    def état_plateau(self):
        """Obtenir l'état du plateau

        Returns:
            list: Liste contenant l'état du plateau tel que représenté dans l'énoncé
        """

        sortie = []
        for ligne in self.plateau:
            sortie_ligne = []
            for case in ligne:
                if case == []:
                    sortie_ligne.append([])
                else:
                    pile = []
                    for gob in case:
                        pile.append(gob.état_gobblet())
                    sortie_ligne.append(pile)
            sortie.append(sortie_ligne)

        return sortie
