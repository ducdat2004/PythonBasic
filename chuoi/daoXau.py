s = input().strip()
n = int(input())
for _ in range(n):
    l = list(map(int, input().split()))
    x = s[l[0] - 1 : l[1]]
    y = s[l[2] - 1 : l[3]]
    if len(x) != len(y):
        print("NO")
    else:
        x = sorted(x)
        y = sorted(y)
        if x == y:
            print("YES")
        else:
            print("NO")