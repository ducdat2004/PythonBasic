def hoa(s):
    c = 0
    u = lambda s : 1 if s.isupper() else 0
    for i in s:
        c += u(i)
    return c
def thuong(s):
    c = 0
    u = lambda s: 1 if s.islower() else 0
    for i in s:
        c += u(i)
    return c
def ans():
    u = lambda s : s.upper() if hoa(s) > thuong(s) else s.lower()
    kq = []
    while True:
        try:
            s = input()
        except:
            break
        # if bool(s) == False:
        #     break
        print(u(s))
ans()