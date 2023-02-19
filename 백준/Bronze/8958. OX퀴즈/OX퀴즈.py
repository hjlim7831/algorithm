import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    score = 0
    ox_quiz = input().rstrip()
    acc = 0
    for quiz in ox_quiz:
        if quiz == "O":
            acc += 1
        else:
            acc = 0
        score += acc
    
    print(score)