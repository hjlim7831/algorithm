def solution(n):
    num3 = ""
    while n:
        num3 += str(n % 3)
        n //= 3
        
    num10 = 0
    for i in num3:
        num10 *= 3
        num10 += int(i)
    
    return num10