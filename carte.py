# -*-coding:Utf-8 -*

"""Ce module contient la classe Carte."""

from labyrinthe import Labyrinthe
from robot import Robot
import pickle

class Carte:

    """Objet de transition entre un fichier et un labyrinthe."""

    def __init__(self, nom, chaine):
        self.nom = nom
        self.labyrinthe = Labyrinthe(chaine, ['O'])
        self.robot = self.setRobotPosition()

    def setRobotPosition(self):
        position = self.labyrinthe.getRobotPosition()
        return Robot(position[0], position[1])

    """ show the labyrinthe with the robot position"""
    def showCarte(self):
        self.labyrinthe.showGrid(self.robot.getLine(), self.robot.getColumn())

    """ manage the ovement on the grid """
    def moveRobot(self, move):
        
        direction = move[0]
        caseNumber = move[1:len(move)]

        if (direction.lower() in ('n', 's', 'w' , 'e') and not caseNumber.isalpha()):
            if (direction.lower() == 'n'):
                if (self.robot.getLine() - int(caseNumber) >= 0):
                    for i in range(1, int(caseNumber)+1):
                        if self.labyrinthe.grille[(self.robot.getLine()-i, self.robot.getColumn())] in self.labyrinthe.getObstacles():
                            return False
                    self.robot.moveNorth(int(caseNumber))
            if (direction.lower() == 's'):
                if (self.robot.getLine() + int(caseNumber) <= self.labyrinthe.Numberline):
                    for i in range(1, int(caseNumber)+1):
                        if self.labyrinthe.grille[(self.robot.getLine()+i, self.robot.getColumn())] in self.labyrinthe.getObstacles():
                            return False
                    self.robot.moveSouth(int(caseNumber))
            if (direction.lower() == 'w'):
                if (self.robot.getColumn() + int(caseNumber) >= 0):
                    for i in range(1, int(caseNumber)+1):
                        if self.labyrinthe.grille[(self.robot.getLine(), self.robot.getColumn()-i)] in self.labyrinthe.getObstacles():
                            return False
                    self.robot.moveWest(int(caseNumber))
            if (direction.lower() == 'e'):
                if (self.robot.getColumn() + int(caseNumber) <= self.labyrinthe.Numbercolumn):
                    for i in range(1, int(caseNumber)+1):
                        if self.labyrinthe.grille[(self.robot.getLine(), self.robot.getColumn()+i)] in self.labyrinthe.getObstacles():
                            return False
                    self.robot.moveEst(int(caseNumber))
        else:
            print('Chemin de direction incorrect : str+int')
        pass
    
    """ chef if the robot get the exit labyrinthe"""
    def checkWin(self):
        if self.labyrinthe.grille[(self.robot.getLine(), self.robot.getColumn())] == 'U':
            return True
        else:
            return False

    def __repr__(self):
        return "<Carte {}>".format(self.nom)
