s = input().strip().upper()
if s.find('A') == -1 or s.find('Z') == -1:
    print(0)
else:
    l = []
    try:
        for i in range(len(s)):
            d = 0 
            if s[i] == "A":   
                for j in range(len(s) - 1, i, - 1):
                    if s[j] == "Z":
                        d = j - i
                        break
                l.append(d + 1)
    except:
        pass
    finally:
        print(max(l))