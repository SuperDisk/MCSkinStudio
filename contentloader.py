#MCSkin2D, a kind of funny skin editor!
#Programmed by SapperEngineer

import glob, os


class contentloader:

    def __init__(self, mcskin2d):
        for item in glob.glob("2data\\*.tga"):
            setattr(self, os.path.basename(item).replace(".tga", ''), mcskin2d.pygame.image.load(item).convert_alpha())

    def getcontent(self, name):
        return getattr(content, name)

    def printcontent(self):
        print(dir(content))
