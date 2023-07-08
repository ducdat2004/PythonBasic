import math
sopt = int(input())
arr = []
s = map(int, input().split())
for i in s:
    arr.append(i)
count = 0
for i in arr:
    i = math.sqrt(i)
    if i % 1 == 0:
        count += 1
print(count)