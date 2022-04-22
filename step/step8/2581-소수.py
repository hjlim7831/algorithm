M = int(input())
N = int(input())

nn = 10000
prime = [i for i in range(nn+1)]
prime[0:2] = [-1,-1]

k = 2
i = 0
while i<nn:
    if prime[i] == -1:
        i += 1
        continue
    while True:
        if prime[i]*k > nn:
            k = 2
            i += 1
            break
        prime[prime[i]*k] = -1
        k += 1

pr = [i for i in prime if i != -1]
aa = [i for i in range(M, N+1)]
result = [i for i in aa if i in pr]

# print(pr)

if result:
    print(sum(result))
    print(min(result))
else:
    print(-1)