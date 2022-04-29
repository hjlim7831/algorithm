while True:
    N = input()
    if N == '0':
        break
    Nr = N[::-1]
    if N == Nr:
        print("yes")
    else:
        print("no")