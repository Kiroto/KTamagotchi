from random import random
from classlib.rgbColor import RGBColor

class PetCheeks:
    def __init__(self, left: str, right: str, color: RGBColor = None) -> None:
        if (color == None):
            color = RGBColor(random() * 0xffffff)
        self.color: RGBColor = color
        self.left: str = left
        self.right: str = right


petCheeks: 'dict[str, PetCheeks]' = {
    "round": PetCheeks("(", ")"),
    "square": PetCheeks("[", "]"),
    "chew": PetCheeks("{", "}"),
    "tilted": PetCheeks("/", "\\"),
}
