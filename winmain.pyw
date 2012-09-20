#MCSkin2D, a kind of funny skin editor!
#Programmed by SapperEngineer

import tkinter.filedialog as filedialog

import pygame
import pygame._view
from pygame.locals import *
pygame.init()

import drawboard
import colorselector
import inputengine
import contentloader
import messhandler
import mousehandler
import fontrenderer
import gui
import skinpreview
import colorshower
import pixscreener
import swatch
from buttonactions import *

class mcskin2d():
    def __init__(self):
        self.filedialog = filedialog
        self.pygame = pygame #Needed for external modules's benefit
        self.tv = self.pygame.display.set_mode((800, 500), DOUBLEBUF)


        #Initialize variables
        self.contentloader = contentloader.contentloader(self)
        self.drawboard = drawboard.drawboard((0, 0), self)
        self.colorselector = colorselector.colorselector((598, 290), self)
        self.inputengine = inputengine.inputengine()
        self.messhandler = messhandler.messhandler(self)
        self.mousehandler = mousehandler.mousehandler()
        self.fontrenderer = fontrenderer.fontrenderer("MC", self)
        self.skinpreview = skinpreview.skinpreview((640, 0), self)
        self.colorshower = colorshower.colorshower((10, 330), self)
        self.pixscreener = pixscreener.pixscreener()
        self.swatchpanel = swatch.swatches((220, 325), self)

        #Initialize gui stuff
        self.guibuffer = []
        self.guibuffer.append(gui.button(" Save", SAVESKIN, (9, 471), self))
        self.guibuffer.append(gui.button(" Undo", UNDO, (70, 471), self))
        self.guibuffer.append(gui.button(" Redo", REDO, (131, 471), self))
        self.guibuffer.append(gui.button(" ^^^Current Color", NOTHING, (3, 374), self))
        self.guibuffer.append(gui.button(" SaveIm", SAVEMODEL, (719, 326), self))
        self.guibuffer.append(gui.button(" Credits and Help", GETHELP, (8, 427), self))
        self.guibuffer.append(gui.button(" -> ", SHIFTRIGHT, (763, 290), self))
        self.guibuffer.append(gui.button(" <- ", SHIFTLEFT, (642, 290), self))


        self.rgbbuffer = {}
        self.rgbbuffer['r'] = gui.slider("                               R", 255, (220, 420), self)
        self.rgbbuffer['g'] = gui.slider("                               G", 255, (220, 445), self)
        self.rgbbuffer['b'] = gui.slider("                               B", 255, (220, 470), self)
        self.rgbbuffer['re'] = gui.textvariable((50, 23), (476, 420), self)
        self.rgbbuffer['ge'] = gui.textvariable((50, 23), (476, 445), self)
        self.rgbbuffer['be'] = gui.textvariable((50, 23), (476, 470), self)



        #Flip screen to start all changes
        self.tv.fill((240, 240, 240))
        pygame.display.flip()

        pygame.display.set_caption("MCSkinStudio")
        pygame.display.set_icon(self.contentloader.steveico)
        self.mousehandler.changecursor(mousehandler.cursors.regmouse)

    def mainloop(self):
        while 1:
            #Render stuff
            self.tv.fill((240, 240, 240))
    
            #RENDER CODE
            self.messhandler.registermesses([

                self.tv.blit(self.contentloader.mcwood, (0, 320)),
                self.tv.blit(self.colorselector.getsurface(), self.colorselector.getpos()),
                self.tv.blit(self.colorshower.getsurface(), self.colorshower.getpos()),
                self.tv.blit(self.contentloader.TranspImage, self.drawboard.getpos()),
                self.tv.blit(self.drawboard.getgriddedsurface(), self.drawboard.getpos()),
                self.tv.blit(self.contentloader.mcmelon, self.skinpreview.getpos()),
                self.tv.blit(self.skinpreview.getsurface(), self.skinpreview.getpos()),
                self.tv.blit(self.swatchpanel.getsurface(), self.swatchpanel.getpos())

            ])

            #GUI RENDER CODE
            for element in self.guibuffer:
                self.messhandler.registermess(self.tv.blit(element.getsurface(), element.getpos()))

            for element in self.rgbbuffer:
                self.messhandler.registermess(self.tv.blit(self.rgbbuffer[element].getsurface(), self.rgbbuffer[element].getpos()))

            

            self.messhandler.cleanmesses() #Update them all

            #START INPUT CODE
            self.inputengine.copybuffer()
            if not (self.inputengine.mouseispushed(1) and self.inputengine.mouseispushed(3)):self.mousehandler.update()
            else:self.mousehandler.updateondisplay()
            self.inputengine.killifrequest()

            self.drawboard.draw()
            self.colorshower.update()

            self.skinpreview.update()

            self.swatchpanel.update()

            newcol = self.colorselector.getcol()
            if newcol: self.drawboard.color = list(newcol)

            for element in self.guibuffer: #GUI UPDATE
                element.update()

            for element in self.rgbbuffer: #GUI UPDATE
                if self.rgbbuffer[element].update():
                    if element == 'r':
                        self.drawboard.color[0] = self.rgbbuffer[element].getvalue()
                        self.rgbbuffer[element + 'e'].setvalue(self.rgbbuffer[element].getvalue())

                    if element == 'g':
                        self.drawboard.color[1] = self.rgbbuffer[element].getvalue()
                        self.rgbbuffer[element + 'e'].setvalue(self.rgbbuffer[element].getvalue())

                    if element == 'b':
                        self.drawboard.color[2] = self.rgbbuffer[element].getvalue()
                        self.rgbbuffer[element + 'e'].setvalue(self.rgbbuffer[element].getvalue())

            if self.inputengine.charpushed(chr(19)):
                #Save image
                try:
                    filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Minecraft Skin PNG file", ".png")])
                    pygame.image.save(pygame.transform.scale(self.drawboard.getsurface(), (64, 32)), filename)
                except:pass

            if self.inputengine.charpushed(chr(12)):
                filename = filedialog.askopenfilename()
                newsurf = pygame.image.load(filename).convert_alpha()
                self.drawboard.surface = newsurf

            if self.inputengine.mouseispushed(1) and self.inputengine.mouseispushed(3) and not self.mousehandler.getrect().colliderect(self.drawboard.getrect()):
                newcolor = self.drawboard.color = list(self.pixscreener.getpixel(self.mousehandler.getposondisplay()))
                self.rgbbuffer['r'].setslider(newcolor[0])
                self.rgbbuffer['g'].setslider(newcolor[1])
                self.rgbbuffer['b'].setslider(newcolor[2])



            self.inputengine.delbuffer()
            #END INPUT CODE


#Start the program
program = mcskin2d()
program.mainloop()
