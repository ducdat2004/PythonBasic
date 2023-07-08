
n = int(input())
saoDau = 0
saoCuoi = n*2
arr = []
for i in range(n*2+1):
    ar = []
    for j in range(n*2+1):
        if j == saoDau or j == saoCuoi:
            ar.append("*")
        elif j != saoDau and j != saoCuoi:
            ar.append('.')
    saoDau+=1
    saoCuoi-=1
    arr.append(ar)
    
for i in arr:
    for j in i:
        print(j, end=' ')
    print()