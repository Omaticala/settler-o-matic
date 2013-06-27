
from sikuli.Sikuli import *

import building
reload(building)
from building import *

import comodity
reload(comodity)
from comodity import *

#
# Economy class provides fluent interface. Usage example:
#
#    ec = Economy()                         # does some initial preparations
#    farm = ec.Wheat().selectBuilding(3)    # building object is returned
#
# As coal can be producted in two types of buildings, you must choose if you want to acces the second type:
# 
#    ec = Economy()
#    charcoal = ec.Coal().production(2).selectBuilding(1)
#
#
# Selected building position:
#
#  - normal:       ~380px top, ~300px bottom
#  - fullscreen:   ~380px top, ~390px bottom
#  - small screen: ~370px top, ~130px bottom
#
# Building accessed via Economy is horizontaly centered and allways approximately 380px from top
# (even if the window is too small to show building)
#

class EconomyException(Exception):
    pass

class Economy:
    "Controls the Economy menu"

    # wait for animation before next step
    menuDelay = 0.8

    # economy menu state
    button = 0 # menu section closing button
    menu = ""  # menu section
    scroll = 0 # menu scroll position

    # name and position of comodity for OCR
    comodity = 0

    # currently selected building name 
    building = ""

    # economy window state
    opened = 0
    inProduction = 0

    def __init__(self):

        self.open()
        self.closeAllMenus()
        self.close()
        
    def open(self):
        "open economy menu (if not opened already)"
        if not exists("economyTitle.png", 0):
            click(Pattern("economyIcon.png").similar(0.80))
            print("opening Economy")
            wait(self.menuDelay)
        self.opened = 1

    def close(self):
        close = exists("closeDialog.png", 0)
        if close:
            click(close)
            print("closing Economy")
        self.opened = 0
        
    # menus ---------------------------------------------------------------

    def scrollToTop(self):
        top = exists(Pattern("scrollbarTop-1.png").exact(), 0)
        if top:
            dragDrop(top, Pattern("scrollBarTopArrow.png").similar(0.80))
        self.scroll = 1
        print("scroll to top")

    def scrollToMiddle(self):
        top = exists(Pattern("scrollbarTop-1.png").exact(), 0)
        if top:
            dragDrop(top, Pattern("scrollBarBottom.png").exact())
        self.scroll = 2
        print("scroll to middle")
            
    def scrollToBottom(self):
        bottom = exists(Pattern("scrollBarBottom.png").exact(), 0)
        if bottom:
            dragDrop(bottom, "scrollBarArrowDown.png")
        self.scroll = 3
        print("scroll to bottom")
    
    def closeAllMenus(self):
        "close all menus to ease automated navigatoin (less scrolling)"
        self.scrollToTop()
        
        buildMat = exists(Pattern("buildingMaterialsMenuOpen.png").exact(), 0)
        if buildMat:
            click(buildMat)
            wait(self.menuDelay)
        food = exists(Pattern("foodMenuOpen.png").exact(), 0)
        if food:
            click(food)
            wait(self.menuDelay)
        weapons = exists(Pattern("weaponsMenuOpen.png").exact(), 0)
        if weapons:
            click(weapons)
            wait(self.menuDelay)
        science = exists(Pattern("scienceMenuOpen.png").exact(), 0)
        if science:
            click(science)
            wait(self.menuDelay)
        materials = exists(Pattern("materialsMenuOpen.png").exact(), 0)
        if materials:
            click(materials)
        self.menu = 0
        self.button = 0
        self.scroll = "top"

    def closeCurrentMenu(self):
        self.scrollToTop()
        if self.button:
            click(self.button)
        wait(self.menuDelay)
        self.menu = 0
        self.button = 0

    def openBuildingMaterialsMenu(self):
        self.open()
        if self.menu != "buildmat":
            self.closeCurrentMenu()
        button = find(Pattern("buildingMaterialsMenu.png").similar(0.90))
        click(button)
        wait(self.menuDelay)
        self.button = button
        self.menu = "buildmat"
        print("open buildmat")

    def openFoodMenu(self):
        self.open()
        if self.menu != "food":
            self.closeCurrentMenu()
            button = find(Pattern("foodMenu.png").exact())
            click(button)
            wait(self.menuDelay)
            self.button = button
            self.menu = "food"
            print("open food")

    def openWeaponsMenu(self):
        self.open()
        if self.menu != "weapons":
            self.closeCurrentMenu()
            button = find(Pattern("weaponsMenu.png").exact())
            click(button)
            wait(self.menuDelay)
            self.button = button
            self.menu = "weapons"
            print("open weapons")

    def openScienceMenu(self):
        self.open()
        if self.menu != "science":
            self.closeCurrentMenu()
            button = find(Pattern("scienceMenu.png").exact())
            click(button)
            wait(self.menuDelay)
            self.button = button
            self.menu = "science"
            print("open science")

    def openMaterialsMenu(self, page):
        self.open()
        if self.menu != "materials":
            self.closeCurrentMenu()
            button = find(Pattern("materialsMenu-1.png").exact())
            click(button)
            wait(self.menuDelay)
            self.button = button
            self.menu = "materials"
                    
        if self.scroll == page:
            return
        if page == 1:
            self.scrollToTop()
        elif page == 2:
            self.scrollToMiddle()
        elif page == 3:
            self.scrollToBottom()
        self.scroll = page

        print("open materials")
    
    # building materials ----------------------------------------------------
        
    def PineBoards(self):
        self.openBuildingMaterialsMenu()
        loc = find(Pattern("pineBoard.png").exact())
        click(loc)
        self.comodity = Comodity("PineWood", loc)
        self.building = "PineWoodSawmill"
        return self

    def HardBoards(self):
        self.openBuildingMaterialsMenu()
        loc = find(Pattern("hardBoard.png").exact())
        click(loc)
        self.comodity = Comodity("HardWood", loc)
        self.building = "HardWoodSawmill"
        return self

    def ExoticBoards(self):
        self.openBuildingMaterialsMenu()
        loc = find(Pattern("exoticBoard.png").exact())
        click(loc)
        self.comodity = Comodity("ExoticWood", loc)
        self.building = "ExoticWoodSawmill"
        return self

    def Tools(self):
        self.openBuildingMaterialsMenu()
        loc = find(Pattern("tool.png").exact())
        click(loc)
        self.comodity = Comodity("Tools", loc)
        self.building = "ToolMaker"
        return self

    def Coins(self):
        self.openBuildingMaterialsMenu()
        loc = find(Pattern("coins.png").exact())
        click(loc)
        self.comodity = Comodity("Coins", loc)
        self.building = "Coinage"
        return self

    def Stone(self):
        self.openBuildingMaterialsMenu()
        loc = find(Pattern("stone.png").exact())
        click(loc)
        self.comodity = Comodity("Stone", loc)
        self.building = "StoneMason"
        return self

    def Marble(self):
        self.openBuildingMaterialsMenu()
        loc = find(Pattern("marble.png").exact())
        click(loc)
        self.comodity = Comodity("Marble", loc)
        self.building = "MarbleMason"
        return self

    # food ------------------------------------------------------------------

    def Fish(self):
        self.openFoodMenu()
        loc = find(Pattern("fish.png").exact())
        click(loc)
        self.comodity = Comodity("Fish", loc)
        self.building = "Fisherman"
        return self

    def Beer(self):
        self.openFoodMenu()
        loc = find(Pattern("beer.png").exact())
        click(loc)
        self.comodity = Comodity("Beer", loc)
        self.building = "Brewery"
        return self

    def Sausages(self):
        self.openFoodMenu()
        loc = find(Pattern("sausage.png").exact())
        click(loc)
        self.comodity = Comodity("Sausage", loc)
        self.building = "Butcher"
        return self

    def Bread(self):
        close = self.openFoodMenu()
        loc = find(Pattern("bread.png").exact())
        click(loc)
        self.comodity = Comodity("Bread", loc)
        self.building = "Bakery"
        return self

    # weapons ---------------------------------------------------------------

    def Horses(self):
        close = self.openWeaponsMenu()
        loc = find(Pattern("horse.png").exact())
        click(loc)
        self.comodity = Comodity("Horses", loc)
        self.building = "Stable"
        return self

    def BronzeSwords(self):
        close = self.openWeaponsMenu()
        loc = find(Pattern("bronzeSword.png").exact())
        click(loc)
        self.comodity = Comodity("BronzeWeapons", loc)
        self.building = "BronzeWeaponSmith"
        return self

    def IronSwords(self):
        close = self.openWeaponsMenu()
        loc = find(Pattern("ironSword.png").exact())
        click(loc)
        self.comodity = Comodity("IronWeapons", loc)
        self.building = "IronWeaponSmith"
        return self

    def SteelSwords(self):
        close = self.openWeaponsMenu()
        loc = find(Pattern("steelSword.png").exact())
        click(loc)
        click(Pattern("steelSword2.png").exact())
        self.comodity = Comodity("SteelWeapons", loc)
        self.building = "SteelWeaponSmith"
        return self

    def DamasceneSwords(self):
        close = self.openWeaponsMenu()
        loc = find(Pattern("damasceneSword.png").exact())
        click(loc)
        self.comodity = Comodity("DamasceneWeapons", loc)
        self.building = "DamasceneWeaponSmith"
        return self

    def Bows(self):
        close = self.openWeaponsMenu()
        loc = find(Pattern("bow.png").exact())
        click(loc)
        self.comodity = Comodity("Bows", loc)
        self.building = "BowMaker"
        return self

    def LongBows(self):
        close = self.openWeaponsMenu()
        loc = find(Pattern("longBow.png").exact())
        click(loc)
        click(Pattern("longBow2.png").exact())
        self.comodity = Comodity("LongBows", loc)
        self.building = "LongBowMaker"
        return self

    def CrossBows(self):
        close = self.openWeaponsMenu()
        loc = find(Pattern("crossBow.png").exact())
        click(loc)
        self.comodity = Comodity("CrossBows", loc)
        self.building = "CrossBowMaker"
        return self

    def Cannons(self):
        close = self.openWeaponsMenu()
        loc = find(Pattern("cannon.png").exact())
        click(loc)
        click(Pattern("cannon2.png").exact())
        self.comodity = Comodity("Cannons", loc)
        self.building = "CannonForge"
        return self

    # science ----------------------------------------------------------------

    def SimplePaper(self):
        close = self.openScienceMenu()
        loc = find(Pattern("simplePaper.png").exact())
        click(loc)
        self.comodity = Comodity("SimplePaper", loc)
        self.building = "SimplePaperMill"
        return self

    def IntermediatePaper(self):
        close = self.openScienceMenu()
        loc = find(Pattern("intermediatePaper.png").exact())
        click(loc)
        self.comodity = Comodity("IntermediatePaper", loc)
        self.building = "IntermediatePaperMill"
        return self

    def AdvancedPaper(self):
        close = self.openScienceMenu()
        loc = find(Pattern("advancedPaper.png").exact())
        click(loc)
        self.comodity = Comodity("AdvancedPaper", loc)
        self.building = "AdvancedPaperMill"
        return self

    def Pens(self):
        close = self.openScienceMenu()
        loc = find(Pattern("pen.png").exact())
        click(loc)
        self.comodity = Comodity("Pens", loc)
        self.building = "FineSmith"
        return self

    def Letters(self):
        close = self.openScienceMenu()
        loc = find(Pattern("letter.png").exact())
        click(loc)
        self.comodity = Comodity("Letters", loc)
        self.building = "LetterSmith"
        return self

    def Ornaments(self):
        close = self.openScienceMenu()
        loc = find(Pattern("ornament.png").exact())
        click(loc)
        self.comodity = Comodity("Ornaments", loc)
        self.building = "OrnamentSmith"
        return self

    # materials --------------------------------------------------------------

    def PineWood(self):
        close = self.openMaterialsMenu(1)
        loc = find(Pattern("pineWood.png").exact())
        click(loc)
        self.comodity = Comodity("PineWood", loc)
        self.building = "PineWoodCutter"
        return self

    def HardWood(self):
        close = self.openMaterialsMenu(1)
        loc = find(Pattern("hardWood.png").exact())
        click(loc)
        self.comodity = Comodity("HardWood", loc)
        self.building = "HardWoodCutter"
        return self
        
    def ExoticWood(self):
        close = self.openMaterialsMenu(1)
        loc = find(Pattern("exoticWood.png").exact())
        click(loc)
        self.comodity = Comodity("ExoticWood", loc)
        self.building = "ExoticWoodCutter"
        return self

    def PineTrees(self):
        close = self.openMaterialsMenu(1)
        click(Pattern("pineWood.png").exact())
        click("pineTree.png")
        self.comodity = 0
        self.building = "PineWoodForrester"
        return self

    def HardTrees(self):
        close = self.openMaterialsMenu(1)
        click(Pattern("hardWood.png").exact())
        click("pineTree.png")
        self.comodity = 0
        self.building = "HardWoodForrester"
        return self

    def ExoticTrees(self):
        close = self.openMaterialsMenu(1)
        click(Pattern("exoticWood.png").exact())
        click("pineTree.png")
        self.comodity = 0
        self.building = "ExoticWoodForrester"
        return self

    def Coal(self):
        close = self.openMaterialsMenu(1)
        loc = find(Pattern("coal.png").exact())
        click(loc)
        self.comodity = Comodity("Coal", loc)
        self.building = "CoalMine"
        return self

    def CopperOre(self):
        close = self.openMaterialsMenu(1)
        loc = find(Pattern("copperOre.png").exact())
        click(loc)
        self.comodity = Comodity("CopperOre", loc)
        self.building = "CoperMine"
        return self

    def Copper(self):
        close = self.openMaterialsMenu(1)
        loc = find(Pattern("copper.png").exact())
        click(loc)
        self.comodity = Comodity("Copper", loc)
        self.building = "CopperSmelter"
        return self

    def IronOre(self):
        close = self.openMaterialsMenu(1)
        loc = find(Pattern("ironOre.png").exact())
        click(loc)
        self.comodity = Comodity("IronOre", loc)
        self.building = "IronMine"
        return self

    def Iron(self):
        close = self.openMaterialsMenu(1)
        loc = find(Pattern("iron.png").exact())
        click(loc)
        self.comodity = Comodity("Iron", loc)
        self.building = "IronSmelter"
        return self

    def Steel(self):
        close = self.openMaterialsMenu(2)
        loc = find(Pattern("steel.png").exact())
        click(loc)
        self.comodity = Comodity("Steel", loc)
        self.building = "SteelSmelter"
        return self

    def GoldOre(self):
        close = self.openMaterialsMenu(2)
        loc = find(Pattern("goldOre.png").exact())
        click(loc)
        self.comodity = Comodity("GoldOre", loc)
        self.building = "GoldMine"
        return self

    def Gold(self):
        close = self.openMaterialsMenu(2)
        loc = find(Pattern("gold.png").exact())
        click(loc)
        self.comodity = Comodity("Gold", loc)
        self.building = "GoldSmelter"
        return self

    def TitanOre(self):
        close = self.openMaterialsMenu(2)
        loc = find(Pattern("titanOre.png").exact())
        click(loc)
        self.comodity = Comodity("TitanOre", loc)
        self.building = "TitanMine [N/A]"
        return self

    def Titan(self):
        close = self.openMaterialsMenu(2)
        loc = find(Pattern("titan.png").exact())
        click(loc)
        self.comodity = Comodity("Titan", loc)
        self.building = "TitanSmelter"
        return self

    def Saltpeter(self):
        close = self.openMaterialsMenu(2)
        loc = find(Pattern("saltpeter.png").exact())
        click(loc)
        self.comodity = Comodity("Saltpeter", loc)
        self.building = "SaltpeterMine [N/A]"
        return self

    def GunPowder(self):
        close = self.openMaterialsMenu(2)
        loc = find(Pattern("gunPowder.png").exact())
        click(loc)
        self.comodity = Comodity("GunPowder", loc)
        self.building = "PowderHut"
        return self

    def Granite(self):
        close = self.openMaterialsMenu(2)
        loc = find(Pattern("granite.png").exact())
        click(loc)
        self.comodity = Comodity("Granite", loc)
        self.building = "GraniteMine [N/A]"
        return self

    def Water(self):
        close = self.openMaterialsMenu(3)
        loc = find(Pattern("water.png").exact())
        click(loc)
        self.comodity = Comodity("Water", loc)
        self.building = "Well"
        return self

    def Wheat(self):
        close = self.openMaterialsMenu(3)
        loc = find(Pattern("wheat.png").exact())
        click(loc)
        self.comodity = Comodity("Wheat", loc)
        self.building = "Field"
        return self

    def Meat(self):
        close = self.openMaterialsMenu(3)
        loc = find(Pattern("meat.png").exact())
        click(loc)
        self.comodity = Comodity("Meat", loc)
        self.building = "Hunter"
        return self

    def Flour(self):
        close = self.openMaterialsMenu(3)
        loc = find(Pattern("flour.png").exact())
        click(loc)
        self.comodity = Comodity("Flour", loc)
        self.building = "Mill"
        return self

    def Wheels(self):
        close = self.openMaterialsMenu(3)
        loc = find(Pattern("wheel.png").exact())
        click(loc)
        self.comodity = Comodity("Wheels", loc)
        self.building = "WheelMaker"
        return self

    def Carts(self):
        close = self.openMaterialsMenu(3)
        loc = find(Pattern("cart.png").exact())
        click(loc)
        self.comodity = Comodity("Carts", loc)
        self.building = "Carpenter"
        return self

    # actions --------------------------------------------------------------
    
    def production(self, number = 1):
        "opens production listing from the production chain view"
        self.inProduction = 1
        click(Pattern("comodityIconTopFrame.png").exact().targetOffset(-20,20))
        if number == 1:
            click(Pattern("production.png").exact().targetOffset(-37,36))
        elif number == 2:
            click(Pattern("production.png").exact().targetOffset(-36,87))
            if self.building == "CoalMine":
                self.building = "CharcoalBurner"
        elif number == 3:
            click(Pattern("production.png").exact().targetOffset(-38,134))
        print("open production")
        return self

    def selectBuilding(self, number):
        "selects N-th building in the production list, returns Building object or 0 if there is none"
        if not self.inProduction:
            self.production()
        
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
        else:
            arrow = exists(Pattern("productionScrollBarDownArrow.png").exact())
            if arrow:
                location = find(Pattern("productionTopBorder.png").exact().targetOffset(-32,250))
                # scroll down
                n = 5
                while n < number:
                    # test if there is other building in list
                    if (number - n == 1):
                        end = exists(Pattern("productionScrollBarAtBottom.png").exact(), 0)
                        if end:
                            # no other building
                            return 0
                    n = n + 1
                    click(arrow)
            else:
                # no scroll bar - no building
                return 0
                
        # check if there is actually some building at the location
        if number < 6 and location:
            print("testing slot")
            target = location.getTarget()
            region = Region(target.x - 20, target.y - 20, 40, 40)
            #region.highlight()
            if region.exists(Pattern("emptySlot.png").exact(), 0):
                # the building slot is empty
                return 0

        # select it, finally!
        if location:
            click(location)
            print("building selected")

        self.inProduction = 0
        wait(self.menuDelay)
        b = Building(self.building)
        return b
    

if __name__ == '__main__':
    e = Economy()
    e.open()
    #print(e.Wheat().selectBuilding(11))
    #print(e.Wheat().selectBuilding(12))
    #print(e.HardBoards().selectBuilding(2))
    #print(e.Pens().selectBuilding(1)) 
    #print(e.Pens().selectBuilding(2))
    #stable = e.Horses().selectBuilding(1)
    #print(stable)
    #stable.getBuffTimeout()
    c = e.Horses().comodity
    print(c.getTrend())
    c.getAmount()
            
        