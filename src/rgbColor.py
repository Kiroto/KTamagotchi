class RGBColor():
    @staticmethod
    def interpolate(a: 'RGBColor', b: 'RGBColor', value: float):
        r = int(a.r + (b.r - a.r) * value)
        g = int(a.g + (b.g - a.g) * value)
        b = int(a.b + (b.b - a.b) * value)
        return RGBColor.fromRGB(r, g, b)

    def __init__(self, hex: int):
        hex = int(hex)
        self.r : int = (hex >> 16) & 0xFF
        self.g : int = (hex >> 8) & 0xFF
        self.b : int = (hex) & 0xFF

    def getHex(self: 'RGBColor') -> int:
        return RGBColor.getHexFromRgb(self.r, self.g, self.b)

    @staticmethod
    def getHexFromRgb(r: int, g: int, b: int) -> int:
        return int(r) * 0x10000 + int(g) * 0x100 + int(b)
    
    @staticmethod
    def fromRGB(r: int, g: int, b: int) -> int:
        return RGBColor(RGBColor.getHexFromRgb(r, g, b))

    def inverted(self) -> 'RGBColor':
        return RGBColor(self.getHex())

    def consoleColorString(self) -> str:
        return f";{int(self.r)};{int(self.g)};{int(self.b)}"
