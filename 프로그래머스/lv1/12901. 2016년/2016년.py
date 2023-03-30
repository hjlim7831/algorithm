def solution(a, b):
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    weekdays = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    idx = 4
    for n in range(a-1):
        idx += days[n]
    idx += b
    print(idx)
    answer = weekdays[idx % 7]
    return answer