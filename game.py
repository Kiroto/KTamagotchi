from time import sleep
from classlib.gameDataFolder import GameDataFolder
from classlib.model.pet import Pet, randomFromList
from classlib.model.petFace import PetFace
from classlib.console import Console
from classlib.soundEngine import SoundEngine, SoundFile

gameDataFolder = GameDataFolder()

def end():
    Console.print("GoodBye")
    sleep(3)


def main():
    validExpressions = list(PetFace.EXPRESSION_DICT.keys())
    while(Console.getch() != 3):
        pet = Pet()
        randomExpression = randomFromList(validExpressions)
        SoundEngine.playAsync(SoundFile.CURSOR)
        Console.print(pet.faceSet.getFace(randomExpression))
    # pet.name = "Batata"
    # Console.moveCursorXY(5, 5)
    # Console.print(pet.name, RGBColor(pet.color))
    # Console.moveCursorXY(5, 6)
    # health = pet.getHealth()
    # ratio = health / Score.MAX_VALUE
    # healthColor = RGBColor.interpolate(RGBColor(0xee3333), RGBColor(0x55ee55), ratio)
    # Console.print(str(health), healthColor)
    end()
