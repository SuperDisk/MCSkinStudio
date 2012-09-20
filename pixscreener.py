from ctypes import windll

class pixscreener:
    def __init__(self):
        self.h = windll.user32.GetDC(0)
        
    def getpixel(self, pos):
        pixel = windll.gdi32.GetPixel(self.h, pos[0], pos[1])
        r = pixel % 256
        b = int(pixel / 65536)
        g = int((pixel - (b * 65536) - r) / 256)
        return r, g, b


if __name__ == "__main__":
    thepixscreener = pixscreener()
    while 1: print(thepixscreener.getpixel())
