n = int(input())
ds = []
m = f = 0
for _ in range(n):
    s = input().split(';')
    a = s
    if a[2].strip() == "M":
        m += 1
    else:
        f += 1
    ds.append(a)
def lop(e):
    return e[3]
ds.sort(key=lop)
print(m, f)
for i in ds:
    for j in i:
        if j != i[-1]:
            print(j, end=';')
        else:
            print(j, end="")
    print()