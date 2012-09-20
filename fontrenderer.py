#Font Renderer, easy surface return fonts
#Programmed by SapperEngineer


class fontrenderer:
    def __init__(self, font, mcskin2d):
        self.mcskin2d = mcskin2d
        self.fontsmall = mcskin2d.pygame.font.Font("2data\\" + font + ".otf", 16)
        self.font = mcskin2d.pygame.font.Font("2data\\" + font + ".otf", 25)
        self.fontbig = mcskin2d.pygame.font.Font("2data\\" + font + ".otf", 40)

    def rendersmall(self, text, antialias=False, color=(0, 0, 0), dest=None, destpos=None):
        if dest == None: return self.fontsmall.render(text, antialias, color)
        else:
            dest.blit(self.fontsmall.render(text, antialias, color), destpos)

    def renderfont(self, text, antialias=False, color=(0, 0, 0), dest=None, destpos=None):
        if dest == None: return self.font.render(text, antialias, color)
        else:
            dest.blit(self.font.render(text, antialias, color), destpos)

    def renderbig(self, text, antialias=False, color=(0, 0, 0), dest=None, destpos=None):
        if dest == None: return self.fontbig.render(text, antialias, color)
        else:
            dest.blit(self.fontbig.render(text, antialias, color), destpos)

    def sizesmall(self, text):
        return self.fontsmall.size(text)[0] + 5, self.fontsmall.size(text)[1] + 3

    def size(self, text):
        return self.font.size(text)

    def sizebig(self, text):
        return self.fontbig.size(text)
