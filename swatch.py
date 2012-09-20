#MCSkin2D, a kind of funny skin editor!
#Programmed by SapperEngineer

from pygame.locals import *
from copy import copy

class swatches:
    def __init__(self, pos, mcskin2d):
        self.mcskin2d = mcskin2d
        self.pos = pos
        self.size = (260, 78)
        self.boxsize = (18, 18)

        self.selectedbox = [0, 0, 18, 18]

        self.rect = mcskin2d.pygame.Rect(self.pos, self.size)

        self.surface = mcskin2d.pygame.Surface(self.size, SRCALPHA).convert_alpha()

        self.boxes = {}

        pad = 2
        placepos = [0, 0]
        
        for i in range(4): #Y
            for i in range(11): #X
                putsurf = mcskin2d.pygame.Surface(self.boxsize)
                putsurf.fill((255, 255, 255))
                mcskin2d.pygame.draw.rect(putsurf, (0, 0, 0), ((0, 0), self.boxsize), 3)
                self.boxes[(placepos[0], placepos[1], 18, 18)] = putsurf
                placepos[0] += 18 + pad + 4

            placepos[0] = 0
            placepos[1] += 18 + pad
            self.update()


    def update(self):
        self.surface.fill((0, 0, 0, 0))

        self.mcskin2d.pygame.draw.rect(self.boxes[tuple(self.selectedbox)], (255, 255, 255), (0, 0, 18, 18), 1)

        for rect in self.boxes:
            self.surface.blit(self.boxes[rect], (rect[0], rect[1]))

        collision = self.getcollisions()
        if self.mcskin2d.inputengine.mousepushed(1) and collision:
            self.setselected((collision[0][0], collision[0][1]))
            self.setselected((collision[0][0], collision[0][1]))
        
        if self.mcskin2d.inputengine.mousepushed(3) and collision:
            self.setboxcolor((collision[0][0], collision[0][1]), self.mcskin2d.drawboard.color)


    def setselected(self, boxpos):
        self.mcskin2d.pygame.draw.rect(self.boxes[tuple(self.selectedbox)], (0, 0, 0), (0, 0, 18, 18), 3)

        #Hacky :(
        setcol = self.boxes[tuple(self.selectedbox)].get_at((5, 5))
        if setcol[0] < 254: setcol[0] += 2
        if setcol[1] < 254: setcol[1] += 2
        if setcol[1] < 254: setcol[2] += 2

        self.mcskin2d.rgbbuffer['r'].setslider(setcol[0])
        self.mcskin2d.rgbbuffer['g'].setslider(setcol[1])
        self.mcskin2d.rgbbuffer['b'].setslider(setcol[2])

        self.selectedbox[0] = boxpos[0]
        self.selectedbox[1] = boxpos[1]

    def setboxcolor(self, box, color):
        box = (box[0], box[1], 18, 18)
        self.boxes[box].fill(color)
        self.mcskin2d.pygame.draw.rect(self.boxes[box], (0, 0, 0), (0, 0, 18, 18), 3)

    def getsurface(self):
        return self.surface

    def getpos(self):
        return self.pos

    def getcollisions(self):
        return self.mcskin2d.mousehandler.getsurfacerect(self.rect).collidedict(self.boxes)
