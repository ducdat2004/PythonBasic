n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
count = 0
for i in arr:
    if i % 3 == 0 or i % 5 == 0:
        count += 1
print(count)