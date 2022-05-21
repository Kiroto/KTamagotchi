from game import main
from src.console import Console


def initialize():
    Console.resetColor()
    Console.clr_scr()


def finish():
    Console.resetColor()
    Console.clr_scr()


if __name__ == "__main__":
    initialize()
    main()
    finish()
