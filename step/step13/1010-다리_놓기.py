def fact(n):
    if n == 0:
        return 1
    else:
        ans = 1
        for i in range(1,n+1):
            ans *= i
        return ans

T = int(input())
for i in range(T):
    N, M = map(int,input().split())
    ans = fact(M)//(fact(N)*fact(M-N))
    print(ans)