def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x

def solution(w, h):
    gcd_n = gcd(w, h)
    sw, sh = w // gcd_n, h // gcd_n
    not_usable = (sw + sh - 1) * gcd_n
    
    return w * h - not_usable
