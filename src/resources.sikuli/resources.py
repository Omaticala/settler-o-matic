
from sikuli.Sikuli import *

class WaitingException(Exception):
    pass


class Resources:
    "checks resources and refills/rebuilds them"

    # callback for multitasking, when waiting
    callback = 0

    # current region
    region = 0

    def __init__(self, builder, supplies):
        self.builder = builder
        self.supplies = supplies
        self.callback = self.dummy

    def setCallback(self, callback):
        "set multitasking callback"
        self.callback = callback
    
    def multitask(self):
        "give control to multitasking callback"
        if self.callback:
            self.callback(self.region)

    def dummy(self, region):
        print("dummy waiting")
        wait(10)

    def checkRegion(self, region):
        "check all necessities in given region"
        self.region = region
        self.rebuildFields(region)
        self.rebuildWells(region)

    def rebuildFields(self, region):
        "find depleted fields, delete them and build again in the same place"
        try:
            fields = region.findAll(Pattern("emptyField.png").similar(0.47))
            while fields.hasNext():
                field = fields.next()
                self.waitForSocket()
                self.builder.Field()
                click(field)
                # todo: measure time and add to queue
        except FindFailed:
            pass

    def rebuildWells(self, region):
        "find depleted wells, delete them and build again in the same place"
        try:
            wells = region.findAll(Pattern("emptyWell.png").similar(0.75))
            while wells.hasNext():
                well = wells.next()
                self.waitForSocket()
                self.builder.Well()
                click(well)
                #todo: measure time and add to queue
        except FindFailed:
            pass

    def waitForSocket(self):
        "wait till another building socket is free. (uses max 2 of 3 building sockets)"
        self.multitask()
        full = exists(Pattern("buildingQueueCancelButton-1.png").similar(0.95))
        n = 0
        while full:
            wait(10)
            full = exists(Pattern("buildingQueueCancelButton-1.png").similar(0.95))
            n = n + 1
            if n > 60:
                raise WaitingException("Building takes more than 10 minutes.")

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
            if n > 3:
                raise MaintenanceException("Cannot open building.")


if __name__ == '__main__':
    import supplies
    import builder
    reload(supplies)
    reload(builder)
    from supplies import *
    from builder import *
    
    r = Resources(Builder(), Supplies())
    r.checkRegion(SCREEN)
    