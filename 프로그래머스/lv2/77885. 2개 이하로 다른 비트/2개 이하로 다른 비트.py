def solution(numbers):
    answer = []
    for num in numbers:
        s_num = bin(num)[2::][::-1]
        ls = len(s_num)
        idx = ls
        for i, s in enumerate(s_num):
            if s == "0":
                idx = i
                break
        # print("idx:",idx)
        target = num + 1
        if idx >= 2:
            target += 2**(idx - 1) - 1
        answer.append(target)
        
    return answer