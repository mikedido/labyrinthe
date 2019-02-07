# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""

class Labyrinthe:

    """Classe représentant un labyrinthe."""

    def __init__(self, contenu):
        self.grille = {}
        self.Numberline = 0
        self.Numbercolumn = 0
        self.setGrid(contenu)

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
                self.grille[i, j] = value
                j+=1
        """ Set the number of line and column of the grid"""
        self.Numberline = i
        self.Numbercolumn = j

    """ get the grid"""    
    def getGrid(self):
        return self.grille

    """ show the grid """    
    def showGrid(self):
        for i in range(0, self.Numberline):
            showLine = ''
            for j in range(0, self.Numbercolumn):
                showLine +=self.grille[(i, j)] 
            print(showLine)
            
    """ get the position of the robot in the grid """
    def getRobotPosition(self):
        for key in self.grille.keys():
            if ('X' == self.grille[key]):
                return key