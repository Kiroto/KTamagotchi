from cgitb import reset
import math

class RGBColor():
    def __init__(self, hex):
        self.r = (hex >> 16) & 0xFF
        self.g = (hex >> 8) & 0xFF
        self.b = (hex) & 0xFF

