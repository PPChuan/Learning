import numpy as np


def se(a):
    sum = 0
    for i in range(0, len(a)):
        sum = a[i] + sum
    e = sum / len(a)
    se = 0
    for i in range(0, len(a)):
        se = se + (a[i] - e) * (a[i] - e)
    return se/len(a)

#
while True:
    arr = input("输入数组")
    a = [float(n) for n in arr.split()]
    for i in range(0, len(a) - 1):
        L1 = []
        L2 = []
        for j in range(0, len(a)):
            if j <= i:
                L1.append(a[j])
            else:
                L2.append(a[j])
        se1 = se(L1) * len(L1)
        se2 = se(L2) * len(L2)
        print("-----------------------")
        print(i+1)
        print(se1 + se2)
