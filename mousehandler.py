#A simple Mouse Handler for offsets and updating mouserect
#Programmed by SapperEngineer

import pygame
from pygame.locals import *

import ctypes

class mousehandler:
    def __init__(self):
        self.mouserect = pygame.Rect(pygame.mouse.get_pos(), (1, 1))
        self.mouseoffset = [0, 0]
        self.posondisplay = [0, 0]
        self.pointstruct = POINT()
        self.pointstructpointer = ctypes.pointer(self.pointstruct)

    def update(self): #Yes, it's cheesy.
        self.mouserect.topleft = (pygame.mouse.get_pos()[0] + self.mouseoffset[0], pygame.mouse.get_pos()[1] + self.mouseoffset[1])
        self.updateondisplay()

    def updateondisplay(self):
        ctypes.windll.user32.GetCursorPos(self.pointstructpointer)
        self.posondisplay = self.pointstruct.x, self.pointstruct.y
        
    def getrect(self):
        return self.mouserect

    def getpos(self):
        return self.mouserect.topleft

    def getposx(self):
        return self.mouserect.topleft[0]

    def getposy(self):
        return self.mouserect.topleft[1]

    def getsurfacepos(self, rect):
        return (self.getpos()[0] - rect.topleft[0], self.getpos()[1] - rect.topleft[1])

    def getsurfacerect(self, rect):
        return pygame.Rect(self.getsurfacepos(rect), (1, 1))

    def changecursor(self, cursorname, hotspot=(7,8)):
        datatuple, masktuple = pygame.cursors.compile(cursorname, black='.', white='x', xor='o')
        pygame.mouse.set_cursor((24,24), hotspot, datatuple, masktuple )

    def getposondisplay(self):
        return self.posondisplay



class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long),
                ("y", ctypes.c_long)]

class cursors:

    paintbrush = (               #sized 24x24
      "                        ",
      "                        ",
      "                        ",
      "                        ",
      "                        ",
      "        x               ",
      "       x.xx             ",
      "       xx.xx            ",
      "      x..x..x           ",
      "     x.x...xxx          ",
      "    x...x.xxx.x         ",
      "     x....xx..x         ",
      "      x..xx...x         ",
      "       xxxx....xx       ",
      "        xx..x...xx      ",
      "          xx x...xx     ",
      "              x...x     ",
      "               xxax     ",
      "                xxx     ",
      "                        ",
      "                        ",
      "                        ",
      "                        ",
      "                        ")

    regmouse = (               #sized 24x24
      "                        ",
      "                        ",
      "                        ",
      "                        ",
      "          oo            ",
      "          oo            ",
      "          oo            ",
      "          oo            ",
      "          oo            ",
      "          oo            ",
      "          oo            ",
      "   oooooooooooooooo     ",
      "   oooooooooooooooo     ",
      "          oo            ",
      "          oo            ",
      "          oo            ",
      "          oo            ",
      "          oo            ",
      "          oo            ",
      "          oo            ",
      "                        ",
      "                        ",
      "                        ",
      "                        ")

    dropper = (               #sized 24x24
      "                        ",
      "                        ",
      "                        ",
      "                        ",
      "                        ",
      "      xxx               ",
      "      x..x              ",
      "      x...x             ",
      "       x...x            ",
      "        x...x           ",
      "         x...x          ",
      "          x...x         ",
      "           x...x        ",
      "            x...x x     ",
      "             x...xx     ",
      "             xx.xxxxx   ",
      "            xxxxxxxxx   ",
      "               xxxxxx   ",
      "                xxx     ",
      "                        ",
      "                        ",
      "                        ",
      "                        ",
      "                        ")

    eraser = (               #sized 24x24
      "                        ",
      "                        ",
      "                        ",
      "                        ",
      "                        ",
      "      xxx               ",
      "     x...x              ",
      "     x...xx             ",
      "     x...x.x            ",
      "     x...x..x           ",
      "     x...x...x          ",
      "     x...x....x         ",
      "     xxxx......x        ",
      "      x..x......x       ",
      "       x..x......x      ",
      "        x..x....x       ",
      "         x..x..x        ",
      "          xxxxx         ",
      "                        ",
      "                        ",
      "                        ",
      "                        ",
      "                        ",
      "                        ")
