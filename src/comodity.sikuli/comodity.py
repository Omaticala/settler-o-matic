
from sikuli.Sikuli import *


class Comodity:

    def __init__(self, name, location):
        self.name = name
        self.location = location

    def getTrend(self):
        region = Region(self.location.getX() + 108, self.location.getY() - 2, 30, 30)
        region.highlight(2)
        if region.exists(Pattern("arrowUpGreen.png").exact()):
            return "growing"
        elif region.exists(Pattern("arrowUpYellow.png").exact()):
            return "growing-x"
        elif region.exists(Pattern("arrowRightGray.png").exact()):
            return "none"
        elif region.exists(Pattern("arrowDownRed.png").exact()):
            return "falling"
        elif exists(Pattern("arrowDownYellow.png").exact()):
            return "falling-x"
        else:
            return "unknown"
            
    def getAmount(self):
        Settings.OcrTextRead = 1
        region = Region(self.location.getX() + 50, self.location.getY() + 3, 55, 25)
        region.highlight(2)
        amount = region.text()
        print(amount)
        return amount

        