s = input().strip().lower()
t = False
for i in range(1, len(s)):
        if s[i] != s[0]:
            t = True
if t == False:
    print(1)
else:
    x = set()
    # x.add("".join(sorted([i for i in s], reverse=True)))
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            x.add(s[:i]+s[j+1:]+s[i:j+1])
            x.add(s[i:j+1]+s[:i]+s[j+1:])
            q = s[i:j+1]
            # s1 = "".join(sorted([i for i in q]))
            # s2 = "".join(sorted([i for i in q], reverse=True))
            # s1 += s[:i]+s[j+1:]
            # s2 += s[:i]+s[j+1:]
            # x.add(s1)
            # x.add(s2)
    print(len(x))