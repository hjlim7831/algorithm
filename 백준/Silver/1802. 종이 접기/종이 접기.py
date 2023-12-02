import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    info = input().rstrip()
    li = len(info)
    ans_flag = True
    while li >= 2:
        if not ans_flag:
            break
        # print(li)
        l_info = info[:li//2]
        r_info = info[li//2+1:][::-1]
        # print(f"l_info: {l_info}, r_info: {r_info}")
        for i in range(li // 2):
            if l_info[i] == r_info[i]:
                ans_flag = False
                break
        info = l_info
        li = len(info)
    
    if ans_flag:
        print("YES")
    else:
        print("NO")