def solution(s):
    print(s.isdigit())
    return (len(s) == 4 or len(s) == 6) and s.isdigit()