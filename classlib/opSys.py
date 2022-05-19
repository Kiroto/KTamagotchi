import platform
from enum import Enum

class OpSys(Enum):
    UNK = -1,
    WIN = 0,
    LIN = 1,
    OSX = 2

def getSys():
    sysStr = platform.system().lower()
    sysDict = {
        "windows": OpSys.WIN,
        "mac": OpSys.OSX,
        "linux": OpSys.LIN
    }
    if (sysStr in sysDict.keys()):
        return sysDict[sysStr]
    return OpSys.UNK

CURRENT_OS = getSys()
