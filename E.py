n = int(input())
epsilon = 1e-9
x = 1/n
for a in range(1, 201):
    for b in range(1, 201):
        z = (1/a) + (1/b)
        if abs(z - x) < epsilon:
            print(a, b)
# lenList = len(arr)
# # for p in range(lenList - 2):
# #     i = arr[p]
# #     x = i[0]
# #     y = i[1]
# #     for k in range(p+1, lenList):
# #         j = arr[k]
# #         if (x == j[0] or x == j[1]) and (y == j[0] or y == j[1]):
# #             if i[0] <= j[0]:
# #                 arr.remove(j) 
# #                 lenList -= 1    