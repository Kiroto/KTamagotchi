from enum import Enum
from pygame import mixer, time
from src.dataFile import DataFile

class AudioFile(Enum):
    CURSOR = DataFile("cursor.wav")
    POWERUP = DataFile("powerUp.wav")
    MUSIC = DataFile("SomeSongC.wav")

mixer.init()

class SoundEngine:
    BGM : mixer.Sound = None
    BGMCH : mixer.Channel = None

    @staticmethod
    def playBgm(soundFile: AudioFile):
        if (SoundEngine.BGMCH != None):
            SoundEngine.BGMCH.fadeout(100)

        dataFile: DataFile = soundFile.value
        binFile: bytes = dataFile.getBin()
        SoundEngine.BGM = mixer.Sound(binFile)
        SoundEngine.BGM.set_volume(0.2)
        SoundEngine.BGMCH = SoundEngine.BGM.play(-1, fade_ms=100)


    @staticmethod
    def play(soundFile: AudioFile, block: bool = False):
        dataFile: DataFile = soundFile.value
        binFile: bytes = dataFile.getBin()

        sound = mixer.Sound(buffer=binFile)
        sound.set_volume(0.2)
        audio = sound.play()
        while (block and audio.get_busy()):
            time.Clock().tick(10)