def kt(s1, s2):
    if len(s1) != len(s2):
        return 'NO'

    char_count = [0] * 26  # Số lần xuất hiện của các ký tự từ 'a' đến 'z'

    for char in s1:
        char_count[ord(char) - ord('a')] += 1

    for char in s2:
        char_count[ord(char) - ord('a')] -= 1
    print(char_count)
    for count in char_count:
        if count != 0:
            return 'NO'

    return 'YES'


s = input()
n = int(input())
for _ in range(n):
    m = list(map(int, input().split()))
    s1 = s[m[0] - 1: m[1]]
    s2 = s[m[2] - 1: m[3]]
    print(kt(s1, s2))