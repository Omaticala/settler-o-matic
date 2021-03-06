
from sikuli.Sikuli import *


class GameException(Exception):
    pass

class Game:

    def __init__(self):
        Settings.MoveMouseDelay = 0.25 # double speed

    def init(self):
        "ensure game is running and has maximal viewport"
        self.startGame()
        self.hideChatWindow()        
        self.hideUsersBar()
        #self.turnSoundsOff()
        self.goFullScreen()

    def restartGame(self):
        fail = exists(Pattern("fail.png").similar(0.90).targetOffset(5,44))
        # ...

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

    def detectAnnouncement(self):
        if exists("serverAnnouncement.png"):
            ok = exists("okButton-1.png")
            if ok:
                click(ok)
        
        
        

def closeDialog():
    cross = exists("dialogCloseX.png")
    if cross:
        click(cross)
        
    