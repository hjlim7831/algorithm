melon = int(input())
arr = [list(map(int,input().split())) for _ in range(6)]

w = 0; w_idx = 0 #가장 긴 가로변 길이, 인덱스 초기화
h = 0; h_idx = 0 #가장 긴 세로변 길이, 인덱스 초기화

for i in range(len(arr)):
    if arr[i][0] == 1 or arr[i][0] == 2:
        if w < arr[i][1]:
            w = arr[i][1]
            w_idx = i
    elif arr[i][0] == 3 or arr[i][0] == 4:
        if h < arr[i][1]:
            h = arr[i][1]
            h_idx = i

# 가장 긴 가로변 양옆에 붙어있는 변(세로변)들의 차이: 뺄 사각형의 세로
# 가장 긴 세로변 양옆에 붙어있는 변(가로변)들의 차이: 뺄 사각형의 가로
subW = abs(arr[(w_idx-1)%6][1] - arr[(w_idx+1)%6][1])
subH = abs(arr[(h_idx-1)%6][1] - arr[(h_idx+1)%6][1])

ans = (w*h-subW*subH)*melon
print(ans)