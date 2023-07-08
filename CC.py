n = int(input())

count = 0
arr = []
for i in range(1, n+1):
    if n % i == 0:
        count += 1
        arr.append(i)
print(count)
for i in arr:
    print(i, end=' ')