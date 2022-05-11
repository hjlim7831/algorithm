def fact(n):
    if n == 0:
        return 1
    else:
        res = 1
        for i in range(1,n+1):
            res *= i
        return res


N, K = map(int,input().split())
ans = (fact(N)//(fact(N-K)*fact(K)))%10007

print(ans)

