n = int(input())
a = 1
b = 2
for i in range(2, n+1):  
    lucas = a + b
    b = a
    a = lucas
print(lucas)