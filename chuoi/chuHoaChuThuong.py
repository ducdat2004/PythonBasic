while 123:
    try:
        s = input()
        hoa = [i for i in s if i.isupper()]
        thuong = [i for i in s if i.islower()]
        if len(hoa) > len(thuong):
            print(s.upper())
        else:
            print(s.lower())
    except:
        break