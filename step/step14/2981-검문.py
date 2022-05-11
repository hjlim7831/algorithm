def gcd(a,b):
    while b>0:
        a,b = b,a%b
    return a

N = int(input())
num = [0 for _ in range(N)]
for i in range(N):
    num[i] = int(input())

num.sort()
num_diff = [0 for _ in range(N-1)]
for i in range(N-1):
    num_diff[i] = num[i+1] - num[i]

num_gcd = num_diff[i]
for i in range(1,N-1):
    num_gcd = gcd(num_diff[i],num_gcd)

ans = [num_gcd]

for i in range(2,int(num_gcd**0.5)+1):
    if num_gcd % i == 0:
        ans.append(i)
        ans.append(num_gcd//i)

ans = list(set(ans))
ans.sort()
print(*ans)

"""
답안 참고해서 직접 써본 코드. # 다시풀기
"""