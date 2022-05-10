N, M = map(int,input().split())
pocketmon_dict1 = {}
pocketmon_dict2 = {}
for i in range(1,N+1):
    ind = str(i)
    po_name = input()
    pocketmon_dict1[ind] = po_name
    pocketmon_dict2[po_name] = ind

for j in range(M):
    det = input()
    if det.isdigit():
        print(pocketmon_dict1[det])
    else:
        print(pocketmon_dict2[det])
