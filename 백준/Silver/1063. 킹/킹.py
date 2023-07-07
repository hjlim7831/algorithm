import sys
input = sys.stdin.readline

king, stone, N = input().rstrip().split()
N = int(N)

def str_to_pos(p:str):
    c = ord(p[0]) - ord("A")
    r = 8 - int(p[1])
    return r, c

def pos_to_str(pos:tuple):
    r, c = pos
    p = chr(c + ord("A")) + str(8 - r)
    return p

k_pos, s_pos = str_to_pos(king), str_to_pos(stone)

direct = {"R":(0, 1), "L":(0, -1), "B":(1, 0), "T":(-1, 0), "RT":(-1, 1), "LT":(-1, -1), "RB":(1, 1), "LB":(1, -1)}

for _ in range(N):
    comm = input().rstrip()
    dr, dc = direct[comm]
    k_next = k_pos[0] + dr, k_pos[1] + dc

    if k_next[0] < 0 or k_next[0] >= 8 or k_next[1] < 0 or k_next[1] >= 8:
        continue
    
    if k_next == s_pos:
        s_next = s_pos[0] + dr, s_pos[1] + dc
        if s_next[0] < 0 or s_next[0] >= 8 or s_next[1] < 0 or s_next[1] >= 8:
            continue
        s_pos = s_next

    k_pos = k_next

print(pos_to_str(k_pos))
print(pos_to_str(s_pos))


