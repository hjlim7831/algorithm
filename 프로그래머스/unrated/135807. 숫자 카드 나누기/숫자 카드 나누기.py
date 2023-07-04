def solution(arrayA, arrayB):
    gcd_a, gcd_b = arrayA[0], arrayB[0]
    
    for i in range(1, len(arrayA)):
        gcd_a = euclidean(gcd_a, arrayA[i])
    
    for i in range(1, len(arrayB)):
        gcd_b = euclidean(gcd_b, arrayB[i])
    
    a_nums, b_nums = set(), set()
    for i in range(1, int(gcd_a**0.5) + 1):
        if gcd_a % i == 0:
            a_nums.add(i)
            a_nums.add(gcd_a // i)
    
    for i in range(1, int(gcd_b**0.5 + 1)):
        if gcd_b % i == 0:
            b_nums.add(i)
            b_nums.add(gcd_b // i)
    a_nums, b_nums = list(a_nums), list(b_nums)
    a_nums.sort(reverse=True)
    b_nums.sort(reverse=True)
    
    answer_a = 0
    for div in a_nums:
        if div == 1:
            break
        answer_flag = True
        for num in arrayB:
            if num % div == 0:
                answer_flag = False
                break
        if answer_flag:
            answer_a = div
            break
    
    answer_b = 0
    for div in b_nums:
        if div == 1:
            break
        answer_flag = True
        for num in arrayA:
            if num % div == 0:
                answer_flag = False
                break
        if answer_flag:
            answer_b = div
            break
    return max(answer_a, answer_b)

def euclidean(a, b):
    while b != 0:
        [a, b] = [b, a%b]
    return a