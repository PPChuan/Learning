import math


while True:
    numerator = float(input("输入分子"))
    denominator = float(input("输入分母"))
    x = numerator/denominator
    if x == 1 or x == 0:
        y = 0
    else:
        y = -1 * (x * math.log(x, 2) + (1 - x) * math.log(1 - x, 2))
    print(y)

