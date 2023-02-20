import sys
input = sys.stdin.readline

number = input().rstrip()

tot_time = 0
for w in number:
    n = ord(w) - ord("A")
    if 0 <= n <= 2: # ABC
        tot_time += 3
    elif 3 <= n <= 5: # DEF
        tot_time += 4
    elif 6 <= n <= 8: # GHI
        tot_time += 5
    elif 9 <= n <= 11: # JKL
        tot_time += 6
    elif 12 <= n <= 14: # MNO
        tot_time += 7
    elif 15 <= n <= 18: # PQRS
        tot_time += 8
    elif 19 <= n <= 21: # TUV
        tot_time += 9
    else: # WXYZ
        tot_time += 10

print(tot_time)