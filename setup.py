from cx_Freeze import setup, Executable
 
exe = Executable(
    script="winmain.pyw",
    base="Win32GUI",
    )
 
setup(
    name = "MCSkin2d",
    version = "0.1",
    description = "A cool Minecraft skin editor by SuperDisk!",
    executables = [exe]
    )
