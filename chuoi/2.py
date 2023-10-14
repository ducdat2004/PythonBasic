s = input().split()[-1]
print(s)
Anh = []
while 2:
    ten = input()
    if len(ten) == 0:
        break
    elif ten.split()[-1] == 'Anh':
        Anh.append(ten)
print("Danh sách sinh viên tên Anh")
for i in Anh:
    print(i)