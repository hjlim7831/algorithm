# min, abs 내에 key로 lambda 사용하는 법 익히기

prime = [i for i in range(10000+1)]
prime[:2] = [-1,-1]
n = 2
k = 0
while k <= 100:
    if prime[k] == -1:
        k += 1
        continue
    while True:
        if prime[k] * n > 10000:
            n = 2
            k += 1
            break
        prime[prime[k] * n] = -1
        n += 1

pr = [i for i in prime if i != -1]

def findNearNum(val):
    global pr
    return min(pr, key=lambda x:abs(x-val))

T = int(input())
for i in range(T):
    n = int(input())
    m = n//2
    ind = pr.index(findNearNum(m))
    while True:
        if  n - pr[ind] in pr:
            print(min(pr[ind], n - pr[ind]), max(pr[ind], n - pr[ind]))
            break
        ind += 1
