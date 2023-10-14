while 'dat':
    try:
        s = input().lower()
        l = [i for i in s if i in ['a', 'o', 'y', 'i', 'e', 'u']]
        print(len(l))
    except:
        break