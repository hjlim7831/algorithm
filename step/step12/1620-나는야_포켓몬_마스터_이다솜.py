import sys

N, M = map(int,sys.stdin.readline().rstrip().split())
pocketmon_dict1 = {}
pocketmon_dict2 = {}
for i in range(1,N+1):
    ind = str(i)
    po_name = sys.stdin.readline().rstrip()
    pocketmon_dict1[ind] = po_name
    pocketmon_dict2[po_name] = ind

for j in range(M):
    det = sys.stdin.readline().rstrip()
    if det.isdigit():
        print(pocketmon_dict1[det])
    else:
        print(pocketmon_dict2[det])

# sys.stdin.readline() 을 애용하자..
# 그리고 문자열을 받을 때에는 rstrip()도 붙이는 것을 잊지 말자..