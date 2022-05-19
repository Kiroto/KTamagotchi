import os
from time import sleep
from classlib.file import File
from classlib.pet import Pet
from classlib.utils.colorlib import RGBColor, printColorString, resetColor


def getGameDataFolder():
    appData = os.getenv("APPDATA")
    return File(os.path.join(appData, "KTamagotchi"))


dataFolder = getGameDataFolder()


def initializeAppData():
    dataFolder.mkDir()


def savePet(pet: Pet):
    petFile = dataFolder.resolve("pet")
    if not petFile.isFile():
        petFile.mkFile()
    petFile.pickleDump(pet)


def loadPet():
    petFile = dataFolder.resolve("pet")
    if not petFile.isFile():
        raise "No Pet File"
    loadedPet: Pet = petFile.pickleLoad()
    return loadedPet


def end():
    printColorString("GoodBye")
    sleep(3)


def main():
    initializeAppData()
    pet = Pet()
    pet.name = "Bakkelito♦♣♠"
    savePet(pet)
    pet.name = "Romeo"
    pet = loadPet()
    printColorString(pet.name, RGBColor(0xaaaaff))
    printColorString(pet.health, RGBColor(0x44ee66), RGBColor(0x111155))
    end()
