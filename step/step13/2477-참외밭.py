K = int(input())
side = []
side_ind = [0,0,0,0,0]
for i in range(6):
    temp = list(map(int,input().split()))
    side_ind[temp[0]] += 1
    side.append(temp)

#print(side_ind)
long_ind = []
for i in range(1,5):
    if side_ind[i] == 1:
        long_ind.append(i)

long_side = []
short_side = []

for i in range(6):
    if side[i][0] == long_ind[0]:
        long_side.append(side[i][1])
        if side[(i-1)%6][0] == long_ind[1]:
            long_side.append(side[(i-1)%6][1])
            short_side.append(side[(i+2)%6][1])
            short_side.append(side[(i+3)%6][1])
        elif side[(i+1)%6][0] == long_ind[1]:
            long_side.append(side[(i+1)%6][1])
            short_side.append(side[(i+3)%6][1])
            short_side.append(side[(i+4)%6][1])

#print(long_side)
#print(short_side)
print(K*(long_side[0]*long_side[1]-short_side[0]*short_side[1]))