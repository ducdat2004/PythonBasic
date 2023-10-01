
def kt(s1, s2):
    if len(s1) != len(s2):
        return "NO"
    s1.lower()
    s2.lower()
    c = [0] * 26
    for i in s1:
        c[ord(i) - ord('a')] -= 1
    for i in s2:
        c[ord(i) - ord('a')] += 1
    for i in c:
        if i != 0:
            return "NO"
    return "YES"
s = input()
n = int(input())
for _ in range(n):
    m = list(map(int, input().split()))
    s1 = s[m[0] - 1 : m[1]]
    s2 = s[m[2] - 1 : m[3]]
    print(kt(s1, s2))