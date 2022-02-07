def find(tuplelist, start, end):
   x,index =0,0
   for i in range(len(tuplelist)):
       if tuplelist[i][0]==start and tuplelist[i][1]==end:
           x = int(tuplelist[i][2])
       if tuplelist[i][0]==start:
           index = i
   if x== 0:
       return tuplelist[index][2] + find(tuplelist, tuplelist[index][1], end)
   else:
       return x

tuplelist = [("i","a",35),("i","b",45),("a","c",22),("a","d",32),("b","d",28),("b","e",36),("b","f",27),
           ("c","d",31),("c","g",47),("d","g",30),("e","g",26)]

start=input("Enter starting node: ")
end=input("Enter destination node: ")

cost=0
neighbor=1

for i in range(len(tuplelist)):
   if start == tuplelist[i][0] and end == tuplelist[i][1]:
       cost=tuplelist[i][2]
       neighbor=0

if neighbor == 1:
   cost = find(tuplelist, start, end)

print(cost)