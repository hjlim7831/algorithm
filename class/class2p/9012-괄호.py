T = int(input())
for i in range(T):
    ps = input()
    while True:
        ps_dump = ps
        ps = ps.replace("()","")
        if ps == "":
            # print(ps)
            print("YES")
            break
        elif ps_dump == ps:
            # print(ps)
            print("NO")
            break
