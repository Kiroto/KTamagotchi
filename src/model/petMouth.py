from enum import Enum

class MouthState(Enum):
    OPEN = 0,
    CLOSED = 1,
    SMILE = 2,
    BIG_SMILE = 3,
    SAD = 4,
    BIG_SAD = 5,
    POUT = 6,
    NERVOUS = 7,
    CHEW = 8

class PetMouth:
    def __init__(self, sprite: str):
        self.sprite = sprite

class PetMouthSet:
    def __init__(self, petMouth: 'dict[MouthState, PetMouth]'):
        self.stateImages: dict[MouthState, PetMouth] = petMouth


petMouths: 'dict[str, PetMouth]' = {
    "open": PetMouth(" o "),
    "closed": PetMouth(" . "),
    "nervous": PetMouth(" ~ "),
    "smile": PetMouth(" v "),
    "bigSmile": PetMouth(" V "),
    "content": PetMouth(" w "),
    "sad": PetMouth(" ^ "),
    "bigSad": PetMouth(" ^ "),
    "pout": PetMouth(".  "),
    "chew": PetMouth("~  "),
}

petMouthSets: 'dict[str, PetMouthSet]' = {
    "regular": PetMouthSet({
        MouthState.OPEN: petMouths["open"],
        MouthState.CLOSED: petMouths["closed"],
        MouthState.SMILE: petMouths["content"],
        MouthState.BIG_SMILE: petMouths["bigSmile"],
        MouthState.SAD: petMouths["sad"],
        MouthState.BIG_SAD: petMouths["bigSad"],
        MouthState.POUT: petMouths["pout"],
        MouthState.NERVOUS: petMouths["nervous"],
        MouthState.CHEW: petMouths["chew"],
    })
}
