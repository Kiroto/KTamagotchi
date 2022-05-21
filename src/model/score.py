class Score:
    MAX_VALUE = 10.0
    def __init__(self, value: float = MAX_VALUE, multiplier: float = 1):
        self.value: float = value
        self.multiplier: float = multiplier

    def change(self, value: float):
        self.value += value
        overflow = 0.0
        if (self.value > Score.MAX_VALUE):
            overflow = Score.MAX_VALUE - self.value
            self.value = Score.MAX_VALUE
        elif (self.value < 0):
            overflow = -self.value
            self.value = 0
        return overflow

    def get(self):
        return self.value * self.multiplier