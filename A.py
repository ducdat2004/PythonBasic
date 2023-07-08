sopt = int(input())
arr = []
for i in range(sopt):
    arr.append(int(input()))
chan = 0
le = 0
am = 0
duong = 0
for i in arr:
    if i % 2 == 0:
        chan += 1
    if i % 2 != 0:
        le += 1
    if i >= 0:
        duong += 1
    if i < 0:
        am += 1
print(am)
print(duong)
print(chan)
print(le)