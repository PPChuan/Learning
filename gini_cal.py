while True:
    a = int(input("输入分子1:"))
    b = int(input("输入分母1:"))

    c = int(input("输入切分点1:"))
    d = int(input("输入切分点2:"))

    p1 = 1 - c / a * c / a - (a - c) / a * (a - c) / a
    p2 = 1 - d / (b - a) * d / (b - a) - (b - a - d) / (b - a) * (b - a - d) / (b - a)
    out = a / b * p1 + (b - a) / b * p2
    print(out)
