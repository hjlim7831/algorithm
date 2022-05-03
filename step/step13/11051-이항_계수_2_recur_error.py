def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

N, K = map(int,input().split())
ans = (fact(N)//(fact(N-K)*fact(K)))%10007

print(ans)

# 백준의 recursionlimit은 1000 까지! 