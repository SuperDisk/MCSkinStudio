SAVESKIN = [
    "filename = self.mcskin2d.filedialog.asksaveasfilename(defaultextension='.png', filetypes=[('Minecraft Skin PNG file', '.png')])",
    "self.mcskin2d.pygame.image.save(self.mcskin2d.pygame.transform.scale(self.mcskin2d.drawboard.getsurface(), (64, 32)), filename)"]

SAVEMODEL = [
    "filename = self.mcskin2d.filedialog.asksaveasfilename(defaultextension='.png', filetypes=[('MCSkin2d Model Image', '.png')])",
    "self.mcskin2d.pygame.image.save(self.mcskin2d.skinpreview.getsurface(), filename)"]

UNDO = [
    "self.mcskin2d.drawboard.revertbackup()",
    "self.mcskin2d.skinpreview.update()"]

REDO = [
    "self.mcskin2d.drawboard.restorebackup()",
    "self.mcskin2d.skinpreview.update()"]

GETHELP = [
    "import easygui",
    "easygui.msgbox('This software © SuperDisk 2012. For information and help, visit                     http://www.planetminecraft.com/member/superdisk/                              on the MCSkinStudio modpage.', title='Help')"]

SHIFTLEFT = [
    "self.mcskin2d.skinpreview.shiftleft()"]

SHIFTRIGHT = [
    "self.mcskin2d.skinpreview.shiftright()"]



NOTHING = ["pass"]
