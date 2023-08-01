def solution(numbers):
    answer = []
    for number in numbers:
        num = bin(number)[2::]
        ln, d = len(num), 0
        while 2**d -1 < ln:
            d += 1
        num = num.zfill(2**d - 1)
        # print(num, d)
        ln = len(num)
        stack = [(ln//2, d)]
        flag = 1
        while stack:
            idx, dx = stack.pop()
            if dx == 1:
                continue
            r = 2**(dx-1)-1
            if num[idx] == "0":
                target = num[idx-r:idx+r+1]
                if len(target) != target.count("0"):
                    flag = 0
                    break
            else:
                nex = 2**(dx-2)
                stack.append((idx-nex, dx-1))
                stack.append((idx+nex, dx-1))
        answer.append(flag)
        
        
    return answer