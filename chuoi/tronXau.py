s1 = input().strip().lower()
s2 = input().strip().lower()
s = ""
if len(s1) > len(s2):
    for i in range(len(s2)):
        s += s1[i] + s2[i]
    s += s1[len(s2):]
else:
    for i in range(len(s1)):
        s += s1[i] + s2[i]
    s += s2[len(s1):]
print(s)