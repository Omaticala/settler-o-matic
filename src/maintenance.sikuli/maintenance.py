
from sikuli.Sikuli import *

from game import *
from map import *
from queue import *
from build import *
from supplies import *


class MaintenanceException(Exception):
    pass

class Maintenance:

    def __init__(self, map, queue):
        self.map = map
        self.queue = queue
        self.supplies = Supplies()
        self.minesToFind = []
        pass

    def run(self):
        "scan all sectors and create work queue"
        pass
        
    def scanSector(self, region):
        "scan one sector for work to do"
        self.rebuildWells(region)
        self.rebuildFields(region)
        #self.rebuildMines(region)
        #self.buffBuildings(region)

    
    def rebuildFields(self, region):
        "find depleted fields, delete them and build again in the same place"
        try:
            fields = region.findAll(Pattern("emptyField.png").similar(0.50))
            while fields.hasNext():
                field = fields.next()
                self.destroy(field)
                Buildings().Field()
                wait(11) # wait till its destroyed
                click(field)
                wait(5)
                waitVanish("fieldIcon.png")
                # todo: measure time and add to queue
        except FindFailed:
            pass

    def rebuildWells(self, region):
        "find depleted wells, delete them and build again in the same place"
        try:
            wells = region.findAll(Pattern("emptyWell.png").similar(0.90))
            while wells.hasNext():
                well = wells.next()
                self.destroy(well)
                Buildings().Well()
                wait(11) # wait till its destroyed
                click(well)
                wait(5)
                waitVanish("wellIcon.png")
                #todo: measure time and add to queue
        except FindFailed:
            pass

    def destroy(self, building):
        "destroy depleted building (well or field)"
        self.safeClick(building)
        click("bombButton.png")
        ok = wait(Pattern("okButton.png").similar(0.80))
        click(ok)
    
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

    def safeClick(self, building):
        "click() with click-lag prevention (the game sometimes does not react to click on a building)"
        n = 0
        while 1:
            click(building)
            wait(1)
            cross = exists(Pattern("dialogCloseX.png").exact())
            if cross:
                break
            # move the mouse a little bit. prevents click lag
            hover(Location(building.getTarget().getX() + 10, building.getTarget().getY()))
            n = n + 1
            if n > 5:
                raise MaintenanceException("Cannot open building.")

if __name__ == '__main__':
    m = Maintenance(Map(), Queue())
    s = SCREEN
    m.rebuildWells(s)
    m.rebuildFields(s)
    m.checkMines(s)

    