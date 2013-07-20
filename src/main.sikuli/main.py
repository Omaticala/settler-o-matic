
from sikuli.Sikuli import *

import gui
import map
import game
import menu
import buffs
import mines
import builder
import economy
import building
import supplies
import resources
import production
import maintenance

reload(gui)
reload(map)
reload(game)
reload(menu)
reload(buffs)
reload(mines)
reload(builder)
reload(economy)
reload(building)
reload(supplies)
reload(resources)
reload(production)
reload(maintenance)

from gui import *
from map import *
from game import *
from menu import *
from buffs import *
from mines import *
from builder import *
from economy import *
from building import *
from supplies import *
from resources import *
from production import *
from maintenance import *

#
# common:
# - Gui          user interface window
# - Game         browser and game window and settings
# - Map          navigation on game map
# - Queue        queue for planned tasks
#
# automation:
# - Maintenance  main automation script
# - Resources    rebuilds fields and wells, feeds fish and deers
# - Supplies     creating buffs and resources in supplies building
# - Buffs        buffs buildings
# - Mines        checks and rebuilds mines and quaries
# 
# game menus:
# - Menu         main menu (specialist, buffs, resources)
# - Builder      constructing new buildings
# - Economy      economy menu
#   - Comodity   represents a single product in the economy menu
#   - Production production buildings submenu of economy
#     - Building represents a single building on the map (selected via Production menu)
#
# yet not used:
# - Adventure
# - Merchant
#
# obsolete:
# - Finder       (replaced with Buffs)
#

class Container:
    "service locator"

    gui = 0
    map = 0
    game = 0
    menu = 0
    buffs = 0
    mines = 0
    builder = 0
    economy = 0
    supplies = 0
    resources = 0
    maintenance = 0

    
    def Gui(self):
        if not self.gui:
            self.gui = Gui()
        return self.gui

    def Map(self):
        if not self.map:
            self.map = Map()
        return self.map

    def Game(self):
        if not self.game:
            self.game = Game()
        return self.game

    def Menu(self):
        if not self.menu:
            self.menu = Menu()
        return self.menu

    def Buffs(self):
        if not self.buffs:
            self.buffs = Buffs(self.Menu(), self.Economy(), self.Game())
        return self.buffs

    def Mines(self):
        if not self.mines:
            self.mines = Mines(self.Menu(), self.Queue(), self.Builder())
        return self.mines

    def Builder(self):
        if not self.builder:
            self.builder = Builder()
        return self.builder

    def Economy(self):
        if not self.economy:
            self.economy = Economy()
        return self.economy

    def Supplies(self):
        if not self.supplies:
            self.supplies = Supplies()
        return self.supplies

    def Resources(self):
        if not self.resources:
            self.resources = Resources()
        return self.resources

    def Maintenance(self):
        if not self.maintenance:
            self.maintenance = Maintenance(self.Map(), self.Game(), self.Menu(), self.Buffs(), self.Mines(), self.Economy(), self.Supplies(), self.Resources())
        return self.maintenance


if __name__ == '__main__':
    c = Container()
    #e = c.Economy()
    #c.Economy().Steel().production().countBuildings()
    #exit()
    #print(c)
    #wait(3600)
    b = c.Buffs()
    while 1:
        b.buffEverything()
    
    
    