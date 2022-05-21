from enum import Enum
from playsound import playsound

from classlib.file import File

class SoundFile(Enum):
    CURSOR = File("/resources/cursor.wav")

class SoundEngine:
    @staticmethod
    def playAsync(soundFile: SoundFile):
        playsound(soundFile.value.path, False)

    @staticmethod
    def play(soundFile: SoundFile):
        playsound(soundFile.value.path, True)
