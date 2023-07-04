def solution(arrayA, arrayB):
    gcd_a, gcd_b = arrayA[0], arrayB[0]
    
    for i in range(1, len(arrayA)):
        gcd_a = euclidean(gcd_a, arrayA[i])
    
    for i in range(1, len(arrayB)):
        gcd_b = euclidean(gcd_b, arrayB[i])
        
    answer_a = 0
    answer_flag = True
    for num in arrayB:
        if num % gcd_a == 0:
            answer_flag = False
            break
    if answer_flag:
        answer_a = gcd_a
    
    answer_b = 0
    answer_flag = True
    for num in arrayA:
        if num % gcd_b == 0:
            answer_flag = False
            break
    if answer_flag:
        answer_b = gcd_b
    return max(answer_a, answer_b)

def euclidean(a, b):
    while b != 0:
        [a, b] = [b, a%b]
    return a