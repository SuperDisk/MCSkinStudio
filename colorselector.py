#MCSkin2D, a kind of funny skin editor!
#Programmed by SapperEngineer

import pygame
from pygame.locals import *

class colorselector:
    def __init__(self, pos, mcskin2d):
        self.color = (0, 0, 0)
        self.pos = pos
        self.mcskin2d = mcskin2d
        self.surface = mcskin2d.contentloader.tri
        self.rect = mcskin2d.pygame.Rect(pos, self.surface.get_size())

    def getsurface(self):
        return self.surface

    def getcol(self):
        if self.mcskin2d.inputengine.mouseispushed(1) and self.mcskin2d.mousehandler.getrect().colliderect(self.rect):

            returncol = self.surface.get_at(self.mcskin2d.mousehandler.getsurfacepos(self.rect))
            if returncol[3] == 255:
                self.mcskin2d.rgbbuffer['r'].setslider(returncol[0])
                self.mcskin2d.rgbbuffer['g'].setslider(returncol[1])
                self.mcskin2d.rgbbuffer['b'].setslider(returncol[2])
                return self.surface.get_at(self.mcskin2d.mousehandler.getsurfacepos(self.rect))

            return False

    def getpos(self):
        return self.pos
