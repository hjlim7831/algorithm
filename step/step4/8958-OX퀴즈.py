T = int(input())
for i in range(T):
    ox_input = input()
    score = 0
    n = 1
    for ox in ox_input:
        if ox == 'O':
            score += n
            n += 1
        else:
            n = 1
    print(score)