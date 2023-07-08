def check(n):
    if n % 3 == 0 or n % 5 == 0:
        return True
    else:
        return False
    
n = int(input())

a = map(int, input().split())
count = 0
for i in a:
    if check(i):
        count += 1
print(count)