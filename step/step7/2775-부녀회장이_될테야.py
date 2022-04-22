
# nn: 호
# kk: 층
def ank(nn, kk):
    ap = [[0 for i in range(nn+1)] for j in range(kk+1)]
    ap[0] = [i for i in range(nn+1)]
    for j in range(1,kk+1):
        for i in range(1,nn+1):
            ap[j][i] = sum(ap[j-1][:i+1])

    return ap[kk][nn]

T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    print(ank(n,k))


# 문제를 제대로 읽자.. 너무 꼬아서 생각했다.