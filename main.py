from game import main
from classlib.utils.colorlib import resetColor
from classlib.utils.consolequirks import clr_scr


def initialize():
    resetColor()
    clr_scr()


def finish():
    resetColor()
    clr_scr()


if __name__ == "__main__":
    initialize()
    main()
    finish()
