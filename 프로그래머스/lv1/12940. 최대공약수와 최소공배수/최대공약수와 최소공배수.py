def solution(n, m):
    answer = []
    gcd_num = gcd(n, m)
    answer.append(gcd_num)
    answer.append(gcd_num * (n // gcd_num) * (m // gcd_num))
    return answer

def gcd(n, m):
    res = 1
    for i in range(min(n, m), 1, -1):
        if n % i == 0 and m % i == 0:
            res = i
            break
    return res
