string = input("Enter positions: ")
l = [[0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]]
indices = []
total = 0
for i in range(len(string)):
   indices.append((i, int(string[i]) - 1))
# print(indices)
for i, j in indices:
   l[i][j] = 1
for x in range(8):
   print(l[x])
i = 0
while i < 8:
   count, j = 0, 0
   x, y = indices[i]
   # row check
   if sum(l[i]) > 1:
       count = sum(l[i]) - 1
   # diagonally down left check
   a, b = x, y
   a += 1
   b -= 1
   while a < 8 and b >= 0:
       if (l[a][b] == 1):
           count = count + 1
           break
       a = a + 1
       b = b - 1

   # diagonally down right check
   a, b = x, y
   a += 1
   b += 1
   while a < 8 and b < 8:
       if (l[a][b] == 1):
           count = count + 1
           break
       a = a + 1
       b = b + 1

   # diagonally up left check
   a, b = x, y
   a -= 1
   b -= 1
   while a >= 0 and b >= 0:
       if (l[a][b] == 1):
           count = count + 1
           break
       a = a - 1
       b = b - 1

   # diagonally up right check
   a, b = x, y
   a -= 1
   b += 1
   while a >= 0 and b < 8:
       # print("A s",a,"bs ",b)
       if l[a][b] == 1:
           count = count + 1
           break
       a = a - 1
       b = b + 1
   print("Attacking positions for the queen placed in (", x, ",", y, ") is ", count)
   total += count
   i = i + 1

print("H3 value: ", total)