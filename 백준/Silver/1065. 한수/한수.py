import sys
input = sys.stdin.readline

N = int(input())

def is_han_num(num: int):
    target = str(num)
    num_len = len(target)
    if num_len <= 2:
        return True
    else:
        d = int(target[1]) - int(target[0])
        for idx in range(2, num_len):
            next_d = int(target[idx]) - int(target[idx-1])
            if d != next_d:
                return False
        return True

cnt = 0
for num in range(1, N + 1):
    if (is_han_num(num)):
        cnt += 1
print(cnt)