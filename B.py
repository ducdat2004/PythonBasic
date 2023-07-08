import math
sopt = int(input())
arr = []
for i in range(sopt):
    arr.append(int(input()))
count = 0
for i in arr:
    i = math.sqrt(i)
    if i % 1 == 0:
        count += 1
print(count)