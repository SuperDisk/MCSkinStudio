#MCSkin2D, a kind of funny skin editor!
#Programmed by SapperEngineer

from pygame.locals import *


class skinpreview:
    def __init__(self, pos, mcskin2d):
        self.pos = pos
        self.modeldir = 0
        self.mcskin2d = mcskin2d
        self.rect = mcskin2d.pygame.Rect(pos, (160, 320))
        self.surface = mcskin2d.pygame.Surface((160, 320), SRCALPHA).convert_alpha()
        self.update()

    def update(self):
        drawsurface = self.mcskin2d.drawboard.getsurface()
        self.surface.fill((255, 255, 255, 0))

        #Modeldir:
        #Modeldir += 1: the model rotates to his left

        #Blits to the model
        if self.modeldir == 0: #Facing down
            self.surface.blit(drawsurface, (40, 1), (80, 80, 80, 80))
            self.surface.blit(drawsurface, (40, 81), (200, 200, 80, 119))
            self.surface.blit(drawsurface, (0, 81), (440, 200, 40, 119))
            self.surface.blit(drawsurface, (120, 81), (440, 200, 40, 119))
            self.surface.blit(drawsurface, (40, 200), (40, 200, 40, 119))        
            self.surface.blit(drawsurface, (80, 200), (40, 200, 40, 119))
            self.surface.blit(drawsurface, (40, 1), (400, 80, 80, 80))

        if self.modeldir == 1: #Facing right
            self.surface.blit(drawsurface, (40, 1), (0, 80, 80, 80))
            self.surface.blit(drawsurface, (40, 1), (320, 80, 80, 80))
            self.surface.blit(drawsurface, (60, 81), (400, 200, 40, 120))
            self.surface.blit(drawsurface, (60, 199), (0, 200, 40, 120))

        if self.modeldir == 2: #Facing forward
            self.surface.blit(drawsurface, (40, 1), (240, 80, 80, 80))
            self.surface.blit(drawsurface, (40, 81), (320, 200, 80, 119))
            self.surface.blit(drawsurface, (0, 81), (520, 200, 40, 119))
            self.surface.blit(drawsurface, (120, 81), (520, 200, 40, 119)) # arm
            self.surface.blit(drawsurface, (40, 200), (120, 200, 40, 119))        
            self.surface.blit(drawsurface, (80, 200), (120, 200, 40, 119))
            self.surface.blit(drawsurface, (40, 1), (559, 80, 80, 80))

        if self.modeldir == 3: #Facing left
            self.surface.blit(drawsurface, (40, 1), (160, 80, 80, 80))
            self.surface.blit(drawsurface, (40, 1), (480, 80, 80, 80))
            self.surface.blit(drawsurface, (60, 81), (400, 200, 40, 120))
            self.surface.blit(drawsurface, (60, 199), (0, 200, 40, 120))

    def shiftright(self):
        self.modeldir += 1
        if self.modeldir > 3:
            self.modeldir = 0

    def shiftleft(self):
        self.modeldir -= 1
        if self.modeldir < 0:
            self.modeldir = 3

    def getsurface(self):
        return self.surface

    def getrect(self):
        return self.rect

    def getpos(self):
        return self.pos
