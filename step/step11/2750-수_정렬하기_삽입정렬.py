N = int(input())
numl = [0 for i in range(N)]
for i in range(N):
    numl[i] = int(input())

snuml = []
snuml.append(numl[0])
for i in range(0,N-1):
    j = i
    while True:
        # print(j,snuml[j],numl[i+1])
        if j == -1 or snuml[j] < numl[i+1]:
            snuml.insert(j+1,numl[i+1])
            # print("j",j)
            # print(snuml)
            break
        else:
            j -=1 


print("\n".join(map(str,snuml)))
