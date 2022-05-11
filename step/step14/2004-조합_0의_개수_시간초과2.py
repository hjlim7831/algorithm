import sys

def count0(num):
    num0 = 0
    for i in range(1,num+1):
        while True:
            if i%5 == 0:
                i = i//5
                num0 += 1
            else:
                break
    return num0

n, m = map(int,sys.stdin.readline().split())

ans = count0(n) - count0(m) - count0(n-m)
print(ans)

# 접근을 비스무리하게 하려고는 했지만,
# 모범답안으로 테스트해 보니
# 5의 배수만 따지는 것은 문제가 있는 것 같다.
# 아무래도 나누는 과정이 두 번이나 있으니까..
# 그 쪽에서 5만 따지는 것은 문제가 생길 것 같다.