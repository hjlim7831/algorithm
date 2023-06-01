def solution(k, ranges):
    nums = [k]
    n = k
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        nums.append(n)
    acc = [k]
    for n in nums[1:]:
        acc.append(acc[-1] + n)
    
    len_nums = len(nums)
    answer = []
    # print(nums)
    # print(acc)
    
    for ran in ranges:
        integ = 0
        ln, rn = ran[0], ran[1]
        
        if ln > len_nums - 1 + rn:
            answer.append(-1)
            continue
        if ln == len_nums - 1 + rn:
            answer.append(0)
            continue
        
        integ += (nums[ln] + nums[rn-1]) / 2
        # print(ln+1, len_nums -1+rn-1)

        if ln + 1 <= len_nums - 1 + rn - 1:
            integ += acc[rn - 2] - acc[ln]
        answer.append(integ)
    return answer