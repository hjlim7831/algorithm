def d(n):
    nn = n
    pn = []
    while True:
        pn.append(nn%10)
        nn = nn//10
        if nn == 0:
            break
    return sum(pn)+n

parm = 10000

arr = [0 for i in range(parm+1)]

for i in range(1,parm+1):
#    print(i)
    if arr[i] == 1:
        continue
    ind = d(i)
    while ind <= parm:
        arr[ind] = 1
#        print(ind)
        ind = d(ind)

#print(arr)
for i in range(1,parm+1):
    if arr[i] == 0:
        print(i)