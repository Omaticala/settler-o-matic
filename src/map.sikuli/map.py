
from sikuli.Sikuli import *

#
# Screen area
# - some areas of screen cannot be used for navigation and search, as they contain game menus and other stuff
# - safe screen area is below:
# +-------------------------------+
# | min       40px top            |
# |       +---------------+       |
# |       |               |       |
# | 140px |  (safe zone)  | 110px |
# | left  |               | right |
# |       +---------------+       |
# |         100px bottom      max |
# +-------------------------------+
#
# Map size:
# - map has fixed size and is surrounded by various width sea
# - for search the position of viewport must be known
# - before each search the position must be re-calibrated
# - beware, that the Y coordinate of map is reversed, compared to Y coordinate of screen
# +-------------------------------+
# | (sea)       340px         max |
# |       +---------------+       |
# |       | (island)      |       |
# | 760px |       ~2210px | 350px |
# |       |   ~3700px     |       |
# |       +---------------+       |
# | min         160px             |
# +-------------------------------+
#

class MapException(Exception):
    pass

class Map:
    "facilitates movement on map and searching of items through all sectors of map"

    def __init__(self):
        "detects map parameters and calibrates map position"
        self.x = 0
        self.y = 0
        self.width = SCREEN.getW()
        self.height = SCREEN.getH()

        self.scrollOverlap = 40
        self.minX = 140
        self.minY = 40
        self.maxX = self.width - 110
        self.maxY = self.height - 100
        self.topLeft = Location(self.minX, self.minY)
        self.topRight = Location(self.maxX, self.minY)
        self.bottomRight = Location(self.maxX, self.maxY)
        self.bottomLeft = Location(self.minX, self.maxY)

        self.stepX = self.maxX - self.minX - self.scrollOverlap
        self.stepY = self.maxY - self.minY - self.scrollOverlap
        self.stepsX = round(3700 / self.stepX, 0)
        self.stepsY = round(2210 / self.stepY, 0)

        self.region = Region(self.minX, self.minY, self.stepX, self.stepY)

        #self.calibrate()
        #self.showUsableArea()
        #self.testMovement()
        
    def showUsableArea(self):
        "uses mouse pointer to show the size of active map area"
        d = Settings.MoveMouseDelay 
        Settings.MoveMouseDelay = 2
        hover(self.topLeft)
        hover(self.topRight)
        hover(self.bottomRight)
        hover(self.bottomLeft)
        hover(self.topLeft)
        Settings.MoveMouseDelay = d
        
        print('screen: ' + str(SCREEN))
        print('usable area: ' + str(self.maxX - self.minX) + 'x' + str(self.maxY - self.minY))

    def calibrate(self):
        "calibrates map position to bottom left corner (sector 1)"
        n = 0
        while not exists(Pattern("bottomLeftCornerSea.png").exact()): 
            self.down()
            self.left()
            n = n + 1
            if n > 8:
                raise MapException("Cannot calibrate map position")
        
        orig = Location(self.bottomLeft.x + 600, self.bottomLeft.y - 250)
        dragDrop(orig, self.bottomLeft)
        self.x = 0
        self.y = 0

    def testMovement(self):
        "tests all map movements"
        self.up()
        self.down()
        self.right()
        self.left()

    def up(self):
        "moves map up by one screen"
        dest = Location(self.bottomRight.x, self.bottomRight.y - self.scrollOverlap)
        dragDrop(self.topRight, dest)
        self.y = self.y + self.stepY
        print('up: ' + str(self.bottomRight.y - dest.y))

    def down(self):
        "moves map down by one screen"
        dest = Location(self.topRight.x, self.topRight.y + self.scrollOverlap)
        dragDrop(self.bottomRight, dest)
        self.y = self.y - self.stepY
        print('down: ' + str(self.bottomRight.y - dest.y))

    def right(self):
        "moves map right by one screen"
        dest = Location(self.topLeft.x + self.scrollOverlap, self.topLeft.y)
        dragDrop(self.topRight, dest)
        self.x = self.x + self.stepX
        print('right: ' + str(self.topLeft.x - dest.x))

    def left(self):
        "moves map left by one screen"
        dest = Location(self.topRight.x - self.scrollOverlap, self.topRight.y)
        dragDrop(self.topLeft, dest)
        self.x = self.x - self.stepX
        print('left: ' + str(self.topLeft.x - dest.x))

    def scanMap(self, callback):
        "scans all screens of the map"
        self.calibrate()
        x = 0
        while x < self.stepsX:
            self._scanMapY()
            self.right()
            x = x + 1
        else:
            self._scanMapY()
            while x > 0:
                self.left()
                x = x - 1

    def _scanMapY(self):
        "scans one column of the map (internal)"
        y = 0
        while y < self.stepsY:
            self.doScan()
            self.up()
            y = y + 1
        else:
            self.doScan()
            while y > 0:
                self.down()
                y = y - 1

    def doScan(self):
        "scans one screen of the map"
        pass



if __name__ == '__main__':
    Settings.MoveMouseDelay = 1 # half speed
    m = Map()
    m.scanMap()
    