from random import random

class RGBColor():
    @staticmethod
    def interpolate(a: 'RGBColor', b: 'RGBColor', value: float):
        result = RGBColor()
        result.r = a.r + (b.r - a.r) * value
        result.g = a.g + (b.g - a.g) * value
        result.b = a.b + (b.b - a.b) * value
        result.normalizeColor()
        return result

    def __init__(self, hex: int = int(random() * 0xffffff)):
        hex = int(hex)
        self.r = (hex >> 16) & 0xFF
        self.g = (hex >> 8) & 0xFF
        self.b = (hex) & 0xFF

    def normalizeColor(self):
        self.r = int(self.r)
        self.g = int(self.g)
        self.b = int(self.b)

    def consoleColorString(self) -> str:
        return f";{int(self.r)};{int(self.g)};{int(self.b)}"

