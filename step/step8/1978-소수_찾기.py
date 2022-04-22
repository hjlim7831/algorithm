N = int(input())
inte = list(map(int,input().split()))

nn = 1000
prime = [i for i in range(2,nn+1)]
i = 0
k = 2
while i <= nn-2:
    if prime[i] == -1:
        i += 1
        continue
    while True:
        if prime[i]*k > nn:
            i += 1
            k = 2
            break
        prime[prime[i]*k-2] = -1
        k += 1

result = [i for i in inte if i in prime and i != -1]
print(len(result))