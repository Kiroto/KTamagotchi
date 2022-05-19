from enum import Enum
import platform
import os

os.system('')

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
	return OpSys.OSX

currentOS = getSys()

def clr_scr():
    #Python program to clear screen
    #Get command to execute
    if(currentOS == OpSys.WIN):
        cmd = 'cls'
    else:
        cmd = 'clear'
    os.system(cmd)

if platform.system() == "Windows":
	import msvcrt
	def getch():
		return msvcrt.getch()
else:
	import tty, termios, sys
	def getch():
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setraw(sys.stdin.fileno())
			ch = sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		return ch
