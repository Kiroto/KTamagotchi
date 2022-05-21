from enum import Enum
from random import random

from classlib.rgbColor import RGBColor


class EyeState(Enum):
    OPEN = 0,
    CLOSED = 1,
    SURPRISED = 2,
    HAPPY = 3,
    SAD = 4,
    SCARED = 5,
    DIZZY = 6,
    TIRED = 7,
    ANGRY = 8


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class PetEye:
    def __init__(self, eyeDirections: str):
        self.directions : dict[Direction, str] = {
            Direction.UP: eyeDirections[0],
            Direction.DOWN: eyeDirections[1],
            Direction.LEFT: eyeDirections[2],
            Direction.RIGHT: eyeDirections[3],
        }

    def getLooking(self, direction: Direction) -> str:
        return self.directions[direction]



class PetEyeSet:
    def __init__(self, petEyes: 'dict[EyeState, PetEye]', color: RGBColor = None):
        if (color == None):
            color = RGBColor(random() * 0xffffff)
        self.color = color
        self.stateImages: dict[EyeState, PetEye] = petEyes

petEyes : 'dict[str, PetEye]' = {
    "o": PetEye("oooo"),
    "line": PetEye("──¬⌐"),
    "wavy": PetEye("~~~~"),
    "O": PetEye("OOOO"),
    "n": PetEye("nnnn"),
    "^": PetEye("^^^^"),
    "u": PetEye("uuuu"),
    "dot": PetEye("∙.∙∙"),
    "bigDot": PetEye("••••"),
    "pressed": PetEye("vv><"),
    "square": PetEye("ΘΘΘΘ"),
    "dizzy": PetEye("@@@@"),
    "tired": PetEye("ºººº"),
    "angry": PetEye("ôôòó"),
}

petEyeSets : 'dict[str, PetEyeSet]' = {
    "regular": PetEyeSet({
        EyeState.OPEN : petEyes["o"],
        EyeState.CLOSED: petEyes["line"],
        EyeState.SURPRISED: petEyes["O"],
        EyeState.HAPPY : petEyes["^"],
        EyeState.SAD : petEyes["u"],
        EyeState.SCARED: petEyes["pressed"],
        EyeState.DIZZY: petEyes["dizzy"],
        EyeState.TIRED: petEyes["tired"],
        EyeState.ANGRY: petEyes["angry"],
    })
}
