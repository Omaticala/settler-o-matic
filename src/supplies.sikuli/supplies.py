
from sikuli.Sikuli import *


class Supplies:

    def open(self):
        building = find("suppliesBuilding.png")
        click(building)
        click(building) # click lag
    
    def Resources(self):
        self.open()
        tab = find("resourcesTab.png")
        click(tab)

    # deposits ---------------------------------------------------------------
    
    def Deposits(self):
        self.open()
        tab = find("depositsTab.png")
        click(tab)
    
    def makeFishFood(self, count):
        self.Deposits()
        food = find("fishFoodButton.png")
        click(food)
        self.add(count)
        self.ok()

    def makeDeerFood(self, count):
        self.Deposits()
        food = find("deerFoodButton.png")
        click(food)
        self.add(count)
        self.ok()
    
    def add(self, count):
        arrow = find(Pattern("leftArrow.png").similar(0.90))
        while count > 1:
            click(arrow)
            count = count - 1
        
    def ok(self):
        ok = find("okButton.png")
        click(ok)
