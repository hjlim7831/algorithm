def solution(arr1, arr2):
    answer = []
    for a1, a2 in zip(arr1, arr2):
        tmp = []
        for b1, b2 in zip(a1, a2):
            tmp.append(b1 + b2)
        answer.append(tmp)
        
    return answer