while 2:
    try:
        s = input()
        u = [i for i in s if i.isupper()]
        print(len(u) + 1)
    except:
        break