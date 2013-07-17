
from javax.swing import JFrame, JButton
from java.awt.BorderLayout import SOUTH

class Gui:

    paused = 0
    
    def __init__(self):
        w = JFrame("Settler-o-matic", size = (120,680))
        w.setAlwaysOnTop(True)
        
        pause = JButton("Pause", actionPerformed = self.pause)
        w.add(pause, SOUTH)
        
        w.visible = True
        self.window = w
        self.pause = pause

    def pause(self, event):
        if self.paused:
            self.pause.text = "Pause"
            self.paused = 0
        else:
            self.pause.text = "Continue"
            self.paused = 1

if __name__ == '__main__':
    gui = Gui()
    
