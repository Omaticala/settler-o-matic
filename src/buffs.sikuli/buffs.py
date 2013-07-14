
from sikuli.Sikuli import *


class Buffs:
    "checks buildings and buffs them"

    comodities = {
        "buildMat": {
            "PineBoards": 1,
            "HardBoards": 1,
            "ExoticBoards": 1,
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
            "DamasceneSwords": 1,
            "Bows": 1,
            "LongBows": 1,
            "CrossBows": 1,
            "Cannons": 1,
        },
        "science": {
            "SimplePaper": 1,
            "IntermediatePaper": 1,
            "Pens": 1,
            "Letters": 1,
            "Ornaments": 1,
        }, 
        "materials": {
            "PineWood": 1,
            "HardWood": 1,
            "PineTrees": 1,
            "HardTrees": 1,
            "Coal": 1, # two types of buildings!
            "CopperOre": 1,
            "Copper": 1,
            "IronOre": 1,
            "Iron": 1,
            "Steel": 1,
            "GoldOre": 1,
            "Gold": 1,
            "Titan": 1,
            "GunPowder": 1,
            "Water": 0,
            "Meat": 1,
            "Flour": 1,
            "Wheels": 1,
            "Carts": 1,
        }
    }

    def __init__(self, menu, economy, supplies):
        self.menu = menu
        self.economy = economy
        self.supplies = supplies

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
        building = 1
        while building:
            n += 1
            selectComodity()
            building = self.economy.production().selectBuffableBuilding(n)
            if not building:
                break
            if building.isBuffed():
                continue
            if building.isPaused():
                continue
            self.menu.FishPlate()
            building.click()
            


if __name__ == '__main__':
    import menu
    import economy
    import supplies
    reload(menu)
    reload(economy)
    reload(supplies)
    from menu import *
    from economy import *
    from supplies import *
    
    b = Buffs(Menu(), Economy(), Supplies())
    b.buffGroup("materials")
    #b.buffEverything()
    

    