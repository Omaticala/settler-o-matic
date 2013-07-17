
from sikuli.Sikuli import *


class Mines:

    def __init__(self, menu, queue, builder):
        self.menu = menu
        self.queue = queue
        self.builder = builder

    def checkMines(self, region):
        "check depleted mines and queue them for rebuilding"
        try:
            mines = region.findAll("emptyMine-1.png")
            while mines.hasNext():
                mine = mines.next()
                self.checkMine(region, mine)
        except FindFailed:
            pass
        try:
            mines = region.findAll(Pattern("emptyQuary.png").similar(0.90))
            while mines.hasNext():
                mine = mines.next()
                self.checkMine(region, mine)
        except FindFailed:
            pass
        print(self.minesToFind)

    def checkMine(self, region, mine):
        "check mine and queue it for rebuilding"
        self.safeClick(mine)
        if region.exists(Pattern("stoneMineIcon.png").similar(0.90)):
            self.minesToFind.append("stone")
        elif region.exists(Pattern("copperMineIcon.png").similar(0.95)):
            self.minesToFind.append("copper")
        elif region.exists(Pattern("marbleMineIcon.png").similar(0.90)):
            self.minesToFind.append("marble")
        elif region.exists(Pattern("ironMineIcon.png").similar(0.95)):
            self.minesToFind.append("iron")
        elif region.exists(Pattern("coalMineIcon.png").similar(0.95)):
            self.minesToFind.append("coal")
        elif region.exists(Pattern("goldMineIcon.png").similar(0.90)):
            self.minesToFind.append("gold")
        closeDialog()
    
    