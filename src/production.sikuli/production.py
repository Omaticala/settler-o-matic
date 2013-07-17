
from sikuli.Sikuli import *

import building
reload(building)
from building import *

#
# irregular production icon placement:
# - SteelSwords
# - Cannons
# - Carts
#

class Production:

    opened = 0
    
    defaultIconLocation = 0
    irregularIconLocations = ["SteelWeaponSmith", "CannonForgery", "Carpenter"]

    # currently selected building name 
    building = ""

    # buildings counts
    counts = {}
    
    # number of buildings to skip
    skip = 0
    skipName = ""

    def __init__(self, economy):
        self.economy = economy
        self.menuDelay = economy.menuDelay
    
    def open(self, number = 1):
        "opens production listing from the production chain view"
        if self.opened == 1:
            return self
        
        wait(self.menuDelay)
        click(Pattern("comodityIconTopFrame.png").similar(0.95).targetOffset(-20,20))
        if number == 1:
            if self.building not in self.irregularIconLocations:
                click(Pattern("production.png").similar(0.95).targetOffset(-37,36))
            else:
                if not self.defaultIconLocation:
                    self.defaultIconLocation = find(Pattern("production.png").similar(0.95).targetOffset(-37,36))
                click(self.defaultIconLocation)
        elif number == 2:
            click(Pattern("production.png").similar(0.95).targetOffset(-36,87))
            if self.building == "CoalMine":
                self.building = "CharcoalBurner"
        elif number == 3:
            click(Pattern("production.png").similar(0.95).targetOffset(-38,134))
        print("open production")
        return self

    def getProductionBuffRate(self):
        location = find(Pattern("production.png").similar(0.95).targetOffset(-8,30))
        region = Region(location.getX(), location.getY(), 20, 20)
        region.highlight()
        wait(5)
        pass

    def selectBuilding(self, number):
        "selects N-th building in the production list, returns Building object or 0 if there is none"
        location = self.findBuilding(number)
        if not location:
            self.opened = 0
            return 0

        click(location)
        print("building selected")

        self.opened = 0
        wait(self.menuDelay)
        return Building(self.building)

    def selectBuffableBuilding(self, number):
        print("selectBuffableBuilding")
        if self.skipName == self.building:
            skip = self.skip
        else:
            skip = 0
        print("skip:" + skip.__repr__())
        
        location = self.findBuilding(number + skip)
        while location and (self.isBuffed(location) or self.isPaused(location)):
            print("skipping")
            skip += 1
            location = self.findBuilding(number + skip)
        self.skip = skip
        self.skipName = self.building
        print(location.__repr__())

        if not location:
            self.opened = 0
            return 0

        click(location)
        print("building selected")

        self.opened = 0
        wait(self.menuDelay)
        return Building(self.building)

    def findBuilding(self, number):
        print("findBuilding")
        try:
            if number < 6:
                location = self.locateOnFirstPage(number)
            else:
                location = self.locateWithScrolling(number)

        # when comodity has no production
        except FindFailed:
            print("find failed")
            return 0
                
        # check if there is actually some building at the location
        if number < 6 and location:
            print("testing slot")
            if self.isEmpty(location):
                # the building slot is empty
                print("slot is empty")
                return 0

        return location

    def locateOnFirstPage(self, number):
        print("locateOnFirstPage")
        if number == 1:
            location = find(Pattern("productionTopBorder.png").exact().targetOffset(-31,48))
        elif number == 2:
            location = find(Pattern("productionTopBorder.png").exact().targetOffset(-31,100))
        elif number == 3:
            location = find(Pattern("productionTopBorder.png").exact().targetOffset(-30,154))
        elif number == 4:
            location = find(Pattern("productionTopBorder.png").exact().targetOffset(-32,201))
        elif number == 5:
            location = find(Pattern("productionTopBorder.png").exact().targetOffset(-32,250))
        return location

    def locateWithScrolling(self, number, start = 5):
        print("locateWithScrolling")
        wait(0.3)
        arrow = exists(Pattern("productionScrollBarDownArrow.png").exact(), 0)
        if not arrow:
            # no scroll bar - no building
            return 0
        else:
            location = find(Pattern("productionTopBorder.png").exact().targetOffset(-32,250))
            # scroll down
            n = start
            while n < number:
                # test if there is other building in list
                if (n == number - 1):
                    wait(0.3)
                    end = not exists(Pattern("buildingsScrollbarBottomArrow.png").exact(), 0)
                    if end:
                        # no other building
                        return 0
                n += 1
                click(arrow)
        return location

    def isEmpty(self, location):
        print("isEmpty")
        target = location.getTarget()
        region = Region(target.x - 20, target.y - 20, 40, 40)
        return region.exists(Pattern("emptySlot.png").exact(), 0)
        
    def isPaused(self, location):
        print("isPaused")
        target = location.getTarget()
        region = Region(target.x - 30, target.y - 30, 60, 60)
        return region.exists(Pattern("zzz.png").similar(0.50), 0)

    def isBuffed(self, location):
        print("isBuffed")
        target = location.getTarget()
        region = Region(target.x - 30, target.y - 30, 60, 60)
        return region.exists(Pattern("2xStar.png").similar(0.50), 0)

    def countBuildings(self):
        "count all production buildings"
        if self.building in self.counts:
            return self.counts[self.building]
        
        wait(0.1)
        arrow = exists(Pattern("productionScrollBarDownArrow.png").exact(), 0)
        # no scroll bar, count buildings on first page
        if not arrow:
            location = self.locateOnFirstPage(2)
            if self.isEmpty(location):
                location = self.locateOnFirstPage(1)
                if self.isEmpty(location):
                    count = 0
                else:
                    count = 1
            else:
                location = self.locateOnFirstPage(4)
                if self.isEmpty(location):
                    location = self.locateOnFirsPage(3)
                    if self.isEmpty(location):
                        count = 2
                    else:
                        count = 3
                else:
                    location = self.locateOnFirstPage(5)
                    if self.isEmpty(location):
                        count = 4
                    else:
                        count = 5
        # scroll down to count buildings
        else:
            count = 6
            while count < 100:
                click(arrow)
                wait(0.1)
                end = not exists(Pattern("buildingsScrollbarBottomArrow.png").exact(), 0)
                if end:
                    break
                count += 1
        top = exists(Pattern("topArrow.png").similar(0.90).targetOffset(-1,8))
        if top:
            dragDrop(Pattern("scrollbarTop.png").similar(0.90).targetOffset(-4,3), top)
        self.counts[self.building] = count
        return count

