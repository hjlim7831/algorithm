def solution(X, Y):
    mate = ''
    count_x = { str(n): 0 for n in range(10) }
    count_y = { str(n): 0 for n in range(10) }
    for n in X:
        count_x[n] += 1
    for n in Y:
        count_y[n] += 1
        
    for n in range(9, -1, -1):
        str_n = str(n)
        cnt = min(count_x[str_n], count_y[str_n])
        mate += str_n * cnt

    if mate == "":
        mate = "-1"
    
    if len(mate) == mate.count("0"):
        mate = "0"
    
    return mate