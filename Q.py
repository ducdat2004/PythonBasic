import math
def giaiThua(n):
    gt = 1
    for i in range(1, n+1):
        gt *= i
    return gt
def tong(x):
    n = 1
    s = 0
    while abs(math.exp(x**n) / giaiThua(n)) < 10**9:
        s += math.exp(x**n) / giaiThua(n)
        n += 1
    return s

x = float(input())

print("{:.4f}".format(tong(x)))