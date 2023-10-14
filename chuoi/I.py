def d(s):
    num = [0] * 10
    upper = [0] * 26
    lower = [0] * 26
    for i in s:
        if i.isnumeric():
            num[ord(i) - ord('0')] += 1
        elif i.isupper():
            upper[ord(i) - ord('A')] += 1
        elif i.islower():
            lower[ord(i) - ord('a')] += 1
    for i in range(len(num)):
        if num[i] != 0:
            print(chr(ord('0') + i) + "   ", num[i])
    for i in range(len(upper)):
        if upper[i] != 0:
            print(chr(ord('A') + i) + "   ", upper[i])
    for i in range(len(lower)):
        if lower[i] != 0:
            print(chr(ord('a') + i) + "   ", lower[i])
s = input()
d(s)