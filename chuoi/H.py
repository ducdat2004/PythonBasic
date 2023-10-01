def ktt(s):
    n = ""
    for i in s:
        if i not in n and i != ' ' and i.isalpha():
            n += i
    print(len(n))
a = input().lower()
ktt(a)