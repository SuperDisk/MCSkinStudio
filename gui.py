#MCSkin2D, a kind of funny skin editor!
#Programmed by SapperEngineer

from pygame.locals import *
from copy import copy

class button:
    def __init__(self, text, code, pos, mcskin2d):
        size = mcskin2d.fontrenderer.sizesmall(text)
        self.pos = pos
        self.rect = mcskin2d.pygame.Rect(pos, size)
        self.text = text
        self.code = code
        self.mcskin2d = mcskin2d
        self.surface = mcskin2d.pygame.Surface(size)
        self.surface.blit(mcskin2d.contentloader.guistone, (0, 0))
        #self.surface.fill((255, 255, 255))
        mcskin2d.pygame.draw.rect(self.surface, (0, 0, 0), ((0, 0), size), 3)
        self.surface.blit(mcskin2d.fontrenderer.rendersmall(text, color=(56, 56, 56)), (4, 2))
        self.surface.blit(mcskin2d.fontrenderer.rendersmall(text, color=(224, 224, 224)), (2, 0))

    def update(self):
        if self.mcskin2d.mousehandler.getrect().colliderect(self.rect):
            if self.mcskin2d.inputengine.mousepushed(1):
                for line in self.code:
                    try:exec(line)
                    except:pass
                    
                    

    def getsurface(self):
        return self.surface

    def getrect(self):
        return self.rect

    def getpos(self):
        return self.pos


class slider:
    def __init__(self, text, length, pos, mcskin2d):
        self.mcskin2d = mcskin2d
        self.text = text
        self.pos = pos
        self.size = (length, 23)
        self.rect = mcskin2d.pygame.Rect(pos, self.size)
        self.sliderpos = 0
        self.surface = mcskin2d.pygame.Surface(self.size)

        self.surface.blit(mcskin2d.contentloader.guistonedepressed, (0, 0))
        mcskin2d.pygame.draw.rect(self.surface, (0, 0, 0), ((0, 0), self.size), 3)
        self.surface.blit(mcskin2d.contentloader.guislider, (0, 0))
        self.surface.blit(mcskin2d.fontrenderer.rendersmall(text, color=(56, 56, 56)), (4, 2))
        self.surface.blit(mcskin2d.fontrenderer.rendersmall(text, color=(224, 224, 224)), (2, 0))

    def update(self):
        if (self.mcskin2d.mousehandler.getrect().colliderect(self.rect) and self.mcskin2d.inputengine.mouseispushed(1)):
            self.sliderpos = (self.mcskin2d.mousehandler.getposx() - self.pos[0]) - 2

        self.surface.blit(self.mcskin2d.contentloader.guistonedepressed, (0, 0))
        self.surface.blit(self.mcskin2d.contentloader.guislider, (self.sliderpos - 2, 0))
        self.mcskin2d.pygame.draw.rect(self.surface, (0, 0, 0), ((0, 0), self.size), 3)
        self.surface.blit(self.mcskin2d.fontrenderer.rendersmall(self.text, color=(56, 56, 56)), (4, 2))
        self.surface.blit(self.mcskin2d.fontrenderer.rendersmall(self.text, color=(224, 224, 224)), (2, 0))
        return True

    def setslider(self, pos):
        self.sliderpos = (pos) - 2
        self.update()

    def getsurface(self):
        return self.surface

    def getrect(self):
        return self.rect

    def getpos(self):
        return self.pos

    def getvalue(self):
        if self.sliderpos < 0: self.sliderpos = 0
        if self.sliderpos > 255: self.sliderpos = 255
        return self.sliderpos




class textvariable:
    def __init__(self, size, pos, mcskin2d):
        self.size = size
        self.pos = pos
        self.mcskin2d = mcskin2d
        self.rect = mcskin2d.pygame.Rect(pos, size)
        self.surface = mcskin2d.pygame.Surface(size)
        self.text = ""

        self.surface.blit(mcskin2d.contentloader.guistonedepressed, (0, 0))
        self.mcskin2d.pygame.draw.rect(self.surface, (0, 0, 0), ((0, 0), self.size), 3)
        

    def update(self):
        self.surface.blit(self.mcskin2d.contentloader.guistonedepressed, (0, 0))
        self.mcskin2d.pygame.draw.rect(self.surface, (0, 0, 0), ((0, 0), self.size), 3)
        self.surface.blit(self.mcskin2d.fontrenderer.rendersmall(self.text, color=(56, 56, 56)), (4, 2))
        self.surface.blit(self.mcskin2d.fontrenderer.rendersmall(self.text, color=(224, 224, 224)), (2, 0))

    def getsurface(self):
        return self.surface

    def getrect(self):
        return self.rect

    def getpos(self):
        return self.pos

    def getvalue(self):
        returnint = int(self.text)
        if returnint > 255: returnint = 255
        if returnint < 0: returnint = 0
        return returnint

    def setvalue(self, value):
        self.text = str(value)
