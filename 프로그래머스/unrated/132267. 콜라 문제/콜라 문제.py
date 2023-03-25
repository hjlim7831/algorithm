def solution(a, b, n):
    # a 개를 가져가면 b개를 줌
    # n 개를 가져갔을 때 얼마만큼 줄까?
    cnt = 0
    rest = n
    while rest >= a:
        div = rest // a
        cnt += div * b
        rest = rest % a + div * b

    return cnt