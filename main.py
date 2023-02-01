"""Jeu Gobblet

Ce programme permet de joueur au jeu Gobblet.
"""
# -*- coding: utf-8 -*-
from pathlib import Path
from api import lister_parties
from gobblet import formater_les_parties, interpréteur_de_commande
from jeu import Jeu




SECRET = "a0534fa0-381a-4372-9bea-53e5834ecb95"


def demander_partie_a_continuer(parties):
    ''' demander partie à continuer '''
    if not parties:
        return None
    while True:
        print(formater_les_parties(parties))
        choix = input("Entrez le numéro de la partie à continuer: ")
        if not choix.isdigit():
            print("Vous devez entrer un nombre.")
            continue
        choix = int(choix)
        if not 1 <= choix <= len(parties):
            print(f"Vous devez entrer un nombre de 1 à {len(parties)}.")
            continue
        return parties[choix - 1]["id"]


def lister_les_parties(idul, secret):
    '''Lister parties '''
    chemin_de_sauvegarde = Path(__file__).parent
    identifiants = []
    parties = []
    if not chemin_de_sauvegarde.exists():
        return parties

    for file in chemin_de_sauvegarde.iterdir():
        identifiants.append(file.stem)

    for partie in lister_parties(idul, secret):
        if partie["id"] not in identifiants:
            continue
        parties.append(partie)

    return parties


if __name__ == "__main__":
    args = interpréteur_de_commande()
    id_partie = None

    if args.lister:
        parties1 = lister_les_parties(args.IDUL, SECRET)
        id_partie = demander_partie_a_continuer(parties1)

    jeu = Jeu(args.IDUL, SECRET, id_partie=id_partie, automatique=args.automatique)
    jeu.jouer()
