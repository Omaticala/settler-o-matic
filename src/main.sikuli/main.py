
class Window:

    def init(self):
        self.hideChatWindow()        
        self.hideUsersBar()
        self.turnSoundsOff()
        self.goFullScreen()
        wait(0.5)
        # bug - opening majors house dialog
        dialog = exists("dialogCloseButton.png")
        if dialog:
            click(dialog)


    def hideUsersBar(self):
        arrow = exists(Pattern("usersBarUpArrow.png").similar(0.90))
        if arrow:
            click(arrow)

    def hideChatWindow(self):
        button = exists(Pattern("chatMinimizeButton.png").similar(0.90).targetOffset(0,-13))
        if button:
            click(button)
        
    def turnSoundsOff(self):
        menu = exists(Pattern("settingsDownArrow.png").similar(0.90))
        if (menu):
            click(menu)
        wait(1)
        note = exists(Pattern("note.png").similar(0.80))
        if (note):
            click(note)
        speaker = exists(Pattern("speaker.png").similar(0.90))
        if (speaker):
            click(speaker)
        arrow = find("settingsUpArrow.png")
        click(arrow)

    def goFullScreen(self):
        if exists(Pattern("browserButtons.png").similar(0.90)):
            green = find("green.png")
            click(green)
            type(Key.F11)
            confirm = exists("fullscreenAllowButton.png")
            if confirm:
                click(confirm)

class Economy:
    
    def open(self):
        if not exists("economyTitle.png"):
            x = find(Pattern("economyButton.png").similar(0.90))
            click(x)

# buildings -----------------------------------------------------------------------------

class Buildings:
    
    def open(self):
        if not exists("buildingsTitle.png"):
            buildings = find(Pattern("buildingsButton.png").similar(0.80))
            click(buildings)

    # basic buildings -------------------------------------------------

    def Basic(self):
        self.open()
        tab = find(Pattern("buildingsBasicTab.png").similar(0.90))
        click(tab)

    def StoneMine(self):
        self.Basic()
        mine = find("stoneMineButton.png")
        click(mine)

    # middle buildings -------------------------------------------------

    def Middle(self):
        self.open()
        tab = find(Pattern("buildingsMiddleTab.png").similar(0.90))
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
        tab = find(Pattern("buildingsAdvancedTab.png").similar(0.90))
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
        tab = find(Pattern("buildingsExpertTab.png").similar(0.90))
        click(tab)

    # building tools --------------------------------------------
    
    def Tools(self): 
        self.open()
        tab = find(Pattern("buildingsToolsTab.png").similar(0.90))
        click(tab)
        

# main menu -------------------------------------------------------------------------

class Menu:
    
    def open(self):
        if not exists("dragonFace.png"):
            star = find(Pattern("nemuStar.png").similar(0.90))
            click(star)

    # specialists -----------------------------------------------------
    
    def Specialists(self):
        self.open()
        tab = find("menuSpecialistsTab.png")
        click(tab)

    def Explorer(self):
        self.Specialists()
        explorer = find(Pattern("explorerButton.png").similar(0.90))
        click(explorer)

    def exploreSector(self):
        self.Explorer()
        telescope = find("telescopeButton.png")
        click(telescope)

    def findTreasure(self, time):
        self.Explorer()
        chest = find("chestButton.png")
        click(chest)
        if time == 1:
            timer = find(Pattern("timer1Button.png").exact())
            click(timer)
        elif time == 2:
            timer = find(Pattern("timer2Button.png").exact())
            click(timer)
        elif time == 3:
            # todo: update image
            timer = find(Pattern("timer3Button.png").exact())
            click(timer)
        else:
            # todo: update image
            timer = find(Pattern("timer4Button.png").exact())
            click(timer)

    def findAdventure(self, time):
        self.Explorer()
        map = find("mapButton.png")
        click(map)
        if time == 1:
            timer = find(Pattern("timer1Button.png").exact())
            click(timer)
        elif time == 2:
            timer = find(Pattern("timer2Button.png").exact())
            click(timer)
        else:
            # todo: update image
            timer = find(Pattern("timer3Button.png").exact())
            click(timer)

    def Geologist(self):
        self.Specialists()
        geologist = find(Pattern("geologistButton.png").similar(0.90))
        click(geologist)

    def findStone(self):
        self.Geologist()
        stone = find("stoneButton.png")
        click(stone)

    def findCopper(self):
        self.Geologist()
        copper = find("copperButton.png")
        click(copper)

    def findMarble(self):
        self.Geologist()
        marble = find("marbleButton.png")
        click(marble)

    def findIron(self):
        self.Geologist()
        iron = find("ironButton.png")
        click(iron)

    def findCoal(self):
        self.Geologist()
        coal = find("coalButton.png")
        click(coal)

    def findGold(self):
        self.Geologist()
        gold = find("goldButton.png")
        click(gold)

    # bonuses --------------------------------------------------------------
    
    def Buffs(self):
        self.open()
        tab = find("menuBuffsTab.png")
        click(tab)

    def FishPlate(self):
        self.Buffs()
        plate = find(Pattern("menuFishPlateButton.png").similar(0.90))
        click(plate)

    # resources -------------------------------------------------------------
    
    
    def Resources(self):
        self.open()
        tab = find("menuResourcesTab.png")
        click(tab)


# supplies -------------------------------------------------------------------

class Supplies:

    def open(self):
        building = find("suppliesBuilding.png")
        click(building)
        click(building)
    
    def Resources(self):
        self.open()
        tab = find("suppliesResourcesTab.png")
        click(tab)

    # deposits ---------------------------------------------------------------
    
    def Deposits(self):
        self.open()
        tab = find("suppliesDepositsTab.png")
        click(tab)
    
    def makeFishFood(self, count):
        self.Deposits()
        food = find("fishFoodButton.png")
        click(food)
        arrow = find(Pattern("leftArrow.png").similar(0.90))
        while count > 1:
            click(arrow)
            count = count - 1
        ok = find("okButton.png")
        click(ok)

    def makeDeerFood(self, count):
        self.Deposits()
        food = find("deerFoodButton.png")
        click(food)
        arrow = find(Pattern("leftArrow.png").similar(0.90))
        while count > 1:
            click(arrow)
            count = count - 1
        ok = find("okButton.png")
        click(ok)

# actions --------------------------------------------------------------------

class Maintenance:
    
    def rebuildField():
        field = find(Pattern("emptyField.png").similar(0.50))
        click(field)
        click(field) # click bug
        bomb = wait("bombButton.png")
        click(bomb)
        ok = wait("okButton.png")
        click(ok)
        Buildings().Field()
        wait(11)
        click(field)

    def rebuildWell():
        well = find(Pattern("emptyWell.png").similar(0.90))  
        click(well)
        click(well) # click bug
        bomb = wait("bombButton.png", 2)
        click(bomb)
        ok = wait("okButton.png", 2)
        click(ok)
        Buildings().Well()
        wait(11)
        click(well)



#Buildings().Field()
#Supplies().makeFishFood(5)
Window().init()

