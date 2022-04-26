N = int(input())
numl = [0 for i in range(N)]
for i in range(N):
    numl[i] = int(input())

i = 0
for j in range(i,N-1):
    k = N-2
    while k >= i:
        # print(numl[k], numl[k+1], k)
        if numl[k] < numl[k+1]:
            pass
        else:
            numl[k], numl[k+1] = numl[k+1], numl[k]
        k -= 1
    i += 1


print("\n".join(map(str,numl)))
