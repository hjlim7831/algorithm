import sys
input = sys.stdin.readline

N = int(input())
An = list(map(int, input().split()))
plus, minus, times, divid = map(int, input().split())

max_ans = -1_000_000_000
min_ans = 1_000_000_000

def calculate(idx:int, res:int, plus:int, minus:int, times:int, divid:int):
    global max_ans, min_ans
    if idx == N:
        max_ans = max(res, max_ans)
        min_ans = min(res, min_ans)
        return
    
    if plus:
        calculate(idx+1, res + An[idx], plus-1, minus, times, divid)
    if minus:
        calculate(idx+1, res - An[idx], plus, minus-1, times, divid)
    if times:
        calculate(idx+1, res * An[idx], plus, minus, times-1, divid)
    if divid:
        if res:
            sign = res // abs(res)
            calculate(idx+1, abs(res) // An[idx] * sign, plus, minus, times, divid-1)
        else:
            calculate(idx+1, 0, plus, minus, times, divid-1)

calculate(1, An[0], plus, minus, times, divid)
print(max_ans)
print(min_ans)