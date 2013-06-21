
from sikuli.Sikuli import *


class Economy:
    
    def open(self):
        if not exists("economyTitle.png"):
            x = find(Pattern("economyButton.png").similar(0.90))
            click(x)


