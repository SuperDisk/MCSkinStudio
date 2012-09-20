#MCSkin2D, a kind of funny skin editor!
#Programmed by SapperEngineer

from copy import copy

class colorshower:
    def __init__(self, pos, mcskin2d):
        self.mcskin2d = mcskin2d

        self.surface = self.mcskin2d.pygame.Surface((42, 42))
        self.rect = (pos, (20, 20))

        self.color = copy(mcskin2d.drawboard.color)

        self.pos = pos

        self.surface.fill(self.color)
        self.mcskin2d.pygame.draw.rect(self.surface, (0, 0, 0), (0, 0, 42, 42), 3)



    def update(self):
        if self.mcskin2d.drawboard.color != self.color:
            self.color = copy(self.mcskin2d.drawboard.color)
            self.surface.fill(self.color)
            self.mcskin2d.pygame.draw.rect(self.surface, (0, 0, 0), (0, 0, 42, 42), 3)

    def getsurface(self):
        return self.surface

    def getrect(self):
        return self.rect

    def getpos(self):
        return self.pos
