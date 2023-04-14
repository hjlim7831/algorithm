def solution(n, arr1, arr2):
    answer = [arr1[i] | arr2[i] for i in range(len(arr1))]
    answer = list(map(lambda x: format(x, f'0{n}b'), answer))
    
    answer = [ans.replace("0", " ").replace("1", "#") for ans in answer]
    
    return answer