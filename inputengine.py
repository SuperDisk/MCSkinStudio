#Input Engine, just delivers inputs back
#Programmed by SapperEngineer

import sys
import pygame
from pygame.locals import *


#When using this, be sure to first do copybuffer,
#Process the events, and then delbuffer.


class inputengine:
    def __init__(self):
        self.eventlist = []
        self.mousepushes = {1 : False, 2 : False, 3 : False, 13 : False, 12 : False, 23: False}

    def copybuffer(self):
        for item in pygame.event.get():
            self.savemouse(item)
            self.eventlist.append(item)

    def savemouse(self, event):
        if event.type == MOUSEBUTTONDOWN:
            self.mousepushes[event.button] = True

            if event.button == 1 and self.mousepushes[3]:
                self.mousepushes[13] = True

            if event.button == 1 and self.mousepushes[2]:
                self.mousepushes[12] = True

            if event.button == 2 and self.mousepushes[3]:
                self.mousepushes[23] = True

        elif event.type == MOUSEBUTTONUP:
            self.mousepushes[event.button] = False

            if event.button == 1:
                self.mousepushes[13] = False
                self.mousepushes[12] = False

            if event.button == 2:
                self.mousepushes[23] = False
                self.mousepushes[12] = False

            if event.button == 3:
                self.mousepushes[23] = False
                self.mousepushes[13] = False

    def getbuffer(self):
        return self.eventlist

    def delbuffer(self):
        self.eventlist = []

    def showbuffer(self):
        print(self.eventlist)

    def buffernotempty(self):
        if self.eventlist != []: return True
        else: return False

    def getkeys(self): #Generator!
        for event in self.eventlist:
            if event.type == KEYDOWN:
                yield event.key

    def getchars(self):
        for event in self.eventlist:
            if event.type == KEYDOWN:
                yield event.unicode

    def charpushed(self, char):
        for event in self.eventlist:
            if event.type == KEYDOWN and event.unicode == char:
                return True

        return False


    def keypushed(self, key):
        for event in self.eventlist:
            if event.type == KEYDOWN and event.key == key:
                return True

        return False

    def keyrelease(self, key):
        for event in self.eventlist:
            if event.type == KEYUP and event.key == key:
                return True

        return False

    def mousepushed(self, button):
        for event in self.eventlist:
            if event.type == MOUSEBUTTONUP and event.button == button:
                return True

        return False

    def mousemotion(self):
        for event in self.eventlist:
            if event.type == MOUSEMOTION:
                return event.rel

        return False

    def mouserelease(self, button):
        for event in self.eventlist:
            if event.type == MOUSEBUTTONUP and event.button == button:
                return True

        return False

    def mouseispushed(self, button):
        if button == 1 and not self.mousepushes[13] and not self.mousepushes[12]:
            return self.mousepushes[button]

        if button == 2 and not self.mousepushes[23] and not self.mousepushes[12]:
            return self.mousepushes[button]

        if button == 3 and not self.mousepushes[13] and not self.mousepushes[23]:
            return self.mousepushes[button]


    def killifrequest(self):
        for event in self.eventlist:
            if event.type == KEYDOWN and event.key == K_ESCAPE:sys.exit()
            if event.type == QUIT: sys.exit()
