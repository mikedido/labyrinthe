# -*-coding:Utf-8 -*

"""Ce module contient la classe Carte."""

from labyrinthe import Labyrinthe
from robot import Robot

class Carte:

    """Objet de transition entre un fichier et un labyrinthe."""

    def __init__(self, nom, chaine):
        self.nom = nom
        self.labyrinthe = Labyrinthe(chaine)
        self.robot = self.setRobotPosition()

    def setRobotPosition(self):
        position = self.labyrinthe.getRobotPosition()
        return Robot(position[0], position[1])

    def showLabirinthe(self):
        self.labyrinthe.showGrid()

    def moveRobot(self):
        pass
    
    def __repr__(self):
        return "<Carte {}>".format(self.nom)
