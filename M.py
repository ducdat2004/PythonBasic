def tongS(m, n):
    d = m % 10
    h = n % 10
    S = d + h
    return S
def TichP(m, n):
    a = m // 1000
    e = n // 1000
    P = a * e
    return P

m, n = map(int, input().split())

S = tongS(m, n)
P = TichP(m, n)
print(S)
print(P)