def ktt(s):
    a = s.split()
    kq = ""
    for i in a:
        kq += i + " "
    print(kq.strip())
while True:
    try:
        s = input()
    except:
        break
    ktt(s)