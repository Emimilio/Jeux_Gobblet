'''Module pour jouer'''
import json
from gobblet import Gobblet, GobbletError, interpréteur_de_commande
from plateau import Plateau
from joueur import Joueur, Automate
from api import débuter_partie, jouer_coup, récupérer_partie



args = interpréteur_de_commande()


class Jeu:
    '''Classe pour jouer'''
    def __init__(self, idul, secret, id_partie=None, automatique=False):
        if id_partie is None:
            try:
                id_partie, plateau, joueurs = débuter_partie(args.IDUL, secret)
                self.plateau = Plateau(plateau)
            except PermissionError as error:
                raise GobbletError(f"L'IDUL {idul} n'est pas reconnu"
                " par le serveur") from error
            except RuntimeError as error:
                raise GobbletError(f"L'identifiant {id_partie} ne correspond"
                "pas à une partie du joueur {idul}") from error
        else:
            try:
                with open(id_partie+'.json', 'r') as json_file:
                    chaine = json_file.read()
                    plat = json.loads(chaine)
                self.plateau = Plateau(plat.get(id_partie))
                id_partie, plateau, joueurs = récupérer_partie(id_partie, args.IDUL, secret)

                test1 = Automate(joueurs[0].get('nom'), 1, joueurs[0].get('piles'))
                if test1.check_win_global(plateau) == 100:
                    raise GobbletError(f"La partie {id_partie} est terminée")

            except PermissionError as error:
                raise GobbletError(f"L'IDUL {idul} n'est pas reconnu"
                " par le serveur") from error
            except RuntimeError as error:
                raise GobbletError(f"L'identifiant {id_partie} ne correspond pas"
                 "à une partie du joueur {idul}") from error

        if automatique:
            self.joueur1 = Automate(joueurs[0].get('nom'), 1, joueurs[0].get('piles'))
        else:
            self.joueur1 = Joueur(joueurs[0].get('nom'), 1, joueurs[0].get('piles'))

        self.joueur2 = Joueur(joueurs[1].get('nom'), 2, joueurs[1].get('piles'))
        self.secret = secret
        self.id_partie = id_partie

    def __str__(self):
        """Formater un jeu.

        Args:
            plateau (Plateau): le plateau de jeu.
            joueurs (list): la liste des deux Joueurs.

        Returns:
            str: Représentation du jeu.
        """
        indice0 = len(self.joueur1.nom)
        indice1 = len(self.joueur2.nom)
        indice_max = max([indice0, indice1])

        sortie = (f"{indice_max*' '}   0   1   2 \n"
                  f"{(indice_max - indice0) * ' '}{self.joueur1}\n"
                  f"{(indice_max - indice1) * ' '}{self.joueur2}\n\n{self.plateau}"
                )
        return sortie

    def jouer(self):
        '''Méthode pour jouer'''
        while True:
            print(self.__str__())
            if isinstance(self.joueur1, Automate):
                print('')
                origine, destination = self.joueur1.récupérer_le_coup(self.joueur2, self.plateau)
            else:
                origine, destination = self.joueur1.récupérer_le_coup(self.plateau)

            if origine == 'stop' or destination == 'stop':
                dico = {self.id_partie: self.plateau.état_plateau()}
                with open(self.id_partie+'.json', 'w') as json_file:
                    json.dump(dico, json_file)
                break

            if len(str(origine)) == 1:
                gob = self.joueur1.retirer_gobblet(origine)
            else:
                gob = self.plateau.retirer_gobblet(origine[0], origine[1])
            self.plateau.placer_gobblet(destination[0], destination[1], gob)
            try:
                id_partie, plateau, joueurs = jouer_coup(
                    self.id_partie, origine, destination, args.IDUL, self.secret)
                self.id_partie = id_partie
            except StopIteration as stop:
                print(self.__str__())
                print('')
                print('')
                print(f'***** Le gagnant est {stop} *****')
                print('')
                break

            index = 0
            for no_pile, (old, new) in enumerate(zip(self.joueur2.piles, joueurs[1].get('piles'))):
                if not isinstance(old, Gobblet):
                    continue
                if old.grosseur == 0 and len(new) == 0:
                    gob2 = self.joueur2.retirer_gobblet(no_pile)
                    index = 1
                    break
                if old.grosseur != new[1]:
                    gob2 = self.joueur2.retirer_gobblet(no_pile)
                    index = 1
                    break

            for i, (old_line, new_line) in enumerate(zip(self.plateau.plateau, plateau)):
                for j, (old_case, new_case) in enumerate(zip(old_line, new_line)):
                    if index == 1:#c'est que les piles du joueur 2 on été modifier
                        if len(old_case) == 0 and len(new_case) == 0:
                            continue
                        if len(old_case) == 0 and len(new_case) != 0:
                            self.plateau.placer_gobblet(j, 3-i, gob2)
                        if len(old_case) != 0 and len(new_case) != 0:
                            if old_case[-1].grosseur != new_case[1]:
                                self.plateau.placer_gobblet(j, 3-i,gob2)
                    else:#quand le bot du serveur a déplacer un goblet du plateau et non d'une pile
                        gob_enlever = 0
                        if len(old_case) == 0 and len(new_case) == 0:
                            continue
                        if len(old_case) > len(new_case):
                            gob_enlever = self.plateau.retirer_gobblet(j, 3-i)
                            continue
                        if isinstance(gob_enlever, Gobblet) and (len(old_case) < len(new_case)):
                            self.plateau.placer_gobblet(j, 3-i, gob_enlever)
