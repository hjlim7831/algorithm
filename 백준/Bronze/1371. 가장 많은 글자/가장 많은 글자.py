import sys
from collections import defaultdict

alp_dict = defaultdict(int)

lines = sys.stdin.readlines()
for line in lines:
    for alp in line:
        if alp != " ":
            alp_dict[alp] += 1

ans = ""
cnt = 0
for i in range(26):
    target = chr(i + ord("a"))
    if cnt < alp_dict[target]:
        cnt = alp_dict[target]
        ans = ""
        ans += target
    elif cnt == alp_dict[target]:
        ans += target

print(ans)