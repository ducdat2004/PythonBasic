n, k = map(int, input().split())
for _ in range(n):
    s = input()
    news = ""
    for i in s:
        if i.isupper():
            if ord(i) + k <= ord('Z'):
                news += chr(ord(i) + k)
            else:
                news += chr(ord('A') + ((ord(i) + (k - 1)) - ord('Z')))
        else:
            news += i
    print(news)