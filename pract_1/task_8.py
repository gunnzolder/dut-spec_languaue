# 8. Написати програму для розрахунку Z
# Z = ((9 * pi * t + 10 * cos(x)) / sqrt(t) - abs(sin(t))) * pow(e,x)
# Для введення даних використовуйте команду input, визначивши тип змінних.
# Результат вивести з двома знаками після коми. х - остання цифра у списку групи, t=1.

import math

message = """
This script will calculate the formula below:
Z = ((9 * Pi * 1 + 10 * cos(4)) / sqrt(1) - abs(sin(1))) * pow(e,4)
Please enter the value for 'e':
"""

print(message)
e = input()

Z = ((9 * math.pi * 1 + 10 * math.cos(4)) / math.sqrt(1) - abs(math.sin(1))) * pow(int(e),4)

print("Z =", "%.2f" % Z)