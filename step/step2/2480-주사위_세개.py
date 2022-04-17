dice = list(map(int, input().split()))
dice.sort()
A, B, C = dice[0], dice[1], dice[2]

if A == C:
    print(10000 + A*1000)
elif A == B:
    print(1000 + A*100)
elif B == C:
    print(1000 + B*100)
else:
    print(C*100)