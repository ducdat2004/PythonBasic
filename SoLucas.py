n = int(input())
if n == 0: 
    kq = 2
elif n == 1:
    kq = 1
else:
    a = 1
    b = 2
    for i in range(2, n+1):
        kq = a + b
        b = a
        a = kq
print(kq)