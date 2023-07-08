def chuyenHe10Sang16(n):
    arr = []
    
    while n > 0:
        soDu = n % 16
        n //= 16
        arr.append(soDu)
    he16 = {
        10 : 'A',
        11 : 'B',
        12 : 'C',
        13 : 'D',
        14 : 'E',
        15 : 'F',
    }
    he10 = ""
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] > 9 and arr[i] < 16:
            he10 += he16[arr[i]]
        else:
            he10 += str(arr[i])
    return he10

n = int(input())

result = chuyenHe10Sang16(n)
print(result)