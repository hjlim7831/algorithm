def solution(brown, yellow):
    tot = brown + yellow
    for h in range(3, int(tot**0.5) + 1):
        w = tot / h
        if int(w) == w and (w - 2) * (h - 2) == yellow:
            return [w, h]
    return [0, 0]