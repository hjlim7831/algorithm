import sys
input = sys.stdin.readline

N, r, c = map(int, input().rstrip().split())

cnt = 0
while N != 0:
    # print(N)
    siz = 2**(N-1)
    r_det, c_det = r // siz, c // siz
    # print(r_det, c_det)
    cnt += (r_det * 2 + c_det) * siz**2
    # print("cnt:",cnt)
    N -= 1
    r, c = r % siz, c % siz
    # print(r, c)

print(cnt)