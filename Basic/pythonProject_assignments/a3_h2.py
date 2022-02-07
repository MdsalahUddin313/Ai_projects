gtp=[(1,1,1), (2,1,2), (3,1,3), (4,2,3), (5,3,3), (6,3,2), (7,3,1), (8,2,1)]
gblnk = (2,2)
tp=[(1,1,2), (2,1,3), (3,2,1), (4,2,3), (5,3,3), (6,2,2), (7,3,2), (8,1,1)]
blnk = (3,1)
i=0
distList=[] #Used to store the distances for each tile
totalDist=0
while(i<len(gtp)):
   dist=abs(gtp[i][1]-tp[i][1]) + abs(gtp[i][2]-tp[i][2])
   totalDist += dist
   distList.append(dist)
   i=i+1

for j in range(len(distList)):
   print("Distance for tile ",j+1," is ",distList[j])
print("Total Manhattan Distance is = ", totalDist)