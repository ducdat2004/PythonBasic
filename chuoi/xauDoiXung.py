s = input().strip()
d = 0
c = len(s) // 2
s1 = [s[i] for i in range(c)]
s2 = [s[i] for i in range(len(s) - 1, c, -1)]
x = lambda s1, s2: len(s1) if len(s1) < len(s2) else len(s2)
print(s1, s2)
for i in range(x(s1, s2)):
    if s1[i] != s2[i]:
        d += 1 
print(d)