
def ans():
    u = lambda c : 1 if c.isupper() else 0
    while True:
        count = 0
        try:
            s = input()
        except:
            break
        for i in s:
            count += u(i)
        print(count + 1)
ans()