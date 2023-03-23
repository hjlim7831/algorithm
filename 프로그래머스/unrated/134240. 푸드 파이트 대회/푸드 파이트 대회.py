def solution(food):
    answer = '0'
    for i in range(len(food) - 1, 0, -1):
        num = food[i] // 2
        answer = num * str(i) + answer + num * str(i)
    
    return answer