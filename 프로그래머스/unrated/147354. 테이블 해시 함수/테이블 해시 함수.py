def solution(data, col, row_begin, row_end):
    # 2. col 번째 컬럼 값을 기준으로 오름차순 정렬.
    # 값이 동일하면 첫 번째 컬럼의 값을 기준으로 내림차순 정렬.
    data.sort(key=lambda x:(x[col-1], -x[0]))
    
    # 3. S_i 구하기
    Si = []
    for i in range(row_begin-1, row_end):
        S_tmp = 0
        for j in range(len(data[0])):
            S_tmp += data[i][j] % (i + 1)
        Si.append(S_tmp)
    answer = Si[0]
    
    #  bitwise XOR
    for num in Si[1:]:
        answer ^= num
    
    return answer