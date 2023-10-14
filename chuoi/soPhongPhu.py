def tongUocSo(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong
n = int(input())
tong = 0
for i in range(1, n+1):
    if tongUocSo(i) > i:
        tong += i
print(tong)