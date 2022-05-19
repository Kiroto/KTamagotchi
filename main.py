from game import main
from classlib.utils.colorlib import resetColor
from classlib.console import Console


def initialize():
    resetColor()
    Console.clr_scr()


def finish():
    resetColor()
    Console.clr_scr()


if __name__ == "__main__":
    initialize()
    main()
    finish()
