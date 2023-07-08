# def ttd(n):
#     if n < 0:
#         n *= -1
#         return n
#     else:
#         return  n
def tongChuSoChan(n):
    tong = 0
    if n < 0:
        n *= -1
    while n > 0:
        digit = n % 10
        n //= 10
        if digit % 2 == 0:
            tong += digit
    return tong

t = int(input())
arr = []
for i in range(t):
    n = int(input())
    arr.append(n) #exp 

for i in arr:
    print(tongChuSoChan(i))