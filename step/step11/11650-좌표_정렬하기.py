import sys
N = int(sys.stdin.readline())
dxy = {}

for i in range(N):
    x, y = map(int,sys.stdin.readline().split())
    try:
        dxy[x].append(y)
    except KeyError:
        dxy[x] = [y]

dkey = list(dxy.keys())
dkey.sort()

for i in dkey:
    sval = dxy[i]
    sval.sort()
    for j in sval:
        print(i, j)

"""
딕셔너리 사용법에 익숙치 않은 편인데, 좀 더 익숙해질 필요가 있어보인다. 꽤 괜찮은 방법일지도.. 
"""