import math

def kiemTraSoNT(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
           return False
    return True
n = int(input())
if kiemTraSoNT(n):
    print("Yes")
else:
    print("No")
# if cnt == 2:
#     print("Yes")
# else:
#     print("No")