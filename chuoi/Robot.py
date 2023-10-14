m, n, x, y = map(int, input().split())
maTran = []
for _ in range(m):
    maTran.append(list(map(int, input().split())))
tong = maTran[x][y]  # gan gia tri ban dau la noi robot dung
while True:
    c = input().upper().strip()
    try:
        if c == "FINISH":
            break
        elif c == "RIGHT":
            y += 1
            tong += maTran[x][y]
        elif c == "LEFT":
            y -= 1
            tong += maTran[x][y]
        elif c == "UP":
            x -= 1
            tong += maTran[x][y]
        else:
            x += 1
            tong += maTran[x][y]
    except:
        tong+= maTran[x][y]
print(tong)