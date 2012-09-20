#MCSkin2D, a kind of funny skin editor!
#Programmed by SapperEngineer

class messhandler:
    def __init__(self, mcskin2d, messes=[]):
        self.mcskin2d = mcskin2d
        self.messes = []

    def registermess(self, mess):
        self.messes.append(mess)

    def registermesses(self, messlist):
        for mess in messlist:
            self.messes.append(mess)
    
    def cleanmesses(self):
        self.mcskin2d.pygame.display.update(self.messes)

        self.messes = []
