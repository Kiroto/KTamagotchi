from enum import Enum
from random import random
from classlib.console import Console
from classlib.model.petCheeks import PetCheeks
from classlib.model.petEyes import Direction, EyeState, PetEyeSet
from classlib.model.petMouth import MouthState, PetMouthSet
from classlib.rgbColor import RGBColor


class Expression(Enum):
    NEUTRAL = 0,
    HAPPY = 1,
    SAD = 2,
    SMILE = 3


class PetFace:
    def __init__(self, cheeks: PetCheeks, eyeset: PetEyeSet, mouthset: PetMouthSet, fur: RGBColor = None, furDensity: float = 0.1):
        if (fur == None):
            fur = RGBColor()
        self.furColor: RGBColor = fur
        if (furDensity == None):
            furDensity = random()
        self.furDensity: float = furDensity
        self.cheeks: PetCheeks = cheeks
        self.eyes: PetEyeSet = eyeset
        self.mouth: PetMouthSet = mouthset
        self.whiskers = "="

    EXPRESSION_DICT : 'dict[Expression, tuple[EyeState, MouthState]]' = {
        Expression.NEUTRAL : (EyeState.OPEN, MouthState.SMILE),
        Expression.HAPPY: (EyeState.HAPPY, MouthState.SMILE),
        Expression.SMILE: (EyeState.HAPPY, MouthState.BIG_SMILE),
        Expression.SAD: (EyeState.SAD, MouthState.POUT)
    }

    def getFace(self, expression: Expression = Expression.HAPPY) -> str:
        eyeState, mouthState = PetFace.EXPRESSION_DICT[expression]
        eyes = self.eyes.stateImages[eyeState]
        mouth = self.mouth.stateImages[mouthState].sprite

        density = self.furDensity
        whiskers = self.whiskers
        cheeks = self.cheeks
        furColor = self.furColor
        defaultColor = Console.getFGColorString(furColor)
        cheeksColor = Console.getFGColorString(
            RGBColor.interpolate(cheeks.color, furColor, density))
        mouthColor = Console.getFGColorString(
            RGBColor.interpolate(self.mouth.color, furColor, density))
        eyesColor = Console.getFGColorString(
            RGBColor.interpolate(self.eyes.color, furColor, density))
        return f"{defaultColor}{whiskers}{cheeksColor}{self.cheeks.left}{eyesColor}{eyes.getLooking(Direction.RIGHT)}{mouthColor}{mouth}{eyesColor}{eyes.getLooking(Direction.LEFT)}{cheeksColor}{cheeks.right}{defaultColor}{self.whiskers}"
