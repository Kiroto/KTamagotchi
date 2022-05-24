from src.consoleGui.consoleImageLayer import ConsoleImageLayer, OpacityMode
from src.rgbColor import RGBColor

defaultBoxParts = "╔╗╚╝═║░"


class ConsoleBox:
    @staticmethod
    def emptyBox(width: int, height: int, opacityMode: OpacityMode = OpacityMode.AUTO, configuration: str = defaultBoxParts, color: RGBColor = RGBColor(0xFFFFFF), bgColor: RGBColor = RGBColor(0)):
        ci = ConsoleImageLayer()
        ci.color = color
        ci.backgroundColor = bgColor
        ci.drawing = list()
        barWidth = max(0, width - 2)

        for y in range(height):
            line = ""
            if (y == 0):
                line = (configuration[0] +
                        configuration[4] * barWidth +
                        configuration[1]
                        )
            elif (y != height - 1):
                line = (
                    configuration[5] +
                    configuration[6] * barWidth +
                    configuration[5]
                )
            else:
                line = (
                    configuration[2] +
                    configuration[4] * barWidth +
                    configuration[3]
                )
            ci.drawing.append(line[:width])
        ci.alpha = ConsoleImageLayer.makeOpacity(ci.drawing, opacityMode)
        ci.width = width
        ci.color = color
        ci.backgroundColor = bgColor
        return ci
