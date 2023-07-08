def tongCacChuSo(n):
    tong = 0
    if n < 0:
        n *= -1
    while n > 0:
        digit = n % 10
        if digit < 0:
            digit *= -1
        tong += digit
        n //= 10

    return tong


n = int(input())
print(tongCacChuSo(n))