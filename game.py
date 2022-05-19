from time import sleep
from classlib.dataFolder import GameDataFolder
from classlib.pet import Pet
from classlib.utils.colorlib import RGBColor, printColorString, resetColor

gameDataFolder = GameDataFolder()

def end():
    printColorString("GoodBye")
    sleep(3)


def main():
    pet = Pet()
    pet.name = "Bakkelito♦♣♠"
    gameDataFolder.savePet(pet)
    pet.name = "Romeo"
    pet = gameDataFolder.loadPet()
    printColorString(pet.name, RGBColor(0xaaaaff))
    printColorString(pet.health, RGBColor(0x44ee66), RGBColor(0x111155))
    end()
