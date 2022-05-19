import os
from classlib.rgbColor import RGBColor
from classlib.opSys import OpSys, CURRENT_OS

if CURRENT_OS == OpSys.WIN:
	import msvcrt
else:
	import tty, termios, sys

class Console():
	KeyboardDecoder = "ascii"

	@staticmethod
	def clr_scr():
		#Python program to clear screen
		#Get command to execute
		if(CURRENT_OS == OpSys.WIN):
			cmd = 'cls'
		else:
			cmd = 'clear'
		os.system(cmd)

	# Input Methods
	@staticmethod
	def getch():
		chNo = -1
		if CURRENT_OS == OpSys.WIN:
			ch = msvcrt.getch()
			chNo = ord(ch)
		else:
			fd = sys.stdin.fileno()
			old_settings = termios.tcgetattr(fd)
			try:
				tty.setraw(sys.stdin.fileno())
				ch = sys.stdin.read(1)[0]
				chNo = ord(ch)
			finally:
				termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		return chNo

	# Color Methods
	@staticmethod
	def setColor(fgHex: RGBColor):
		print(f'\x1b[38;2;{fgHex.r};{fgHex.g};{fgHex.b}m', end="")

	@staticmethod
	def setBackground(bgHex: RGBColor):
		print(f'\x1b[48;2;{bgHex.r};{bgHex.g};{bgHex.b}m', end="")

	@staticmethod
	def resetColor():
		print('\033[m', end="")

	@staticmethod
	def printColorString(text:str, fgHex: RGBColor = None, bgHex: RGBColor = None, end: str = None):
		if (fgHex):
			Console.setColor(fgHex)
		if (bgHex):
			Console.setBackground(bgHex)
		print(text, end=end)
		Console.resetColor()
