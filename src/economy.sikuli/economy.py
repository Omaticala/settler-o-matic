
from sikuli.Sikuli import *

# building centering:
# normal:     ~380px top, ~300px bottom
# fullscreen: ~380px top, ~390px bottom
# small:      ~370px top, ~130px bottom
#
# bilding accessed via economy is horizontaly centered and allways approximately 380px from top
# (even if the window is too small to show building)


class Economy:

    def __init__(self):
        self.menuDelay = 0.8
        self.closeMenus()
        wait(self.menuDelay)
    
    def open(self):
        "open economy menu (if not opened already)"
        
        if not exists("economyTitle.png", 0):
            click(Pattern("economyIcon.png").similar(0.80))
            wait(self.menuDelay)
 
    def openMenus(self):
        "[deprecated]"
        materials = exists(Pattern("materialsMenu-1.png").similar(0.90), 0)
        science = exists(Pattern("scienceMenu.png").similar(0.90), 0)
        weapons = exists(Pattern("weaponsMenu.png").similar(0.90), 0)
        food = exists(Pattern("foodMenu.png").similar(0.90), 0)
        buildingMat = exists(Pattern("buildingMaterialsMenu.png").similar(0.90), 0)
        
        if materials:
            click(materials)
        if science:
            click(science)
        if weapons:
            click(veapons)
        if food:
            click(food)
        if buildingMat:
            click(buildingMat)

    def scrollToTop(self):
        top = exists(Pattern("scrollbarTop-1.png").exact(), 0)
        if top:
            dragDrop(top, Pattern("scrollBarTopArrow.png").exact())

    def scrollToMiddle(self):
        top = exists(Pattern("scrollbarTop-1.png").exact(), 0)
        if top:
            dragDrop(top, Pattern("scrollBarBottom.png").exact())
            
    def scrollToBottom(self):
        bottom = exists(Pattern("scrollBarBottom.png").exact(), 0)
        if bottom:
            dragDrop(bottom, "scrollBarArrowDown.png")
    
    def closeMenus(self):
        "close all menus to ease automated navigatoin (less scrolling)"
        self.open()
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

    # building materials ----------------------------------------------------
    
    def openBuildingMaterialsMenu(self):
        self.open()
        button = find(Pattern("buildingMaterialsMenu.png").similar(0.90))
        click(button)
        wait(self.menuDelay)
        return button
        
    def openPineBoards(self):
        close = self.openBuildingMaterialsMenu()
        click(Pattern("pineBoard.png").exact())
        click(close)
        click(Pattern("pineBoard2.png").exact())
        self.production()

    def openHardBoards(self):
        close = self.openBuildingMaterialsMenu()
        click(Pattern("hardBoard.png").exact())
        click(close)
        click(Pattern("hardBoard2.png").exact())
        self.production()

    def openExoticBoards(self):
        close = self.openBuildingMaterialsMenu()
        click(Pattern("exoticBoard.png").exact())
        click(close)
        click(Pattern("exoticBoard2.png").exact())
        self.production()

    def openTools(self):
        close = self.openBuildingMaterialsMenu()
        click(Pattern("tool.png").exact())
        click(close)
        click(Pattern("tool2.png").exact())
        self.production()

    def openCoins(self):
        close = self.openBuildingMaterialsMenu()
        click(Pattern("coins.png").exact())
        click(close)
        click(Pattern("coins2.png").exact())
        self.production()

    def openStone(self):
        close = self.openBuildingMaterialsMenu()
        click(Pattern("stone.png").exact())
        click(close)
        click(Pattern("stone2.png").exact())
        self.production()

    def openMarble(self):
        close = self.openBuildingMaterialsMenu()
        click(Pattern("marble.png").exact())
        click(close)
        click(Pattern("marble2.png").exact())
        self.production()

    # food ------------------------------------------------------------------

    def openFoodMenu(self):
        self.open()
        button = find(Pattern("foodMenu.png").exact())
        click(button)
        wait(self.menuDelay)
        return button

    def openFish(self):
        close = self.openFoodMenu()
        click(Pattern("fish.png").exact())
        click(close)
        click(Pattern("fish2.png").exact())
        self.production()

    def openBier(self):
        close = self.openFoodMenu()
        click(Pattern("beer.png").exact())
        click(close)
        click(Pattern("beer2.png").exact())
        self.production()

    def openSausages(self):
        close = self.openFoodMenu()
        click(Pattern("sausage.png").exact())
        click(close)
        click(Pattern("sausage2.png").exact())
        self.production()

    def openBread(self):
        close = self.openFoodMenu()
        click(Pattern("bread.png").exact())
        click(close)
        click(Pattern("bread2.png").exact())
        self.production()

    # weapons ---------------------------------------------------------------

    def openWeaponsMenu(self):
        self.open()
        button = find(Pattern("weaponsMenu.png").exact())
        click(button)
        wait(self.menuDelay)
        return button

    def openHorses(self):
        close = self.openWeaponsMenu()
        click(Pattern("horse.png").exact())
        click(close)
        click(Pattern("horse2.png").exact())
        self.production()

    def openBronzeSwords(self):
        close = self.openWeaponsMenu()
        click(Pattern("bronzeSword.png").exact())
        click(close)
        click(Pattern("bronzeSword2.png").exact())
        self.production()

    def openIronSwords(self):
        close = self.openWeaponsMenu()
        click(Pattern("ironSword.png").exact())
        click(close)
        click(Pattern("ironSword2.png").exact())
        self.production()

    def openSteelSwords(self):
        close = self.openWeaponsMenu()
        click(Pattern("steelSword.png").exact())
        click(close)
        click(Pattern("steelSword2.png").exact())
        self.production()

    def openDamasceneSwords(self):
        close = self.openWeaponsMenu()
        click(Pattern("damasceneSword.png").exact())
        click(close)
        click(Pattern("damasceneSword2.png").exact())
        self.production()

    def openBows(self):
        close = self.openWeaponsMenu()
        click(Pattern("bow.png").exact())
        click(close)
        click(Pattern("bow2.png").exact())
        self.production()

    def openLongBows(self):
        close = self.openWeaponsMenu()
        click(Pattern("longBow.png").exact())
        click(close)
        click(Pattern("longBow2.png").exact())
        self.production()

    def openCrossBows(self):
        close = self.openWeaponsMenu()
        click(Pattern("crossBow.png").exact())
        click(close)
        click(Pattern("crossBow2.png").exact())
        self.production()

    def openCannons(self):
        close = self.openWeaponsMenu()
        click(Pattern("cannon.png").exact())
        click(close)
        click(Pattern("cannon2.png").exact())
        self.production()

    # science ----------------------------------------------------------------

    def openScienceMenu(self):
        self.open()
        button = find(Pattern("scienceMenu.png").exact())
        click(button)
        wait(self.menuDelay)
        return button

    def openSimplePaper(self):
        close = self.openScienceMenu()
        click(Pattern("simplePaper.png").exact())
        click(close)
        click(Pattern("simplePaper2.png").exact())
        self.production()

    def openIntermediatePaper(self):
        close = self.openScienceMenu()
        click(Pattern("intermediatePaper.png").exact())
        click(close)
        click(Pattern("intermediatePaper2.png").exact())
        self.production()

    def openAdvancedPaper(self):
        close = self.openScienceMenu()
        click(Pattern("advancedPaper.png").exact())
        click(close)
        click(Pattern("advancedPaper2.png").exact())
        self.production()

    def openPens(self):
        close = self.openScienceMenu()
        click(Pattern("pen.png").exact())
        click(close)
        click(Pattern("pen2.png").exact())
        self.production()

    def openLetters(self):
        close = self.openScienceMenu()
        click(Pattern("letter.png").exact())
        click(close)
        click(Pattern("letter2.png").exact())
        self.production()

    def openOrnaments(self):
        close = self.openScienceMenu()
        click(Pattern("ornament.png").exact())
        click(close)
        click(Pattern("ornament2.png").exact())
        self.production()

    # materials --------------------------------------------------------------

    def openMaterialsMenu(self, page):
        "opens menu and returns button position to close it"
        self.open()
        button = find(Pattern("materialsMenu-1.png").exact())
        click(button)
        wait(self.menuDelay)
        if page == 2:
            self.scrollToMiddle()
        elif page == 3:
            self.scrollToBottom()
        return button

    def openPineWood(self):
        close = self.openMaterialsMenu(1)
        click(Pattern("pineWood.png").exact())
        click(close)
        click(Pattern("pineWood2.png").exact())
        self.production()

    def openHardWood(self):
        close = self.openMaterialsMenu(1)
        click(Pattern("hardWood.png").exact())
        click(close)
        click(Pattern("hardWood2.png").exact())
        self.production()
        
    def openExoticWood(self):
        close = self.openMaterialsMenu(1)
        click(Pattern("exoticWood.png").exact())
        click(close)
        click(Pattern("exoticWood2.png").exact())
        self.production()

    def openPineTrees(self):
        close = self.openMaterialsMenu(1)
        click(Pattern("pineWood.png").exact())
        click(close)
        click("pineTree.png")

    def openHardTrees(self):
        close = self.openMaterialsMenu(1)
        click(Pattern("hardWood.png").exact())
        click(close)
        click("pineTree.png")
        self.production()

    def openExoticTrees(self):
        close = self.openMaterialsMenu(1)
        click(Pattern("exoticWood.png").exact())
        click(close)
        click("pineTree.png")
        self.production()

    def openCoal(self):
        close = self.openMaterialsMenu(1)
        click(Pattern("coal.png").exact())
        click(close)
        click(Pattern("coal2.png").exact())
        self.production()

    def openCopperOre(self):
        close = self.openMaterialsMenu(1)
        click(Pattern("copperOre.png").exact())
        click(close)
        click(Pattern("copperOre2.png").exact())
        self.production()

    def openCopper(self):
        close = self.openMaterialsMenu(1)
        click(Pattern("copper.png").exact())
        click(close)
        click(Pattern("copper2.png").exact())
        self.production()

    def openIronOre(self):
        close = self.openMaterialsMenu(1)
        click(Pattern("ironOre.png").exact())
        click(close)
        click(Pattern("ironOre2.png").exact())
        self.production()

    def openIron(self):
        close = self.openMaterialsMenu(1)
        click(Pattern("iron.png").exact())
        click(close)
        click(Pattern("iron2.png").exact())
        self.production()

    def openSteel(self):
        close = self.openMaterialsMenu(2)
        click(Pattern("steel.png").exact())
        self.scrollToTop()
        click(close)
        click(Pattern("steel2.png").exact())
        self.production()

    def openGoldOre(self):
        close = self.openMaterialsMenu(2)
        click(Pattern("goldOre.png").exact())
        self.scrollToTop()
        click(close)
        click(Pattern("goldOre2.png").exact())
        self.production()

    def openGold(self):
        close = self.openMaterialsMenu(2)
        click(Pattern("gold.png").exact())
        self.scrollToTop()
        click(close)
        click(Pattern("gold2.png").exact())
        self.production()

    def openTitanOre(self):
        close = self.openMaterialsMenu(2)
        click(Pattern("titanOre.png").exact())
        self.scrollToTop()
        click(close)
        click(Pattern("titanOre2.png").exact())
        self.production()

    def openTitan(self):
        close = self.openMaterialsMenu(2)
        click(Pattern("titan.png").exact())
        self.scrollToTop()
        click(close)
        click(Pattern("titan2.png").exact())
        self.production()

    def openSaltpeter(self):
        close = self.openMaterialsMenu(2)
        click(Pattern("saltpeter.png").exact())
        self.scrollToTop()
        click(close)
        click(Pattern("saltpeter2.png").exact())
        self.production()

    def openGunPowder(self):
        close = self.openMaterialsMenu(2)
        click(Pattern("gunPowder.png").exact())
        self.scrollToTop()
        click(close)
        click(Pattern("gunPowder2.png").exact())
        self.production()

    def openGranite(self):
        close = self.openMaterialsMenu(2)
        click(Pattern("granite.png").exact())
        self.scrollToTop()
        click(close)
        click(Pattern("granite2.png").exact())
        self.production()

    def openWater(self):
        close = self.openMaterialsMenu(3)
        click(Pattern("water.png").exact())
        self.scrollToTop()
        click(close)
        click(Pattern("water2.png").exact())
        self.production()

    def openWheat(self):
        close = self.openMaterialsMenu(3)
        click(Pattern("wheat.png").exact())
        self.scrollToTop()
        click(close)
        click(Pattern("wheat2.png").exact())
        self.production()

    def openMeat(self):
        close = self.openMaterialsMenu(3)
        click(Pattern("meat.png").exact())
        self.scrollToTop()
        click(close)
        click(Pattern("meat2.png").exact())
        self.production()

    def openFlour(self):
        close = self.openMaterialsMenu(3)
        click(Pattern("flour.png").exact())
        self.scrollToTop()
        click(close)
        click(Pattern("flour2.png").exact())
        self.production()

    def openWheels(self):
        close = self.openMaterialsMenu(3)
        click(Pattern("wheel.png").exact())
        self.scrollToTop()
        click(close)
        click(Pattern("wheel2.png").exact())
        self.production()

    def openCarts(self):
        close = self.openMaterialsMenu(3)
        click(Pattern("cart.png").exact())
        self.scrollToTop()
        click(close)
        click(Pattern("cart2.png").exact())
        self.production()
            
    def production(self):
        click(Pattern("production.png").exact().targetOffset(-35,32))
        

if __name__ == '__main__':
    e = Economy()
    #e.open()
    #e.scrollToTop()
    e.openWheels()
    
    
            
        