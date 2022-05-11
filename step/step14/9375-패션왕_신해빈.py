T = int(input())
for i in range(T):
    n = int(input())
    c_dict = {}
    for j in range(n):
        c_name, c_type = input().split()
        try:
            c_dict[c_type] += [c_name]
        except KeyError:
            c_dict[c_type] = [c_name]
    c_values = list(c_dict.values())
    ans1 = 1
    for i in range(len(c_values)):
        l = len(c_values[i])
        ans1 *= (l+1)
    ans1 -= 1
    print(ans1)
    