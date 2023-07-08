def dal(h, a, b):
    count = 0
    ht = 0
    if a <= b:
        return -1
    elif a > h:
        return -1
    else:
        while ht < h - 1:
            ht += a
            ht -= b
            count += 1
        return count

h, a, b = map(int, input().split())

soNgay = dal(h, a, b)

print(soNgay)