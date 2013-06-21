
from sikuli.Sikuli import *


class Menu:
    
    def open(self):
        if not exists("dragonFace.png"):
            star = find(Pattern("star.png").similar(0.90))
            click(star)

    # specialists -----------------------------------------------------
    
    def Specialists(self):
        self.open()
        tab = find("specialistsTab.png")
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

    # bonuses --------------------------------------------------------------
    
    def Buffs(self):
        self.open()
        tab = find("buffsTab.png")
        click(tab)

    def FishPlate(self):
        self.Buffs()
        plate = find(Pattern("fishPlateButton.png").similar(0.90))
        click(plate)

    # resources -------------------------------------------------------------
    
    
    def Resources(self):
        self.open()
        tab = find("resourcesTab.png")
        click(tab)

