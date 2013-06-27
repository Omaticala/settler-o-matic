
from sikuli.Sikuli import *

import builder
reload(builder)
from builder import *


class Resources:

    def __init__(self, supplies):
        self.builder = Builder()
        self.supplies = supplies

    def checkRegion(self, region):
        self.rebuildFields(region)
        self.rebuildWells(region)

    def rebuildFields(self, region):
        "find depleted fields, delete them and build again in the same place"
        try:
            fields = region.findAll(Pattern("emptyField.png").similar(0.50))
            while fields.hasNext():
                field = fields.next()
                self.destroy(field)
                Build().Field()
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
                Build().Well()
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



    