
from sikuli.Sikuli import *


class MaintenanceException(Exception):
    pass

class Maintenance:

    def __init__(self, map, game, menu, buffs, mines, economy, supplies, resources):
        self.map = map        
        self.game = game
        self.menu = menu
        self.buffs = buffs
        self.mines = mines
        self.economy = economy
        self.supplies = supplies
        self.resources = resources
        

    def run(self):
        "scan all sectors and create work queue"
        pass

    def scanMap(self):
        self.map.forAllSectors(self.scanSector)
        
    def scanSector(self, region):
        "scan one sector for work to do"
        self.resources.checkRegion(region)
        #self.rebuildMines(region)
        #self.buffBuildings(region)


    