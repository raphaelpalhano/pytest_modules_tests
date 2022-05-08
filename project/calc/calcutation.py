class Calculation:
    def __init__(self, *args):
        self.values = args
    

    def sumValues(self):
        return sum(self.values)

    def subtraction(self):
        value = 0
        count = 0
        for i in range(len(self.values)):
            if count == 0:
                value += self.values[i]
            elif count > 0:
                value -= self.values[i]
            count+=1
        return value

    def division(self):
        try:
            self.values[0] /  self.values[1]
        except ZeroDivisionError as zeroDiv:
            return zeroDiv


cal = Calculation(2,0)

print(cal.sumValues())
print(cal.subtraction())
print(cal.division())