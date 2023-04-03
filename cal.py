import math

d = 0.14
a = 8/20
b = 7/20
c = 1 - a - b
e = -1*(a * math.log(a,2) + b * math.log(b,2) + c * math.log( c,2))
print(e)
print(d/e)