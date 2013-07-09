
from sikuli.Sikuli import *


class Builder:

    # currently opened tab
    tab = ""
    
    def open(self):
        if not exists("buildingsTitle.png", 0):
            buildings = find(Pattern("buildingsButton.png").similar(0.80))
            click(buildings)
            wait(0.7)

    def Basic(self):
        self.open()
        if not self.tab == "basic":
            tab = find(Pattern("basicTab.png").similar(0.90))
            click(tab)
            wait(0.3)
            self.tab = "basic"

    def Middle(self):
        self.open()
        if not self.tab == "middle":
            tab = find(Pattern("middleTab.png").similar(0.90))
            click(tab)
            wait(0.3)
            self.tab = "middle"

    def Advanced(self):
        self.open()
        if not self.tab == "advanced":
            tab = find(Pattern("advancedTab.png").similar(0.90))
            click(tab)
            wait(0.3)
            self.tab = "advanced"

    def Expert(self):
        self.open()
        if not self.tab == "expert":
            tab = find(Pattern("expertTab.png").similar(0.90))
            click(tab)
            wait(0.3)
            self.tab = "expert"

    def Tools(self): 
        self.open()
        if not self.tab == "tools":
            tab = find(Pattern("toolsTab.png").similar(0.90))
            click(tab)
            wait(0.3)
            self.tab = "tools"
    
    # basic buildings -------------------------------------------------

    def StoneMine(self):
        self.Basic()
        mine = find("stoneMineButton.png")
        click(mine)

    # middle buildings -------------------------------------------------

    

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
    
    

    # building tools --------------------------------------------
    
        
