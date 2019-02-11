# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os
from carte import Carte
import pickle

#save map
def save_map(carte):
	with open('carte.txt', 'wb') as fichier:
		mon_pickler = pickle.Pickler(fichier)
		mon_pickler.dump(carte)
		fichier.close()

#get map if exist
def get_map():

	carte = None
	if os.path.exists('carte.txt'):
		with open('carte.txt', 'rb') as fichier:
		    mon_pickler = pickle.Unpickler(fichier)
		    carte = mon_pickler.load()
		    fichier.close()

	return carte

#delete saved map
def delete_save_map():
    if os.path.exists('carte.txt'):
        os.remove('carte.txt')
    else:
        print('File not exist')

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
retrive_map = False
if get_map() != None:
    print('recupération carte')
    carteJeu = get_map()
    retrive_map = True

#gestion des erreur de choix de carte
error=1
while error and not retrive_map:
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

    if move.lower() == 'q':
        print('Au revoir!!!')
        quit()
    elif (len(move) == 1):
        move +='1'
    
    carteJeu.moveRobot(move)
    carteJeu.showCarte()

    if carteJeu.checkWin():
        win = True
        delete_save_map()
        print('Félicitation!!! Vous avez gagner !!!')
    else:
        #sauvegarde de la carte
        save_map(carteJeu)
        pass
