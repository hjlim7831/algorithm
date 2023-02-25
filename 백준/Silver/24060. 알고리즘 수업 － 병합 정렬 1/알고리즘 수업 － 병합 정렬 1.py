import sys
input = sys.stdin.readline

N, K = map(int, input().split())
An = list(map(int, input().split()))

cnt = 0
ans = -1
def merge_sort(A:list, st:int, ed:int):
    if st < ed:
        mid = (st + ed) // 2
        merge_sort(A, st, mid)
        merge_sort(A, mid + 1, ed)
        merge(A, st, mid, ed)

def merge(A:list, st:int, mid:int, ed:int):
    global cnt, ans
    L = st; R = mid + 1; idx = 0
    tmp = [0 for _ in range(st, ed+1)]

    while L <= mid and R <= ed:
        if A[L] <= A[R]:
            tmp[idx] = A[L]
            idx += 1; L += 1
        else:
            tmp[idx] = A[R]
            idx += 1; R += 1
    
    while L <= mid:
        tmp[idx] = A[L]
        idx += 1; L += 1
    
    while R <= ed:
        tmp[idx] = A[R]
        idx += 1; R += 1
    
    for i in range(st, ed+1):
        A[i] = tmp[i - st]
        cnt += 1; idx += 1
        if (cnt == K):
            ans = tmp[i - st]

merge_sort(An, 0, len(An)-1)

print(ans)