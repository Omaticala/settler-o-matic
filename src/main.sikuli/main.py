
import sys
from sikuli.Sikuli import *

myScriptPath = "c:\\http\\omaticala\\settler-o-matic\\src"
if not myScriptPath in sys.path:
    sys.path.append(myScriptPath)

from game import *
from map import *
from queue import *
from menu import *
from economy import *
from buildings import *
from maintenance import *
from supplies import *

g = Game()
g.init()

#map = Map()

#Buildings.Field()
#Supplies.makeFishFood(5)


