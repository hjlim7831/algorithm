cnt = 0
def dfs(d, numbers, tot, target, res_sum):
    # print(d, tot, res_sum)
    global cnt
    if d == len(numbers):
        # print(tot)
        if tot == target:
            cnt += 1
        return
    if tot - res_sum > target:
        return
    if tot + res_sum < target:
        return
    res_sum -= numbers[d]
    dfs(d+1, numbers, tot + numbers[d], target, res_sum)
    dfs(d+1, numbers, tot - numbers[d], target, res_sum)
    

def solution(numbers, target):
    dfs(0, numbers, 0, target, sum(numbers))
    
    return cnt