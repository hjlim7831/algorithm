M, N = map(int, input().split())

prime = [i for i in range(N+1)]
prime[:2] = [-1, -1]
n = 2
k = 0

while k<=N**0.5:
    if prime[k] == -1:
        k += 1
        continue
    while True:
        if prime[k] * n > N:
            k += 1
            n = 2
            break
        prime[prime[k] * n] = -1
        n += 1

pr = [i for i in prime if i != -1 and i >= M]
for i in pr:
    print(i)