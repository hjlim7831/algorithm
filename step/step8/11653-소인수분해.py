N = int(input())

if N ==1:
    pass
else:
    prime = [i for i in range(N+1)]
    prime[:2] = [-1,-1]

    k = 0
    n = 2
    nn = 0
    while k<=N**0.5:
        if prime[k] == -1:
            k += 1
            nn += 1
            continue
        while True:
            if prime[k]*n >N:
                k += 1
                n = 2
                nn += 1
                break
            prime[prime[k]*n] = -1
            nn += 1
            n += 1
# 시간을 줄인다면 위에서 줄여야 한다..
    print(nn)
    pr = [i for i in prime if i != -1]
    #print(pr)
    k = 0
    while True:
        if N in prime:
            print(N)
            nn += 1
            break
        if N%pr[k] == 0:
            print(pr[k])
            N = N//pr[k]
            k = 0
            nn += 1
        else:
            k += 1
            nn += 1
    print(nn)