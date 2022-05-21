from enum import Enum
import io
from pydub import AudioSegment
import simpleaudio
from src.dataFile import DataFile

class SoundFile(Enum):
    CURSOR = DataFile("/resources/cursor.wav")
    POWERUP = DataFile("/resources/powerUp.wav")


class SoundEngine:
    @staticmethod
    def playAsync(soundFile: SoundFile):
        binFile: bytes = soundFile.value.getBin()
        segment = AudioSegment.from_file(io.BytesIO(binFile), "wav")
        simpleaudio.play_buffer(
            segment.raw_data,
            num_channels=segment.channels,
            bytes_per_sample=segment.sample_width,
            sample_rate=segment.frame_rate
        )

    @staticmethod
    def play(soundFile: SoundFile):
        playsound(soundFile.value.getBin(), True)
