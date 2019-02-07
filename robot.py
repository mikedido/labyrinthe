# -*-coding:Utf-8 -*

"""Ce module contient la classe Robot."""

class Robot:

    """Classe représentant un robot."""

    def __init__(self, line, column):
        self.line = line
        self.column = column

    def moveSouth(self, caseNumber=1):
        self.line += caseNumber
        pass

    def moveNorth(self, caseNumber=1):
        self.line -= caseNumber
        pass

    def moveWest(self, caseNumber=1):
        self.column -= caseNumber
        pass

    def moveEst(self, caseNumber=1):
        self.column += caseNumber
        pass

    def getLine(self):
        return self.line

    def getColumn(self):
        return self.column