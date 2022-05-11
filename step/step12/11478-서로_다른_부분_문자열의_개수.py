S = input()

ls = len(S)
rset = set()
for i in range(ls):
    for j in range(i,ls):
        rset.add(S[i:j+1])

print(len(rset))