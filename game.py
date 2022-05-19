from time import sleep
from classlib.gameDataFolder import GameDataFolder
from classlib.pet import Pet
from classlib.rgbColor import RGBColor
from classlib.console import Console

gameDataFolder = GameDataFolder()

def end():
    inputstr= Console.getch()
    print(inputstr)
    Console.printColorString("GoodBye")
    sleep(3)


def main():
    pet = Pet()
    pet.name = "Bakkelito♦♣♠"
    gameDataFolder.savePet(pet)
    pet.name = "Romeo"
    pet = gameDataFolder.loadPet()
    Console.printColorString(pet.name, RGBColor(0xaaaaff))
    Console.printColorString(pet.health, RGBColor(0x44ee66), RGBColor(0x111155))
    end()
