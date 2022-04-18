S = input()
for i in range(26):
    alp = chr(i+97)
    try:
        ind = S.index(alp)
    except ValueError:
        ind = -1
    print(ind,end=" ")