
from sikuli.Sikuli import *

import map
import game
import menu
import buffs
import mines
import economy
import builder
import supplies
import resources

reload(map)
reload(game)
reload(menu)
reload(buffs)
reload(mines)
reload(economy)
reload(builder)
reload(supplies)
reload(resources)

from map import *
from game import *
from menu import *
from buffs import *
from mines import *
from economy import *
from builder import *
from supplies import *
from resources import *


class MaintenanceException(Exception):
    pass

class Maintenance:

    def __init__(self):
        self.game = Game()
        self.map = Map()
        self.menu = Menu()
        self.economy = Economy()
        self.supplies = Supplies()
        self.resources = Resources(self.supplies)
        self.buffs = Buffs(self.economy, self.supplies)
        self.mines = Mines()

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



if __name__ == '__main__':
    m = Maintenance()
    m.scanMap()

    