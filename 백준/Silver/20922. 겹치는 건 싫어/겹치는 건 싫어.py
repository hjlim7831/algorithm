import sys
input = sys.stdin.readline

N, K = map(int, input().split())
An = list(map(int, input().split()))
count = [0] * 100_001
st, ed = 0, 1
count[An[0]] = 1

ans = 0
while ed < N:
    st_val, ed_val = An[st], An[ed]    
    if count[ed_val] < K:
        count[ed_val] += 1
        ed += 1
        ans = max(ans, ed - st)
    else:
        count[st_val] -= 1
        st += 1

print(ans)
        