import os
from .file import File
from .pet import Pet


class GameDataFolder():
    # Obtains the Game Data folder
    @staticmethod
    def getGameDataFolder():
        appData = os.getenv("APPDATA")
        return File(os.path.join(appData, "KTamagotchi"))

    def __initializeAppData(self):
        self.file.mkDir()

    def __init__(self):
        self.file = GameDataFolder.getGameDataFolder()
        self.__initializeAppData()

    def savePet(self, pet: Pet):
        petFile = self.file.resolve("pet.ktg")
        if not petFile.isFile():
            petFile.mkFile()
        petFile.pickleDump(pet)

    def loadPet(self):
        petFile = self.file.resolve("pet")
        if not petFile.isFile():
            raise "No Pet File"
        loadedPet: Pet = petFile.pickleLoad()
        return loadedPet
