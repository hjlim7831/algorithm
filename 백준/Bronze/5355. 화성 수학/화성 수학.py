import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    op = input().rstrip().split()
    ans = float(op[0])
    for o in op[1:]:
        if o == "@":
            ans *= 3
        elif o == "%":
            ans += 5
        elif o == "#":
            ans -= 7
    print(f"{ans:.2f}")