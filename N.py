
def thuaSoNguyenTo(n):
    i = 2
    arr = []
    while i <= n:
        if n % i == 0:
            n = n // i
            print(i, end=' ')
        else:
            i += 1
    return arr

n = int(input())

thuaSoNguyenTo(n)
