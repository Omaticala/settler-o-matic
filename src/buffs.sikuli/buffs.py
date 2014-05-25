
from sikuli.Sikuli import *


class Buffs:
    "checks buildings and buffs them"

    comodities = {
        "buildMat": {
            "PineBoards": 1,
            "HardBoards": 1,
            "ExoticBoards": 0,
            "Tools": 1,
            "Coins": 1,
            "Stone": 1,
            "Marble": 1
        },
        "food": { 
            "Fish": 1,
            "Beer": 1,
            "Sausages": 1,
            "Bread": 1,
        },
        "weapons": {
            "Horses": 1,
            "BronzeSwords": 1,
            "IronSwords": 1,
            "SteelSwords": 1,
            "DamasceneSwords": 0,
            "Bows": 1,
            "LongBows": 1,
            "CrossBows": 0,
            "Cannons": 0,
        },
        "science": {
            "SimplePaper": 1,
            "IntermediatePaper": 1,
            "AdvancedPaper": 0,
            "Pens": 1,
            "Letters": 1,
            "Ornaments": 0,
        }, 
        "materials": {
            "PineWood": 1,
            "HardWood": 1,
            "PineTrees": 0,
            "HardTrees": 0,
            "Coal": 1, # two types of buildings!
            "CopperOre": 1,
            "Copper": 1,
            "IronOre": 1,
            "Iron": 1,
            "Steel": 1,
            "GoldOre": 1,
            "Gold": 0,            
            "Titan": 0,
            "GunPowder": 0,
            "Water": 0,
            "Wheat": 1,
            "Meat": 1,
            "Flour": 1,
            "Wheels": 0,
            "Carts": 0,
        }
    }

    def __init__(self, menu, economy, game):
        self.menu = menu
        self.economy = economy
        game.goFullScreen()
        #self.supplies = supplies

    def buffEverything(self):
        for group in self.comodities:
            self.buffGroup(group)
                    
    def buffGroup(self, group):
        for comodity in self.comodities[group]:
            if self.comodities[group][comodity]:
                self.buffComodity(comodity)

    def buffComodity(self, comodity):
        print(comodity)
        selectComodity = getattr(self.economy, comodity)
        n = 0
        next = 1
        try:
            while next:
                n += 1
                selectComodity()
                building = self.economy.production().selectBuffableBuilding(n)
                if not building:
                    break
                next = building.hasNext
                self.menu.FishPlate()
                wait(0.1)
                building.click()
        except:
            pass

    