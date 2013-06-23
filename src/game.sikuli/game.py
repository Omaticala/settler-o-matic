
#import sys
#myScriptPath = "c:\\http\\omaticala\\settler-o-matic\\src"
#if not myScriptPath in sys.path:
#    sys.path.append(myScriptPath)
    
from sikuli.Sikuli import *

from map import *
from queue import *
from economy import *
from maintenance import *


class GameException(Exception):
    pass

class Game:

    def __init__(self):
        Settings.MoveMouseDelay = 0.25 # double speed
        self.init()
        self.map = Map()
        self.queue = Queue()
        self.economy = Economy()
        self.maintenance = Maintenance(self.map, self.queue, self.economy)
        self.maintenance.run()

    def init(self):
        "ensure game is running and has maximal viewport"
        self.startGame()
        self.hideChatWindow()        
        self.hideUsersBar()
        #self.turnSoundsOff()
        self.goFullScreen()

    def startGame(self):
        play = exists("playNowButton.png")
        if play:
            click(play)
            ok = wait("okButton.png", 60)
            if ok:
                click(ok)
            else:
                raise GameException("Cannot start game.")

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
            green = find(Pattern("green-1.png").similar(0.50))
            click(green)
            type(Key.F11)
            confirm = exists("fullscreenAllowButton.png")
            if confirm:
                click(confirm)
                wait(0.5)
                # bug - opening majors house dialog
                cross = exists("dialogCloseButton.png")
                if cross:
                    click(cross)


def closeDialog():
    cross = exists("dialogCloseX.png")
    if cross:
        click(cross)
        

if __name__ == '__main__':
    g = Game()
    