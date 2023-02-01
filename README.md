# Gobblet

<img src="https://m.media-amazon.com/images/I/41QOpMfQRRL._AC_SX425_.jpg" style="display: block; margin-left: auto; margin-right: auto;" alt="Squadro" width="50%" height="auto">

## Objectifs

Pour ce projet, vous allez réaliser un premier programme qui interagit avec la **ligne de commande** et qui accède à **Internet**. Vous allez aussi vous familiariser avec la logistique des projets, c'est-à-dire installer sur votre ordinateur un environnement de développement [VS Code](https://code.visualstudio.com/) et vous initier à un logiciel de gestion des révisions [Git](https://git-scm.com/).

## Prérequis

- [Git](https://git-scm.com/downloads/)
- [Python pour macOS](https://www.python.org/downloads/), [Python pour Windows](https://www.microsoft.com/fr-ca/p/python-39/9p7qfqmjrfp7)
- [VS Code](https://code.visualstudio.com/download/)

Avant de télécharger Python ou Git, vous pouvez vérifier s'il est déjà installé sur votre ordinateur depuis un terminal.
Notez que pour Python les version 3.7, 3.8, 3.9, 3.10 seront tous compatible.
Donc si vous avez déjà une de ces versions, inutile d'en installer une autre.

### Windows

Depuis le menu démarré, cherchez Powershell et exécuter la commande:

```powershell
python3 --version
```

Ça devrait afficher `Python 3.9.7` avec le numéro de votre version au lieu de `3.9.7`.

Si ça ne fonctionne pas, essayez la commande:

```powershell
python --version
```

Si aucune de ces 2 commandes fonctionnent, vous devez télécharger Python depuis le Microsoft Store.

Pour Git vous pouvez vérifier avec la commande:

```powershell
git --version
```

### MacOS

Depuis Finder, cherchez `Terminal`, ouvrez l'application puis exécuter la commande:

```zsh
python3 --version
```

Ça devrait afficher `Python 3.9.7` avec le numéro de votre version au lieu de `3.9.7`.

N'utilisez **jamais** la commande `python` sans le `3` sur MacOS car il fera référence à Python 2.

## Extension VS Code

Voici la liste des extensions **VS Code** que nous vous conseillons d'ajouter à votre configuration:

- Python (celui de Microsoft)
- GitLens $-$ Git supercharged
- Live Share (_Pour le dépannage en ligne_)
- Live Share Extension Pack (_Pour le dépannage en ligne_)

## Commandes utile

Exécuter les tests que nous vous avons fournis

```bash
python3 tests.py
```

Installer un module externe **Python**:

```bash
pip3 install nom-du-module
```

Sous MacOS il sera important d'utiliser `pip3` et non pas `pip`.

Créer un bundle depuis un terminal:

```bash
git bundle create gobblet.bundle --all
```

Vérifier que le bundle a été créé avec succès:

```bash
git bundle verify gobblet.bundle
```

Ouvrir un bundle:

```bash
git clone gobblet.bundle
```

**N'oubliez pas de supprimer les fichiers créé lors de l'ouverture du bundle pour ne pas vous embourber de fichiers inutiles.**

## Liens utile

- [Aide-mémoire Github Git](https://github.github.com/training-kit/downloads/fr/github-git-cheat-sheet.pdf)
- [Vidéo explicative du jeu](https://youtu.be/YVxVMa-XSLE)
