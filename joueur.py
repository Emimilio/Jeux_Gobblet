"""Module Joueur

Functions:
    * Joueur - Classe représentant un joueur de Gobblet.
"""


from gobblet import Gobblet, GobbletError
from plateau import Plateau


class Joueur:
    """
    Joueur de Gobblet.
    """


    def __init__(self, nom, no_joueur, gobelets):
        """Constructeur de joueur.

        Ne PAS modifier cette méthode.

        Args:
            nom (str): le nom du joueur.
            no_joueur (int): le numéro du joueur (1 ou 2).
            gobelets (list): une liste des trois gobelets disponibles pour ce joueur,
                             par exemple [[1, 1], [], [1, 2]], où la paire [1, 2]
                             représente le numéro du joueur (1) et la grosseur du gobelet (2).
        """
        self.nom, self.no_joueur, self.piles = self.valider_joueur(nom, no_joueur, gobelets)


    def valider_joueur(self, nom, no_joueur, gobelets):
        """Validateur de Joueur.

        Args:
            nom (str): le nom du joueur.
            no_joueur (int): le numéro du joueur (1 ou 2).
            gobelets (list): une liste des trois gobelets disponibles pour ce joueur,
                             par exemple [[1, 1], [], [1, 2]], où la paire [1, 2]
                             représente le numéro du joueur (1) et la grosseur du gobelet (2).

        Returns:
            tuple[str, int, list]: Un tuple contenant
                                    - le nom du joueur;
                                    - son numéro;
                                    - une liste d'objets Gobblet (None pour une pile vide).

        Raises:
            GobbletError: Le nom du joueur doit être une chaine de caractères non vide.
            GobbletError: Le numéro du joueur doit être 1 ou 2.
            GobbletError: Les piles de gobelets doivent être spécifiés sous la forme d'une liste.
            GobbletError: Le joueur doit possèder 3 piles.
            GobbletError: Une pile doit être une liste de deux entiers ou une liste vide.
        """
        if len(nom) == 0:
            raise GobbletError('Le nom du joueur doit être une chaine de caractères non vide.')
        if no_joueur not in [1,2]:
            raise GobbletError("Le numéro du joueur doit être 1 ou 2.")
        if len(gobelets) != 3:
            raise GobbletError("Le joueur doit possèder 3 piles.")
        gobs = []
        for pile in gobelets:
            if isinstance(pile, list) is False:
                raise GobbletError("Les piles de gobelets doivent être "
                                   "spécifiés sous la forme d'une liste."
                                   )
            if len(pile) != 2 and len(pile) != 0:
                raise GobbletError("Une pile doit être une liste "
                                   "de deux entiers ou une liste vide."
                                   )
            if len(pile) == 2:
                if isinstance(pile[0], int) is False or isinstance(pile[1], int) is False:
                    raise GobbletError("Une pile doit être une liste "
                                       "de deux entiers ou une liste vide.")
            if len(pile) == 0:
                gobs.append([])
            else:
                gobs.append(Gobblet(pile[1], pile[0]))

        return (nom, no_joueur, gobs)


    def __str__(self):
        """Formater un joueur.

        Returns:
            str: Représentation du joueur et de ses piles de gobelets.
        """
        sortie = f"{self.nom}: "
        num_gob = 0
        for gob in self.piles:
            if 0 < num_gob < 3:
                sortie += " "
            num_gob += 1
            if gob == []:
                sortie += "   "
            else:
                sortie += gob.__str__()
        return sortie


    def retirer_gobblet(self, no_pile):
        """Retirer un gobelet de la pile.

        Args:
            no_pile (int): le numéro de la pile [0, 1, 2].

        Returns:
            Gobblet: le gobelet retiré de la pile.

        Raises:
            GobbletError: Le numéro de la pile doit être un entier.
            GobbletError: Le numéro de la pile doit être 0, 1 ou 2.
            GobbletError: Le joueur ne possède pas de gobelet pour la pile demandée.
        """
        if isinstance(no_pile, int) is False:
            raise GobbletError("Le numéro de la pile doit être un entier.")
        if no_pile not in [0, 1, 2]:
            raise GobbletError("Le numéro de la pile doit être 0, 1 ou 2.")
        if self.piles[no_pile] == []:
            raise GobbletError("Le joueur ne possède pas de gobelet pour la pile demandée.")
        gob = self.piles[no_pile]
        if self.piles[no_pile].grosseur == 0:
            self.piles[no_pile] = []
        else:
            self.piles[no_pile] = Gobblet(gob.grosseur-1, self.no_joueur)

        return gob


    def placer_gobblet(self, no_pile, gobelets):
        """Placer un gobelet dans la pile.

        Notez que les règles du jeu ne permettent pas de placer un gobelet dans une pile,
        sauf au début de la partie pour l'initialiser.

        L'emplacement de la pile doit donc être libre (valeur `None`).

        Args:
            no_pile (int): le numéro de la pile [0, 1, 2].
            gobelets (Gobblet): le gobelet à placer dans la pile.

        Raises:
            GobbletError: Le numéro de la pile doit être un entier.
            GobbletError: Le numéro de la pile doit être 0, 1 ou 2.
            GobbletError: Le gobelet doit appartenir au joueur.
            GobbletError: Vous ne pouvez pas placer un gobelet à cet emplacement.
        """
        if isinstance(no_pile, int) is False:
            raise GobbletError("Le numéro de la pile doit être un entier.")
        if not 0 <= no_pile <= 2:
            raise GobbletError("Le numéro de la pile doit être 0, 1 ou 2.")
        if gobelets.no_joueur != self.no_joueur:
            raise GobbletError("Le gobelet doit appartenir au joueur.")
        if self.piles[no_pile] is not None:
            if gobelets.grosseur <= self.piles[no_pile].grosseur:
                raise GobbletError("Vous ne pouvez pas placer un gobelet à cet emplacement.")
        self.piles.append(gobelets)


    def récupérer_le_coup(self, plateau):
        """Récupérer le coup

        Demande au joueur le coup à jouer.
        Cette méthode ne doit PAS modifier le plateau.
        Cette méthode ne doit PAS modifier les piles de Gobblets.

        Returns:
            tuple: Un tuple composé d'une origine et de la destination.
                L'origine est soit un entier représentant le numéro de la pile du joueur
                ou une liste de 2 entier [x, y] représentant le gobelet sur le plateau.
                La destination est une liste de 2 entiers [x, y] représentant le gobelet
                sur le plateau.

        Raises:
            GobbletError: L'origine doit être un entier ou une liste de 2 entiers.
            GobbletError: L'origine n'est pas une pile valide.
            GobbletError: L'origine n'est pas une case valide du plateau.
            GobbletError: L'origine ne possède pas de gobelet.
            GobbletError: Le gobelet d'origine n'appartient pas au joueur.
            GobbletError: La destination doit être une liste de 2 entiers.
            GobbletError: La destination n'est pas une case valide du plateau.

        Examples:
            Quel gobelet voulez-vous déplacer:
            Donnez le numéro de la pile (p) ou la position sur le plateau (x,y): 0
            Où voulez-vous placer votre gobelet (x,y): 0,1

            Quel Gobbgobeletlet voulez-vous déplacer:
            Donnez le numéro de la pile (p) ou la position sur le plateau (x,y): 2,3
            Où voulez-vous placer votre gobelet (x,y): 0,1
        """
        print("Quel gobelet voulez-vous déplacer:")
        origin = input('Donnez le numéro de la pile (p) ou la position sur le plateau (x,y): ')
        if origin =='stop':
            return (origin, origin)
        desti = input('Où voulez-vous placer votre gobelet (x,y): ')
        z = [3, 2, 1, 0]
        if desti == 'stop':
            return (desti, desti)

        if len(desti) != 3:
            raise GobbletError("La destination doit être une liste de 2 entiers.")
        if desti[0].isdigit() is False or desti[2].isdigit() is False or desti[1] != ',':
            raise GobbletError("La destination doit être une liste de 2 entiers.")

        destination = [int(desti[0]), int(desti[2])]

        if destination[0] not in [0, 1, 2, 3] or destination[1] not in [0, 1, 2, 3]:
            raise GobbletError("La destination n'est pas une case valide du plateau.")


        if len(origin) != 3 and len(origin) != 1:
            raise GobbletError("L'origine doit être un entier ou une liste de 2 entiers.")

        if len(origin) == 1:

            if origin.isdigit() is False:
                raise GobbletError("L'origine doit être un entier ou une liste de 2 entiers.")

            origin = int(origin)

            if origin not in [0, 1, 2]:
                raise GobbletError("L'origine n'est pas une pile valide.")
            if self.piles[origin] == []:
                raise GobbletError("L'origine ne possède pas de gobelet.")

            return (origin, destination)

        if (origin[0].isdigit() is False or origin[2].isdigit() is False) or origin[1] != ',':
            raise GobbletError("L'origine doit être un entier ou une liste de 2 entiers.")
        origin = [int(origin[0]), int(origin[2])]
        if origin[0] not in [0, 1, 2, 3] or origin[1] not in [0, 1, 2, 3]:
            raise GobbletError("L'origine n'est pas une case valide du plateau.")
        if plateau.plateau[z[origin[1]]][origin[0]] == []:
            raise GobbletError("L'origine ne possède pas de gobelet.")
        if plateau.plateau[z[origin[1]]][origin[0]][-1].no_joueur != self.no_joueur:
            raise GobbletError("Le gobelet d'origine n'appartient pas au joueur.")

        return (origin, destination)


    def état_joueur(self):
        """Obtenir l'état du joueur

        Returns:
            dict: Dictionnaire contenant l'état du joueur tel que représenté dans l'énoncé
        """
        sortie = []
        for pile in self.piles:
            if pile == []:
                sortie.append([])
            else:
                sortie.append(pile.état_gobblet())

        return {'nom' : self.nom, 'piles' : sortie}


class Automate(Joueur):
    """Classe pour l'automate"""

    def check_win_global(self, plateau):
        '''
        Vérifie s'il y a un gagnant
        si oui la fonction retourne 100
        Args:
           plateau:(list)
        '''

        if self.no_joueur == 1:
            other_num = 2
        else:
            other_num = 1

        plato = []
        #etap 1 créer une list avec le num des joueur
        for ligne in plateau:
            sortie = []
            for case in ligne:
                if len(case) == 0:
                    sortie.append([])
                else:
                    sortie.append(case[0])
            plato.append(sortie)

        #check win in the lines
        for ligne in plato:
            streak1 = ligne.count(self.no_joueur)
            streak2 = ligne.count(other_num)
            if streak1 == 4 or streak2 == 4:
                return 100

        rotate_plat = list(zip(*plato[::-1]))
        #check win in colonne
        for ligne in rotate_plat:
            streak1 = ligne.count(self.no_joueur)
            streak2 = ligne.count(other_num)
            if streak1 == 4 or streak2 == 4:
                return 100

        #check win in diagonal
        diago1 = [plato[0][0], plato[1][1], plato[2][2], plato[3][3]]
        diago2 = [plato[3][0], plato[2][1], plato[1][2], plato[0][3]]

        for diag in [diago1, diago2]:
            streak1 = diag.count(self.no_joueur)
            streak2 = diag.count(other_num)
            if streak1 == 4 or streak2 == 4:
                return 100

    def chose_origine(self):
        '''
        Choisi un origine dans les piles du joueur.
        (il prend le goblet le plus gros dans les piles)
        si les pile sont vide None est retourner
        si un goblet valid est trouver,
        un dictionnair avec le goblet la pile et la grosseur
        est retourner
        '''

        gobs = {'gob': 0, 'pile': 0, 'grosseur': -1}

        for num_piles, pile in enumerate(self.piles):
            if not isinstance(pile, Gobblet):
                continue
            if pile.grosseur > gobs.get('grosseur'):
                gobs['pile'] = num_piles
                gobs["grosseur"] = pile.grosseur
                gobs['gob'] = pile

        if gobs.get('grosseur') != -1:
            return gobs
        return None

    def chose_origine_plat(self, plateau):
        '''
        Choisir un goblet d'origine dans le plateau
        (utiliser si les piles sont vides ou
        si les goblet dans les piles ne peuve pas mené
        a une meilleur position)
        args:
            plateau: (Plateau)
        '''

        gobs = {'gob': 0, 'j,i': 0, 'grosseur': -1}
        i = 4
        for ligne in plateau.plateau:
            i -= 1
            for j, case in enumerate(ligne):
                if len(case) == 0:
                    continue
                if case[-1].no_joueur == self.no_joueur and case[-1].grosseur == 3:
                    gobs['gob'] = case[-1]
                    gobs['j,i'] = [j, i]
                    gobs['grosseur'] = 3
                    return gobs

    def valid_moves(self, plateau, indice=True):
        '''
        Retourne un touple composer d'une liste des coup possible à fair
        en fonction de l'origine choisie. Le deuxième element dans le tuple
        retourné est l'origine choisie.
        'plateau' est un instance de la classe Plateau
        'indice' est un bool qui indique si l'on veut que notre origine
        sois un goblet dans les piles ou le plateau
        '''

        if indice:
            origine = self.chose_origine()
            if origine is None:
                origine = self.chose_origine_plat(plateau)
        else:
            origine = self.chose_origine_plat(plateau)
        moves = []
        i = 4
        for line in plateau.plateau:
            i -= 1
            for j, case in enumerate(line):
                if len(case) == 0:
                    moves.append([j, i])
                    continue
                if case[-1].grosseur < origine.get('grosseur'):
                    moves.append([j, i])
        return (moves, origine)

    def check_win(self, plateau):
        '''
        Vérifier si le joueur self gagne
        s'il gange (return 100) mais s'il ne gagne pas
        return une valeur associer a la position actuel
        du plateau
        Args:
            plateau:(Plateau)
        '''

        if self.no_joueur == 1:
            other_num = 2
        else:
            other_num = 1

        plato = []
        #etap 1 créer une list avec le num des joueur
        for ligne in plateau.plateau:
            sortie = []
            for case in ligne:
                if len(case) == 0:
                    sortie.append([])
                else:
                    sortie.append(case[-1].no_joueur)
            plato.append(sortie)
        #check win in the lines
        line_streak = [0]
        for ligne in plato:
            streak = ligne.count(self.no_joueur)
            if streak == 4:
                return 100
            if ligne.count(other_num) != 0:
                continue
            line_streak.append(streak)

        rotate_plat = list(zip(*plato[::-1]))
        #check win in colonne
        col_streak = [0]
        for ligne in rotate_plat:
            streak = ligne.count(self.no_joueur)
            if streak == 4:
                return 100
            if ligne.count(other_num) != 0:
                continue
            col_streak.append(streak)

        #check win in diagonal
        diago1 = [plato[0][0], plato[1][1], plato[2][2], plato[3][3]]
        diago2 = [plato[3][0], plato[2][1], plato[1][2], plato[0][3]]

        diag_streak = [0]
        for diag in [diago1, diago2]:
            streak = diag.count(self.no_joueur)
            if streak == 4:
                return 100
            if diag.count(other_num) != 0:
                continue
            diag_streak.append(streak)

        all_streak = max(diag_streak) + max(col_streak) + max(line_streak)
        return all_streak

    def récupérer_le_coup(self, other, plateau):
        '''
        Vérifier la valeur associer a chaque coup valide
        prendre le coup qui donne la meilleur
        position future
        (nous testons uniquement un coup a l'avance)

        Args:
            other:(self.joueur2)
            plateau:(Plateau)
        '''

        moves, origine = self.valid_moves(plateau)
        other_player = Automate(other.nom, other.no_joueur, other.état_joueur().get('piles'))

        copy_plat = plateau.état_plateau()
        other_posi = other_player.check_win(plateau)
        my_posi = self.check_win(plateau)
        if my_posi == 100 or other_posi == 100:
            raise GobbletError('La partie est terminée.')

        best_moves = {}
        if origine.get('pile') is not None:#tester quand l'origine est une pile
            best_moves = {}
            for move in moves:
                reset_plat = Plateau(copy_plat)
                reset_plat.placer_gobblet(move[0], move[1], origine.get('gob'))
                futur_posi = self.check_win(reset_plat)
                other_futur_posi = other_player.check_win(reset_plat)

                if (futur_posi - (other_futur_posi/2)) >= (my_posi - (other_posi/2)):
                    best_moves[tuple(move)] = (futur_posi - (other_futur_posi/2))

        if len(best_moves) > 0:
            #aller chercher meilleur coup
            best = max(best_moves.values())
            my_move = []
            for key, val in best_moves.items():
                if val == best:
                    my_move = list(key)
                    break

            return (origine.get('pile'), my_move)

        #quand l'origine est dans le plateau ou que l'origine de
        # la pile ne donne jamais de meilleur position
        if origine.get('j,i') is None:
            moves, origine = self.valid_moves(plateau, indice=False)
        for move in moves:
            if move == origine.get('j,i'):
                continue
            reset_plat = Plateau(copy_plat)
            gob = reset_plat.retirer_gobblet(origine.get('j,i')[0], origine.get('j,i')[1])
            reset_plat.placer_gobblet(move[0], move[1], gob)
            futur_posi = self.check_win(reset_plat)
            other_futur_posi = other_player.check_win(reset_plat)
            if (futur_posi - (other_futur_posi/2)) >= (my_posi-(other_posi/2)):
                best_moves[tuple(move)] = (futur_posi - (other_futur_posi/2))

        best = max(best_moves.values())
        my_move = []
        for key, val in best_moves.items():
            if val == best:
                my_move = list(key)
                break

        return (origine.get('j,i'), my_move)
