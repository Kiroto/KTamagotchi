from time import sleep
from src.consoleGui.consoleBox import ConsoleBox
from src.gameDataFolder import GameDataFolder
from src.model.pet import Pet, randomFromList
from src.model.petFace import PetFace
from src.console import Console
from src.soundEngine import SoundEngine, AudioFile

gameDataFolder = GameDataFolder()

def end():
    Console.print("GoodBye")
    sleep(3)


def main():
    validExpressions = list(PetFace.EXPRESSION_DICT.keys())
    SoundEngine.playBgm(AudioFile.MUSIC)
    Console.draw(ConsoleBox.emptyBox(5, 5), 5, 5)
    while(Console.getch() != 3):
        pet = Pet()
        randomExpression = randomFromList(validExpressions)
        SoundEngine.play(AudioFile.POWERUP)
        Console.print(pet.faceSet.getFace(randomExpression))
    end()
