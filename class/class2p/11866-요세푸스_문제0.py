N, K = map(int,input().split())

mem = [i for i in range(1,N+1)]
perm = [0 for i in range(1,N+1)]
i = 0
ip = 0

N1 = N
while len(mem) > 0:
    i = (i + K-1)%N1
    perm[ip] = mem[i]
    del mem[i]
    N1 -= 1
    ip += 1

print("<", end="")

for i in range(N-1):
    print(perm[i], end=", ")

print(f"{perm[N-1]}>",end="")

# 의외로 알고리즘 부분보단 [] 대신 <> 안에 넣는 것에서 헤맸다..ㅋㅋ