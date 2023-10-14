p = input()
t = input()
tong = i = 0
while 1:
    s = t[i : i+len(p)]
    if len(s) != len(p):
        break
    l = []
    for k in range(len(s)):
        if s[k] == p[k]:
            l.append(s[k])
    tong += len(l)
    i += 1
print(tong)