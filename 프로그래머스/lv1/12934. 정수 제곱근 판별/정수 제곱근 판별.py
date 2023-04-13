def solution(n):
    n_sqrt = int(n**0.5)
    if n_sqrt * n_sqrt == n:
        return (n_sqrt + 1)**2
    else:
        return -1