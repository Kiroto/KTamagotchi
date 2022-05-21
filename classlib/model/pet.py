from random import random
from classlib.model.petCheeks import petCheeks
from classlib.model.petEyes import petEyeSets
from classlib.model.petFace import PetFace
from classlib.model.petMouth import petMouthSets
from classlib.model.score import Score
from classlib.rgbColor import RGBColor

def randomFromList(thing: list):
    return list(thing)[int(random() * len(thing))]


class Pet:
    def __init__(self):
        self.name: str = "Mark"

        self.color : RGBColor = RGBColor()

        self.faceSet: PetFace = PetFace(randomFromList(petCheeks.values()), randomFromList(
            petEyeSets.values()), randomFromList(petMouthSets.values()))

        self.life: dict[Score] = {
            "saciety": Score(),
            "hygiene": Score(),
            "energy": Score(),
            "fun": Score(),
            "social": Score(),
            "bladder": Score(),
        }

        self.stats: dict[Score] = {
            "strength": Score(),
            "dexterity": Score(),
            "constitution": Score(),
            "intelligence": Score(),
            "wisdom": Score(),
            "charisma": Score(),
        }

    def getHealth(self) -> float:
        scores = self.life.values()
        addition : float = 0
        for score in scores:
            addition += score.value
        return addition / len(scores)



