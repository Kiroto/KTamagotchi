from time import sleep
from src.gameDataFolder import GameDataFolder
from src.model.pet import Pet, randomFromList
from src.model.petFace import PetFace
from src.console import Console
from src.soundEngine import SoundEngine, SoundFile

gameDataFolder = GameDataFolder()

def end():
    Console.print("GoodBye")
    sleep(3)


def main():
    validExpressions = list(PetFace.EXPRESSION_DICT.keys())
    while(Console.getch() != 3):
        pet = Pet()
        randomExpression = randomFromList(validExpressions)
        SoundEngine.playAsync(SoundFile.POWERUP)
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
