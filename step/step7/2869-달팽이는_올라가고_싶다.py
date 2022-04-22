A, B, V = map(int, input().split())

det = (V-A)/(A-B)

# V <= (A-B) * x + A
if int(det) == det:
    print(int(det)+1)
else:
    print(int(det)+2)

# 단순히 while문을 써버리면 시간 초과가 됨..
# -> 더 직접적으로 계산해서 생각해봐야 하는 문제