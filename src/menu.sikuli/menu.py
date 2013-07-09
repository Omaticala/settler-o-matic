
from sikuli.Sikuli import *


class Menu:

    tab = ""
    
    def open(self):
        if not exists("dragonFace.png", 0):
            click(Pattern("star.png").similar(0.90))

    def All(self):
        "opens 'all' menu"
        self.open()
        if self.tab != "all":
            click("all.png")
            self.tab = "all"

    def Specialists(self):
        "opens specialists menu"
        self.open()
        if self.tab != "specialists":
            click("specialistsTab.png")
            self.tab = "specialists"

    def Buffs(self):
        "opens Buffs menu"
        self.open()
        if self.tab != "buffs":
            click("buffsTab.png")
            self.tab = "buffs"

    def Resources(self):
        "opens resources menu"
        self.open()
        if self.tab != "resources":
            click("resourcesTab.png")
            self.tab = "resources"

    def Misc(self):
        "opens 'misc' menu"
        self.open()
        if self.tab != "misc":
            click("misc.png")
            self.tab = "misc"

    # specialists -----------------------------------------------------

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
            self.timer1()
        elif time == 2:
            self.timer2()
        elif time == 3:
            self.timer3()
        else:
            self.timer4()

    def findAdventure(self, time):
        self.Explorer()
        map = find("mapButton.png")
        click(map)
        if time == 1:
            self.timer1()
        elif time == 2:
            self.timer2()
        else:
            self.timer3()

    def timer1(self):
        timer = find(Pattern("timer1Button.png").exact())
        click(timer)
    
    def timer2(self):
        timer = find(Pattern("timer2Button.png").exact())
        click(timer)
    
    def timer3(self):
        # todo: update image
        timer = find(Pattern("timer3Button.png").exact())
        click(timer)
            
    def timer4(self):
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

    # buffs ----------------------------------------------------------------

    def FishPlate(self):
        "selects Fish Plate, returns 1 if ok"
        self.Buffs()
        plate = exists(Pattern("fishPlateButton.png").similar(0.90))
        if plate:
            click(plate)
            return 1
        return 0

    def Sandwich(self):
        "selects Big Sandwich, returns 1 if ok"
        self.Buffs()
        sandwich = exists(Pattern("sandwich.png").similar(0.90))
        if sandwich:
            click(sandwich)
            return 1
        return 0

    def Basket(self):
        "selects Aunt Irma's Basket, returns 1 if ok"
        basket = exists(Pattern("basket.png").similar(0.90))
        if basket:
            click(basket)
            return 1
        return 0

    def Drink(self):
        "selects Red Drink, return 1 if ok"
        drink = exists("drink.png")
        if drink:
            click(drink)
            return 1
        return 0

    # resources -------------------------------------------------------------

    def FishFood(self):
        self.Resources()
        ##

    def DeerFood(self):
        self.Resources()
        ##


        
        