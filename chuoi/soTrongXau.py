try:
    s = input()
    i = 0
    dem = 0
    while i < len(s):
        if s[i].isnumeric():
            while i < len(s) and s[i].isnumeric():
                i += 1
            dem += 1
        else:
            i += 1
    print(dem)
except:
    print(0)