#MCSkin2D, a kind of funny skin editor!
#Programmed by SapperEngineer

from pygame.locals import *
import mousehandler
import queue

class drawboard: #The part where the user draws
    def __init__(self, pos, mcskin2d):
        self.pos = pos
        self.surface = mcskin2d.contentloader.Char
        self.rect = mcskin2d.pygame.Rect(pos, (640, 320))
        self.mcskin2d = mcskin2d
        self.backups = []
        self.junkbackups = []
        self.savebackup()
        self.color = [255, 255, 255]
        self.oldpos = [0, 0]
        
    def draw(self):
        
        if self.rect.colliderect(self.mcskin2d.mousehandler.getrect()):
            mousepos = self.mcskin2d.mousehandler.getpos()

            if self.mcskin2d.inputengine.mouseispushed(1):
                self.mcskin2d.skinpreview.update()
                self.surface.set_at((mousepos[0] // 10, mousepos[1] // 10), self.color)
                self.mcskin2d.mousehandler.changecursor(mousehandler.cursors.paintbrush)
                
            elif self.mcskin2d.inputengine.mouseispushed(2):
                self.color = self.surface.get_at((mousepos[0] // 10, mousepos[1] // 10))
                self.mcskin2d.rgbbuffer['r'].setslider(self.color[0])
                self.mcskin2d.rgbbuffer['g'].setslider(self.color[1])
                self.mcskin2d.rgbbuffer['b'].setslider(self.color[2])
                self.mcskin2d.mousehandler.changecursor(mousehandler.cursors.dropper)

            elif self.mcskin2d.inputengine.mouseispushed(3):
                self.mcskin2d.skinpreview.update()
                self.surface.set_at((mousepos[0] // 10, mousepos[1] // 10), (0, 0, 0, 0))
                self.mcskin2d.mousehandler.changecursor(mousehandler.cursors.eraser)

            else:
                self.mcskin2d.mousehandler.changecursor(mousehandler.cursors.regmouse, (12, 12))

            if self.mcskin2d.inputengine.mousepushed(1):
                self.savebackup()


        if self.mcskin2d.inputengine.charpushed(chr(26)): #Undo
            self.revertbackup()
            self.mcskin2d.skinpreview.update()

        if self.mcskin2d.inputengine.charpushed(chr(25)): #Redo
            self.restorebackup()
            self.mcskin2d.skinpreview.update()

        self.color = list(self.color)

        #Floodfill code, though it doesn't work
        '''if self.rect.colliderect(self.mcskin2d.mousehandler.getrect()): THIS DOOESN'T WORK
            mousepos = self.mcskin2d.mousehandler.getpos()
            if self.mcskin2d.inputengine.mousepushed(1):
                newsurf = self.floodfill(self.surface, mousepos, self.surface.get_at((mousepos[0] // 10, mousepos[1] // 10)), self.color)
                self.surface.blit(newsurf, (0, 0))
                self.mcskin2d.skinpreview.update()'''
            

    def floodfill(self, surface, startnode, target, replacement):
        lifo = queue.LifoQueue()
        lifo.put(startnode)
        surface = surface.copy()
        while not lifo.empty():
            
            n = lifo.get()
            if surface.get_at((n[0] // 10, n[1] // 10)) == target:
                surface.set_at((n[0] // 10, n[1] // 10), replacement)
                lifo.put((n[0] + 1, n[1]))
                lifo.put((n[0] - 1, n[1]))
                lifo.put((n[0], n[1] + 1))
                lifo.put((n[0], n[1] - 1))
                self.mcskin2d.pygame.display.flip()
                self.mcskin2d.pygame.event.pump()

            else:
                print("NOMATCH: ", surface.get_at((n[0] // 10, n[1] // 10)), target)

        return surface

    def savebackup(self):
        if len(self.backups) > 30:
            self.backups = []
            self.junkbackups = []

        self.backups.append(self.surface.copy())

    def revertbackup(self):
        try:
            self.junkbackups.append(self.backups[len(self.backups) - 1])
            del self.backups[len(self.backups) - 1]
            self.surface = self.backups[len(self.backups) - 1].copy()
        except:pass

    def restorebackup(self):
        try:
            del self.junkbackups[len(self.backups) - 1]
            self.surface = self.junkbackups[len(self.junkbackups) - 1].copy()
            self.savebackup()
        except:pass

    def getsurface(self):
        return self.mcskin2d.pygame.transform.scale(self.surface, (640, 320))

    def getgriddedsurface(self):
        if not self.mcskin2d.mousehandler.getrect().colliderect(self.rect):
            returnsurf = self.mcskin2d.pygame.transform.scale(self.surface.copy(), (640, 320))
            returnsurf.blit(self.mcskin2d.contentloader.CharOverlay, (0, 0))
            return returnsurf

        else:return self.getsurface()

    def getpos(self):
        return self.pos

    def getrect(self):
        return self.rect
