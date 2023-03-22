from math import sqrt

def solution(number, limit, power):
    weight = 0
    nums = set()
    for my_num in range(1, number + 1):
        nsq = int(sqrt(my_num))
        nums = set()
        for chk in range(1, nsq + 1):
            if my_num % chk == 0:
                nums.add(chk)
                nums.add(my_num // chk)
        tmp_weight = len(nums)
        if tmp_weight > limit:
            weight += power
        else:
            weight += tmp_weight
    
    
        
    
    
    return weight