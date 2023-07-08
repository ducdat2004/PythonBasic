def soDoiXung(n):
    ss1 = ""
    ss2 = ""
    stn = str(n)
    for i in range(len(stn)):
        ss1 += stn[i]
    for i in range(len(ss1) - 1, -1, -1):
        ss2 += stn[i]
    if ss1 == ss2:
        return True
    else:
        return False

n = int(input())

if soDoiXung(n):
    print("Yes")
else:
    print("No")