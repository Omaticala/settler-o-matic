
from sikuli.Sikuli import *

from game import *
from menu import *
from supplies import *

#
# game            browser and game window and settings
# maintenance     main automation script
#  - map          navigation on game map
#  - menu         main menu (specialist, buffs, resources)
#  - economy      economy menu
#    + building   represents a single building on the map
#    + comodity   represents a single product in the economy menu
#  - resources    rebuilds fields and wells, feeds fish and deers
#    + builder    constructing new buildings
#    - supplies   creating buffs and resources
#  - buffs        buffs buildings
#    + menu       ... (for buffing)
#    - economy    ... (for opening buildings)
#    - supplies   ... (for creating buffs)
#  - mines        checks and rebuilds mines and quaries
#    + menu       ... (for finding mines)
#    + queue      ... (for planning)
#    + builder    ... (for re-building mines)

g = Game()

#Buildings.Field()
#Supplies.makeFishFood(5)


