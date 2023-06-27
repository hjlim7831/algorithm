def solution(n):
    cnt = 1
    for b in range(1, 2*n):
        if (2 * n) % (b + 1) == 0:
            div = (2 * n) // (b + 1)
            if div == 0:
                break
            a = (div - b) / 2
            if a <= 0:
                break
            if int(a) == a:
                cnt += 1
                # print(a, b)
    return cnt