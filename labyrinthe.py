# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""

class Labyrinthe:

    """Classe représentant un labyrinthe."""

    def __init__(self, contenu, obstacles):
        self.grille = {}
        self.Numberline = 0
        self.Numbercolumn = 0
        self.robotPosition = []
        self.setGrid(contenu)
        self.obstacles = obstacles

    """ get obstacles """
    def getObstacles(self):
        return self.obstacles

    """ set the grid"""    
    def setGrid(self, contenu):
        i = 0
        j = 0
        for value in contenu:
            if (value == '\n'):
                i += 1
                j = 0
                pass
            elif (value == '\r'):
                pass
            else:
                if (value == 'X'):
                    self.grille[i, j] = ' '
                    self.robotPosition = (i, j)
                else:
                     self.grille[i, j] = value
                j+=1
        """ Set the number of line and column of the grid"""
        self.Numberline = i
        self.Numbercolumn = j

    """ get the grid"""    
    def getGrid(self):
        return self.grille

    """ show the grid """    
    def showGrid(self, robotLine, robotColumn):
        for i in range(0, self.Numberline):
            showLine = ''
            for j in range(0, self.Numbercolumn):
                if (i == robotLine and j == robotColumn):
                    showLine += 'X'
                else:
                    showLine +=self.grille[(i, j)] 
            print(showLine)

    """ set the position of the robot in the grid """
    def getRobotPosition(self):
        return self.robotPosition