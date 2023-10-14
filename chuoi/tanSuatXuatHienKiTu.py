s = input().strip()
s = [i for i in s if i.isalnum()]
so = [0] * 9
hoa = [0] * 26
thuong = [0] * 26
for i in s:
    if str(i).isdigit():
        so[ord(i) - ord('0')] += 1
    elif str(i).isupper():
        hoa[ord(i) - ord('A')] += 1
    elif str(i).islower():
        thuong[ord(i) - ord('a')] += 1
for i in range(len(so)):
    if so[i] != 0:
        print(chr(ord('0') + i)+'   ',so[i])
for i in range(len(hoa)):
    if hoa[i] != 0:
        print(chr(ord('A') + i)+'   ',hoa[i])
for i in range(len(thuong)):
    if thuong[i] != 0:
        print(chr(ord('a') + i)+'   ',thuong[i])