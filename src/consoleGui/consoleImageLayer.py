from enum import Enum, auto
from src.rgbColor import RGBColor


class OpacityMode(Enum):
    NONE = auto()
    AUTO = auto()
    FULL = auto()


class ConsoleImageLayer:
    @staticmethod
    def square(width: int, height: int, filler: str = " ", opacityMode: OpacityMode = OpacityMode.AUTO, color: RGBColor = RGBColor(0xffffff), bgColor: RGBColor = RGBColor(0)):
        ci = ConsoleImageLayer()
        ci.width = width
        ci.height = height
        ci.drawing = list()
        ci.color = color
        ci.backgroundColor = bgColor

        for y in range(height):
            ci.drawing.append(filler * width)

        ci.alpha = ConsoleImageLayer.makeOpacity(ci.drawing, opacityMode)

        return ci

    @staticmethod
    def makeOpacity(sourceImage: 'list[str]', opacityMode: OpacityMode) -> 'list[str]':
        alpha: list[str] = list()
        width = len(sourceImage[0])
        height = len(sourceImage)
        if (opacityMode == OpacityMode.AUTO):
            alpha = sourceImage.copy()
        else:
            alphaBg = "█"
            if (opacityMode == OpacityMode.NONE):
                alphaBg = " "
            for y in range(height):
                alpha.append(alphaBg * width)
        return alpha

    @staticmethod
    def stringBox(source: str, height: int, width: int, opacityMode: OpacityMode = OpacityMode.AUTO, color: RGBColor = RGBColor(0xffffff), bgColor: RGBColor = RGBColor(0)):
        ci = ConsoleImageLayer()
        ci.width = width
        ci.height = height

        ci.drawing = list()
        for y in range(height):
            srcLen = len(source)
            if len(source) > 0:
                ci.drawing += source[:min(width, srcLen)].ljust(width)
                source = source[min(width, srcLen):]
            else:
                break

        ci.alpha = ConsoleImageLayer.makeOpacity(ci.drawing, opacityMode)
        return ci

    def __init__(self):

        self.width: int
        self.height: int

        self.drawing: list[str]
        self.alpha: list[str]

        self.backgroundColor: RGBColor
        self.color: RGBColor
