# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os

from carte import Carte

# On charge les cartes existantes
cartes = []
for nom_fichier in os.listdir("cartes"):
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join("cartes", nom_fichier)
        nom_carte = nom_fichier[:-3].lower()
        with open(chemin, "r") as fichier:
            contenu = fichier.read()
            # Création d'une carte, à compléter
            cartes.append(Carte(nom_carte, contenu))

# On affiche les cartes existantes
print("Labyrinthes existants :")
for i, carte in enumerate(cartes):
    print("  {} - {}".format(i + 1, carte.nom))
# Si il y a une partie sauvegardée, on l'affiche, à compléter



#gestion des erreur de choix de carte
error=1
while error :
    choix = input('Entrez un numéro de labyrinthe pour commencer à jouer :')
    choix = int(choix)
    if (choix > len(cartes) or choix < 1):
        print("Veuillez saisir une valeur correcte entre : {} et {}".format(1, len(cartes))) 
        error =1 
    else:
        error=0
        carteJeu = cartes[choix-1]

#affichage de la carte initial
carteJeu.showCarte()

# gestion des mouvemments 
win = False
while not win:
    move = input ('>')
    if (len(move) == 1):
        move +='1'
    carteJeu.moveRobot(move)
    carteJeu.showCarte()
    if carteJeu.checkWin():
        win = True
        print('Félicitation!!! Vous avez gagner !!!')