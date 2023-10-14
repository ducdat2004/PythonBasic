s = input().lower()
c = lambda s : "YES" if len(set(s)) == len(tuple(s)) else "NO"
print(c(s))