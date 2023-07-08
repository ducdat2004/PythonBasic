def phongDoanCollatz(n):
    count = 1
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        elif n % 2 != 0 and n > 1:
            n = n * 3 + 1
        count += 1
    return count

n = int(input())

doDai = phongDoanCollatz(n)

print(doDai)