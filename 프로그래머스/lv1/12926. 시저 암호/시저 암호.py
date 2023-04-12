def solution(s, n):
    answer = ''
    for comp in s:
        if comp == " ":
            answer += comp
        else:
            num = ord(comp)
            if ord("A") <= num <= ord("Z"):
                d = (num - ord("A") + n) % 26
                answer += chr(d + ord("A"))
            else:
                d = (num - ord("a") + n) % 26
                answer += chr(d + ord("a"))
            
    
    
    return answer