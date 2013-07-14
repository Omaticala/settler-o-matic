
from sikuli.Sikuli import *


class Merchant:

    def open(self):
        if not exists("menuTopRightCorner.png", 0):
            click(Pattern("chestIcon.png").similar(0.90))

    def Adventures(self):
        self.open()
        click(Pattern("adventuresMenu.png").similar(0.90))

    def BountyHunter():
        click(Pattern("bountyHunterAdventure.png").similar(0.90))
        

if __name__ == '__main__':
    m = Merchant()
    m.open()
    