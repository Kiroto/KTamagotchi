from random import random 
from time import sleep
from classlib.gameDataFolder import GameDataFolder
from classlib.model.pet import Pet, Score, randomFromList
from classlib.model.petFace import PetFace
from classlib.rgbColor import RGBColor
from classlib.console import Console

gameDataFolder = GameDataFolder()

def end():
    Console.print("GoodBye")
    sleep(3)


def main():
    validExpressions = list(PetFace.EXPRESSION_DICT.keys())
    while(True):
        pet = Pet()
        randomExpression = randomFromList(validExpressions)
        Console.print(pet.faceSet.getFace(randomExpression))
        sleep(1)
    # pet.name = "Batata"
    # Console.moveCursorXY(5, 5)
    # Console.print(pet.name, RGBColor(pet.color))
    # Console.moveCursorXY(5, 6)
    # health = pet.getHealth()
    # ratio = health / Score.MAX_VALUE
    # healthColor = RGBColor.interpolate(RGBColor(0xee3333), RGBColor(0x55ee55), ratio)
    # Console.print(str(health), healthColor)
    end()
