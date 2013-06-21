
from sikuli.Sikuli import *


class Maintenance:

    def __init__(self, game):
        self.game = game
    
    def rebuildField(self):
        field = find(Pattern("emptyField.png").similar(0.50))
        click(field)
        click(field) # click bug
        self.destroy()
        Buildings().Field()
        wait(11)
        click(field)

    def rebuildWell(self):
        well = find(Pattern("emptyWell.png").similar(0.90))  
        click(well)
        click(well) # click bug
        self.destroy()
        Buildings().Well()
        wait(11)
        click(well)

    def findEmptyMine(self):
        mine = exists(Pattern("emptyMine.png").similar(0.50))
        return mine

    def destroy(self):
        bomb = wait("bombButton.png", 2)
        click(bomb)
        ok = wait("okButton.png", 2)
        click(ok)
    