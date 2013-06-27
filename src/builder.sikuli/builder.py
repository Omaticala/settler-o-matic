
from sikuli.Sikuli import *


class Builder:
    
    def open(self):
        if not exists("buildingsTitle.png"):
            buildings = find(Pattern("buildingsButton.png").similar(0.80))
            click(buildings)

    # basic buildings -------------------------------------------------

    def Basic(self):
        self.open()
        tab = find(Pattern("basicTab.png").similar(0.90))
        click(tab)

    def StoneMine(self):
        self.Basic()
        mine = find("stoneMineButton.png")
        click(mine)

    # middle buildings -------------------------------------------------

    def Middle(self):
        self.open()
        tab = find(Pattern("middleTab.png").similar(0.90))
        click(tab)

    def CopperMine(self):
        self.Middle()
        mine = find("copperMineButton.png")
        click(mine)

    def Well(self):
        self.Middle()
        well = find("wellButton.png")
        click(well)

    def Field(self):
        self.Middle()
        field = find("fieldButton.png")
        click(field)

    # advanced bildings ----------------------------------------

    def Advanced(self):
        self.open()
        tab = find(Pattern("advancedTab.png").similar(0.90))
        click(tab)

    def MarbleMine(self):
        self.Advanced()
        mine = find("marbleMineButton.png")
        click(mine)

    def IronMine(self):
        self.Advanced()
        mine = find("ironMineButton.png")
        click(mine)

    def CoalMine(self):
        self.Advanced()
        mine = find("coalMineButton.png")
        click(mine)

    def GoldMine(self):
        self.Advanced()
        mine = find("goldMineButton.png")
        click(mine)

    def Well2(self):
        self.Advanced()
        well = find("well2Button.png")
        click(well)

    def Field2(self):
        self.Advanced()
        field = find("field2Button.png")
        click(field)

    # expert buildings -----------------------------------------
    
    def Expert(self):
        self.open()
        tab = find(Pattern("expertTab.png").similar(0.90))
        click(tab)

    # building tools --------------------------------------------
    
    def Tools(self): 
        self.open()
        tab = find(Pattern("toolsTab.png").similar(0.90))
        click(tab)
        
