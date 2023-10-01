s = input().strip()
c = 0
j = len(s) - 1
for i in range(len(s)//2):
    if s[i] != s[j]:
        c += 1
    j -= 1
print(c)