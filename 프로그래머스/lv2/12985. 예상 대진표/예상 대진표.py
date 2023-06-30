def solution(n,a,b):
    r = 0
    while n != 1:
        r += 1
        n //= 2
    
    bin_a, bin_b = bin(a-1)[2:].zfill(r), bin(b-1)[2:].zfill(r)
    
    for i in range(r):
        if bin_a[i] != bin_b[i]:
            return r - i