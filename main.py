import math

def addmultiplenumbers(numbers):
    return sum(numbers)

def multiplymultiplenumbers(numbers):
    return math.prod(numbers)

def isiteven(number):
    return number % 2 == 0

def isitaninteger(num):
    return isinstance(num, int)

print(addmultiplenumbers([2, 4, 6]))
print(multiplymultiplenumbers([2, 3, 4]))
print(isiteven(4))
print(isitaninteger(6))