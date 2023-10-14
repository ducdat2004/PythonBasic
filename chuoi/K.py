def maHoa(s, k):
    kq = ""
    for i in s:
        if i.isalpha():
            if ord(i) + k <= ord('Z'):
                c = ord(i)
            else:
                c = ord(i) - 90 + 64
            kq += chr(c + k)
        else:
            kq += i
    return kq
def ans():
    n, k = map(int, input().split())
    for i in range(n):
        s = input().strip()
        print(maHoa(s, k))
ans()