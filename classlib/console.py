import os
from classlib.rgbColor import RGBColor
from classlib.opSys import OpSys, CURRENT_OS

if CURRENT_OS == OpSys.WIN:
	import msvcrt
	from ctypes import *

	STD_OUTPUT_HANDLE = -11

	class COORD(Structure):
		pass

	COORD._fields_ = [("X", c_short), ("Y", c_short)]
else:
	import tty, termios, sys

class Console():
	@staticmethod
	def clr_scr():
		#Python program to clear screen
		#Get command to execute
		if(CURRENT_OS == OpSys.WIN):
			cmd = 'cls'
		else:
			cmd = 'clear'
		os.system(cmd)

	# ==================
	# Navigation Methods
	# ==================
	@staticmethod
	def moveCursorXY(xpos: int, ypos: int):
		if CURRENT_OS == OpSys.WIN:
			h = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
			windll.kernel32.SetConsoleCursorPosition(h, COORD(xpos, ypos))
		else:
			print(f"\033[{ypos};{xpos}H")

	# =============
	# Input Methods
	# =============
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

	# =============
	# Color Methods
	# =============
	@staticmethod
	def setColor(fgHex: RGBColor):
		print(f'\x1b[38;2;{fgHex.r};{fgHex.g};{fgHex.b}m', end="")

	@staticmethod
	def setBackground(bgHex: RGBColor):
		print(f'\x1b[48;2;{bgHex.r};{bgHex.g};{bgHex.b}m', end="")

	@staticmethod
	def resetColor():
		print('\033[m', end="")

	# ==============
	# Output Methods
	# ==============
	@staticmethod
	def printColorString(text:str, fgHex: RGBColor = None, bgHex: RGBColor = None, end: str = None):
		if (fgHex):
			Console.setColor(fgHex)
		if (bgHex):
			Console.setBackground(bgHex)
		print(text, end=end)
		Console.resetColor()
