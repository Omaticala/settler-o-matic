
from sikuli.Sikuli import *


class Building:

    def __init__(self, name = "unknown"):
        self.name = name
        self.location = Location(SCREEN.getW() / 2, 380)

    def __repr__(self):
        return "Building: " + self.name

    def click(self):
        click(self.location)

    def close(self):
        close = exists("closeButton.png")
        if close:
            click(close)

    def pause(self):
        pause = exists(Pattern("pauseButton.png").exact(), 0)
        if pause:
            click(pause)

    def resume(self):
        resume = exists(Pattern("resumeButton.png").exact(), 0)
        if resume:
            click(resume)

    def isRunning(self):
        return exists(Pattern("pauseButton.png").exact(), 0)

    def isPaused(self):
        return not self.isRunning()
    
    def isBuffed(self):
        #wait(1)
        sandwich = exists("sandwich.png", 0)

        hover(sandwich)
        
        return sandwich
    
    def getBuffTimeout(self):
        buff = self.isBuffed()
        if not buff:
            print(0)
            return 0
        
        Settings.OcrTextRead = 1
        region = Region(buff.getX() - 70, buff.getY() + 30, 130, 15)
        region.highlight()
        time = region.text()
        print(time)
        return time

    def getLevel(self):
        Settings.OcrTextRead = 1
        label = find(Pattern("levelLabel.png").similar(0.90))
        region = Region(label.getX(), label.getY(), 80, 20)
        region.highlight()
        level = region.text()
        print(level)
        return level

    def getProductionTime(self):
        Settings.OcrTextRead = 1
        click("detailsTab.png")
        clock = find("clock.png")
        region = Region(clock.getX() + 170, clock.getY() + 5, 140, 20)
        region.highlight()
        time = region.text()
        print(time)
        return time


if __name__ == '__main__':
    b = Building("Stable")
    b.getLevel()
    b.getBuffTimeout()
    b.getProductionTime()
        