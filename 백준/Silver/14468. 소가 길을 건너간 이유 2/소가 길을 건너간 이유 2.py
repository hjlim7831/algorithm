
route = input()

pos = [[] for _ in range(26)]

for idx, alp in enumerate(route):
    pos[ord(alp) - ord("A")].append(idx)

cnt = 0
for a1 in range(26):
    for a2 in range(a1+1, 26):
        alp1 = pos[a1]
        alp2 = pos[a2]
        if alp1[0] < alp2[0] < alp1[1] < alp2[1]:
            cnt += 1
        elif alp2[0] < alp1[0] < alp2[1] < alp1[1]:
            cnt += 1

print(cnt)