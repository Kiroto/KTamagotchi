from cgitb import reset
import math

class RGBColor():
    def __init__(self, hex):
        self.r = (hex >> 16) & 0xFF
        self.g = (hex >> 8) & 0xFF
        self.b = (hex) & 0xFF


def setColor(fgHex: RGBColor):
    print(f'\x1b[38;2;{fgHex.r};{fgHex.g};{fgHex.b}m', end="")


def setBackground(bgHex: RGBColor):
    print(f'\x1b[48;2;{bgHex.r};{bgHex.g};{bgHex.b}m', end="")

def resetColor():
    print('\033[m', end="")

def printColorString(text:str, fgHex: RGBColor = None, bgHex: RGBColor = None, end: str = None):
    if (fgHex):
        setColor(fgHex)
    if (bgHex):
        setBackground(bgHex)
    print(text, end=end)
    resetColor()
