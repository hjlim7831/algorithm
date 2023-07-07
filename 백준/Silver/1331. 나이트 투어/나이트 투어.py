import sys
input = sys.stdin.readline

traverse = []
for _ in range(36):
    traverse.append(input().rstrip())
traverse.append(traverse[0])

visited = set([traverse[0]])
valid_flag = True

for i in range(1, 37):
    p1, p2 = traverse[i-1], traverse[i]

    if i != 36:
        if p2 in visited:
            valid_flag = False
            break
        visited.add(p2)
    
    d1 = ord(p1[0]) - ord(p2[0])
    d2 = int(p1[1]) - int(p2[1])

    if abs(d1 * d2) == 2:
        continue
    
    valid_flag = False
    break

if valid_flag:
    print("Valid")
else:
    print("Invalid")