class Calculation:
    def __init__(self):
        self._values = []
    
    def addValues(self, *args):
        self._values = args

    def sumValues(self):
        return sum(self._values)

    def subtraction(self):
        value = 0
        count = 0
        for i in range(len(self._values)):
            if count == 0:
                value += self._values[i]
            elif count > 0:
                value -= self._values[i]
            count+=1
        return value

    def division(self):
        try:
            self._values[0] /  self._values[1]
        except ZeroDivisionError as zeroDiv:
            return zeroDiv


