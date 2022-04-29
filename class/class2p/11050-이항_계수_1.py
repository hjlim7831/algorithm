def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

N, K = map(int,input().split())

ans = fact(N)//(fact(K)*fact(N-K))
print(ans)