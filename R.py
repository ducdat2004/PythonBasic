def qds(a, b, v):
    count = 0
    s = 0
    while s != v:
        if s + a == v:
            s += a
        else:
            s += a - b
        count += 1
    return count
a, b, v = map(int, input().split())
if (a - b) != 1:
    kq = v // (a - b)
else:
    kq = v - b
# if (a-b) * kq < v and (a-b) != 1:
#     kq += 1
print(kq)