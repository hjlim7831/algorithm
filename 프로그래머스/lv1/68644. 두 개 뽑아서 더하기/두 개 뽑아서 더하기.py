from itertools import combinations

def solution(numbers):
    sum_nums = set()
    for i, j in combinations(numbers, 2):
        sum_nums.add(i+j)
    answer = list(sum_nums)
    answer.sort()
    return answer