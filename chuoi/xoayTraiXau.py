n = int(input())
s = input()
while n > len(s) - 1: # neu qua len thi reset ve 0 roi cong len tiep khi nao be hon len thi thoi
    n -= len(s)
print(s[n:] + s[0:n]) 