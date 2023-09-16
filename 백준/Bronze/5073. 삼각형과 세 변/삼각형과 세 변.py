import sys
input = sys.stdin.readline
while True:
    lines = list(map(int, input().split()))
    if sum(lines) == 0:
        break
    lines.sort()
    a, b, c = lines
    if a + b <= c:
        print("Invalid")
        continue
    if a == b == c:
        print("Equilateral")
        continue
    if a == b or b == c or c == a:
        print("Isosceles")
        continue
    print("Scalene")
        
