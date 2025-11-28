import math

def square(side):
    return math.ceil(side ** 2)

side_length = 3.2
result = square(side_length)
print(f"Площадь квадрата со стороной {side_length}: {result}")
