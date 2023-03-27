def solution(absolutes, signs):
    sum_nums = 0
    for i in range(len(absolutes)):
        if signs[i]:
            sum_nums += absolutes[i]
        else:
            sum_nums -= absolutes[i]
    
    return sum_nums