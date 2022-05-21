from time import sleep
from classlib.gameDataFolder import GameDataFolder
from classlib.model.pet import Pet, Score
from classlib.rgbColor import RGBColor
from classlib.console import Console

gameDataFolder = GameDataFolder()

def end():
    Console.print("GoodBye")
    sleep(3)


def main():
    pet = Pet()
    Console.print(pet.faceSet.getFace())
    # pet.name = "Batata"
    # Console.moveCursorXY(5, 5)
    # Console.print(pet.name, RGBColor(pet.color))
    # Console.moveCursorXY(5, 6)
    # health = pet.getHealth()
    # ratio = health / Score.MAX_VALUE
    # healthColor = RGBColor.interpolate(RGBColor(0xee3333), RGBColor(0x55ee55), ratio)
    # Console.print(str(health), healthColor)
    end()
