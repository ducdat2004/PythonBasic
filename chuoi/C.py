ans = lambda s, i : s[i:] + s.split(s[i:])[0] if (i < len(s)) else s
n = int(input())
s = input()
print(ans(s, n % len(s)))