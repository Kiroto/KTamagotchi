from enum import Enum
from random import random
from src.console import Console
from src.model.petCheeks import PetCheeks
from src.model.petEyes import Direction, EyeState, PetEyeSet
from src.model.petMouth import MouthState, PetMouthSet
from src.rgbColor import RGBColor


class Expression(Enum):
    NEUTRAL = 0,
    HAPPY = 1,
    SAD = 2,
    SMILE = 3


class PetFace:
    def __init__(self, cheeks: PetCheeks, eyeset: PetEyeSet, mouthset: PetMouthSet, furDensity: float = 0.1):
        if (furDensity == None):
            furDensity = random()
        self.furDensity: float = furDensity
        self.cheeks: PetCheeks = cheeks
        self.eyes: PetEyeSet = eyeset
        self.mouth: PetMouthSet = mouthset
        self.whiskers = "="

        self.colors: dict[str, RGBColor] = {
            "fur": RGBColor(random() * 0xffffff),
            "mouth" : RGBColor(random() * 0xffffff),
            "eyes": RGBColor(random() * 0xffffff),
            "cheeks": RGBColor(random() * 0xffffff)
        }


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

        furColor = self.colors["fur"]
        cheekColor = self.colors["cheeks"]
        mouthColor = self.colors["mouth"]
        eyesColor = self.colors["eyes"]

        furColorString = Console.getFGColorString(furColor)
        cheekColorStrinig = Console.getFGColorString(
            RGBColor.interpolate(cheekColor, furColor, density))
        mouthColorString = Console.getFGColorString(
            RGBColor.interpolate(mouthColor, furColor, density))
        eyesColorString = Console.getFGColorString(
            RGBColor.interpolate(eyesColor, furColor, density))

        return f"{furColorString}{whiskers}{cheekColorStrinig}{self.cheeks.left}{eyesColorString}{eyes.getLooking(Direction.RIGHT)}{mouthColorString}{mouth}{eyesColorString}{eyes.getLooking(Direction.LEFT)}{cheekColorStrinig}{cheeks.right}{furColorString}{self.whiskers}"
