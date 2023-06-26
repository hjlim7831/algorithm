def solution(n):
    num = bin(n)
    cnt = num.count("1")
    while True:
        n += 1
        if cnt == bin(n).count("1"):
            break
    return n