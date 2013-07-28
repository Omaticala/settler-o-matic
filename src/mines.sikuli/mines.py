
from sikuli.Sikuli import *

#
# map sectors are as follows:
# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#

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

    def findCopper(self, number):
        # sector 2 ------------------
        exists(Pattern("copper21.png").similar(0.90).targetOffset(24,-10)) # 2/1
        exists(Pattern("copper22.png").similar(0.90).targetOffset(-13,5)) # 2/2
        # 2/3
        # sector 4 ------------------
        exists(Pattern("copper41.png").similar(0.90).targetOffset(4,-2)) # 4/1
        exists(Pattern("copper42.png").similar(0.90).targetOffset(-2,-12)) # 4/2
        exists(Pattern("copper43.png").similar(0.90).targetOffset(24,4)) # 4/3
    
    def findIron(self, number):
        # sector 3 ------------------
        exists(Pattern("iron31.png").similar(0.90).targetOffset(-10,-21)) # 3/1
        exists(Pattern("iron32.png").similar(0.90).targetOffset(-12,28)) # 3/2
        exists(Pattern("oron33.png").similar(0.90).targetOffset(-17,23)) # 3/3
        # sector 5 ------------------
        # 5/1
        exists(Pattern("iron52.png").similar(0.90).targetOffset(0,13)) # 5/2
        exists(Pattern("iron53.png").similar(0.90).targetOffset(-17,7)) # 5/3
        # sector 6 ------------------
        exists(Pattern("iron61.png").similar(0.90).targetOffset(-13,1)) # 6/1
        exists(Pattern("iron62.png").similar(0.90).targetOffset(12,15)) # 6/2
        exists(Pattern("iron63.png").similar(0.90).targetOffset(-4,23)) # 6/3
        exists(Pattern("iron64.png").similar(0.90).targetOffset(-11,28)) # 6/4
        # sector 8 ------------------
        exists(Pattern("iron81.png").similar(0.90).targetOffset(-5,-4)) # 8/1
        exists(Pattern("iron82.png").similar(0.90).targetOffset(2,25)) # 8/2
        exists(Pattern("iron83.png").similar(0.90).targetOffset(-31,17)) # 8/3
        exists(Pattern("iron84.png").similar(0.90).targetOffset(3,-12)) # 8/4
        exists(Pattern("iron85.png").similar(0.90).targetOffset(-7,-17)) # 8/5

    def findCoal(self, number):
        # sector 6 ------------------
        exists(Pattern("coal61.png").similar(0.90).targetOffset(-11,-14)) # 6/1
        exists(Pattern("coal62.png").similar(0.90).targetOffset(-8,-8)) # 6/2
        exists(Pattern("coal63.png").similar(0.90).targetOffset(-12,-9)) # 6/3
        # sector 7 ------------------
        exists(Pattern("coal71.png").similar(0.90).targetOffset(17,13)) # 7/1
        exists(Pattern("coal72.png").similar(0.90).targetOffset(-21,7)) # 7/2
        exists(Pattern("coal73.png").similar(0.90).targetOffset(-23,7)) # 7/3
        
        
    def findGold(self, number):
        # sector 2 ------------------
        exists(Pattern("gold21.png").similar(0.90).targetOffset(-21,-1)) # 2/1
        exists(Pattern("gold22.png").similar(0.90).targetOffset(-6,13)) # 2/2
        exists(Pattern("gold23.png").similar(0.90).targetOffset(-7,-3)) # 2/3
        # sector 9 ------------------
        exists(Pattern("gold91.png").similar(0.90).targetOffset(5,16)) # 9/1
        exists(Pattern("gold92.png").similar(0.90).targetOffset(-15,13)) # 9/2
        exists(Pattern("gold93.png").similar(0.90).targetOffset(-17,0)) # 9/3
        exists(Pattern("gold94.png").similar(0.90).targetOffset(-14,-4)) # 9/4
        exists(Pattern("gold95.png").similar(0.90).targetOffset(-21,-12)) # 9/5
        
    def identifyDeadMine(self):
        "identifies mine position to build here when the resource is found again"
        # sector 2 ------------------
        if exists(Pattern("oldCopper21.png").similar(0.90)):
            return "copper21"
        if exists(Pattern("oldCopper22.png").similar(0.90)):
            return "copper22"
        if exists(Pattern("oldCopper23.png").similar(0.90)):
            return "copper23"
        # gold21
        # gold22
        # gold23
        # sector 3 ------------------
        if exists(Pattern("oldIron31-1.png").similar(0.90)):
            return "iron31"
        if exists(Pattern("oldIron31.png").similar(0.90)):
            return "iron32"
        if exists(Pattern("oldIron33.png").similar(0.90)):
            return "iron33"
        # sector 4 ------------------
        if exists(Pattern("oldCopper41.png").similar(0.90)):
            return "copper41"
        if exists(Pattern("oldCopper42.png").similar(0.90)):
            return "copper42"
        if exists(Pattern("oldCopper43.png").similar(0.90)):
            return "copper43"
        if exists(Pattern("oldIron41.png").similar(0.90)):
            return "iron41"
        if exists(Pattern("oldIron42.png").similar(0.90)):
            return "iron42"
        # sector 5 ------------------
        if exists(Pattern("oldIron51.png").similar(0.90)):
            return "iron51"
        if exists(Pattern("oldIron52.png").similar(0.90)):
            return "iron52"
        if exists(Pattern("oldIron53.png").similar(0.90)):
            return "iron53"
        # sector 6 ------------------
        if exists(Pattern("oldIron61.png").similar(0.90)):
            return "iron61"
        if exists(Pattern("oldIron62.png").similar(0.90)):
            return "iron62"
        if exists(Pattern("oldIron63.png").similar(0.90)):
            return "iron63"
        if exists(Pattern("oldIron64.png").similar(0.90)):
            return "iron64"
        if exists(Pattern("oldCoal61.png").similar(0.90)):
            return "coal61"
        if exists(Pattern("oldCoal62.png").similar(0.90)):
            return "coal62"
        if exists(Pattern("oldCoal63.png").similar(0.90)):
            return "coal63"
        # sector 7 ------------------
        if exists(Pattern("oldCoal71.png").similar(0.90)):
            return "coal71"
        if exists(Pattern("oldCoal72.png").similar(0.90)):
            return "coal72"
        if exists(Pattern("oldCoal73.png").similar(0.90)):
            return "coal73"
        # sector 8 ------------------
        if exists(Pattern("oldIron81.png").similar(0.90)):
            return "iron81"
        if exists(Pattern("oldIron82.png").similar(0.90)):
            return "iron82"
        if exists(Pattern("oldIron83.png").similar(0.90)):
            return "iron83"
        if exists(Pattern("oldIron84.png").similar(0.90)):
            return "iron84"
        if exists(Pattern("oldIron85.png").similar(0.90)):
            return "iron85"
        # sector 9 ------------------
        if exists(Pattern("oldGold91.png").similar(0.90)):
            return "gold91"
        if exists(Pattern("oldGold92.png").similar(0.90)):
            return "gold92"
        if exists(Pattern("oldGold93.png").similar(0.90)):
            return "gold93"
        if exists(Pattern("oldGold94.png").similar(0.90)):
            return "gold94"
        # gold95

    def identifyDeadQuary(self):
        "not needed, as there is no need to rebuild quary"
        # sector 1 ------------------
        # stone11
        # stone12
        # stone13
        # stone14
        # marble11
        # marble12
        # sector 3 ------------------
        # marble31
        # marble32
        # sector 4 ------------------
        # stone41
        # sector 5 ------------------
        # stone51
        # stone52
        # stone53
        # stone54
        # marble51
        # marble52
        # sector 8 ------------------
        # marble81
        # marble82
        # marble83
        # marble84
        # marble85
        