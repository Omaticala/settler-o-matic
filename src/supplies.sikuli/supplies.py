
from sikuli.Sikuli import *


class Supplies:

    def __init__(self, economy):
        self.economy = economy
        
    def open(self):
        location = self.locate()
        click(location)
        hover("something.png")
        click(location) # click lag
        wait(0.3)
        return self

    def locate(self):
        location = exists("suppliesBuilding.png", 0)
        if not location:
            self.economy.Sausages().production().selectBuilding(1)
            wait(0.3)
            location = exists("suppliesBuilding.png", 0)
        return location

    def close(self):
        close = exists("closeButton.png", 0)
        if close:
            click(close)
    
    def Resources(self):
        self.open()
        tab = find("resourcesTab.png")
        click(tab)
        return self

    def Deposits(self):
        self.open()
        tab = find("depositsTab.png")
        click(tab)
        return self

    # buffs ------------------------------------------------------------------

    def makeFishPlate(self, count):
        click(Pattern("fishPlate.png").similar(0.90))
        self.add(count)
        self.clickOk()
        return self

    def makeSandwich(self, count):
        click(Pattern("sandwich.png").similar(0.90))
        self.add(count)
        self.clickOk()
        return self

    def makeBasket(self, count):
        click(Pattern("basket.png").similar(0.90))
        self.add(count)
        self.clickOk()
        return self

    # resources --------------------------------------------------------------

    
    
    # deposits ---------------------------------------------------------------
    
    def makeFishFood(self, count):
        self.Deposits()
        click(Pattern("fishFood.png").similar(0.90))
        self.add(count)
        self.clickOk()
        return self

    def makeDeerFood(self, count):
        self.Deposits()
        click(Pattern("deerFood.png").similar(0.90))
        self.add(count)
        self.clickOk()
        return self

    # common ------------------------------------------------------------------
    
    def add(self, count):
        if count == 25:
            dragDrop("scroller.png", "arrow.png")
        else:
            arrow = find(Pattern("leftArrow.png").similar(0.90))
            while count > 1:
                click(arrow)
                count = count - 1
        
    def clickOk(self):
        click(Pattern("okButton.png").similar(0.90))
