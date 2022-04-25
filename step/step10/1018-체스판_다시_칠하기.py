N, M = map(int, input().split())
board = [["" for i in range(M)]for j in range(N)]
# print(board)
for i in range(N):
    inp = input().split()[0]
    # print("inp",inp)
    for j in range(M):
        # print(inp[j])
        board[i][j] = inp[j]
        # print(board)

#print(board)
mini = 64
for i in range(N-7):
    for j in range(M-7):
#        print(i,j)
        mbo = [["" for i in range(8)]for j in range(8)]
        for k in range(8):
            mbo[k] = board[i+k][j:j+8]
#        print(mbo)
        c1, c2 = 0, 0
        for ii in range(8):
            for jj in range(8):
                # print(ii,jj)
                # print(mbo[ii][jj], ii, jj)
                # print((ii+jj)%2)
                if (ii+jj)%2 == 0:
                    if mbo[ii][jj] == 'B':
                        c1 += 1
                    #    print("B c1",c1)
                    else:
                        c2 += 1
                else:
                    if mbo[ii][jj] == 'W':
                        c1 += 1
                        # print("W c1",c1)
                    else:
                        c2 += 1
#        print(c1, c2)
        mini = min(mini, c1, c2)

print(mini)
                    
