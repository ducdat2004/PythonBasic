s = str(input())
n = int(input())
x = map(int, input().split())
arr = []
for i in x:
    arr.append(i)
index = 0
for i in range(n):
    for j in range(arr[index]):
        print(s, end='')
    index += 1
    print()