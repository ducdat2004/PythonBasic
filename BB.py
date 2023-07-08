n, p, q = map(int, input().split())


arr = []
for i in range(1, n +1):
    if i % p == 0 or i % q == 0:
        arr.append(i)
for i in arr:
    print(i, end=' ')