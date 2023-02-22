import sys
input = sys.stdin.readline

N = int(input())

offset = 4000
count_arr = [0 for _ in range(offset*2 + 1)]
nums_sum = 0
nums_max = -offset
nums_min = offset

sorted_arr = [0 for _ in range(N)]

for _ in range(N):
    num = int(input())
    count_arr[num+offset] += 1 # 2-1, 3-1. count 어레이 구하기
    nums_sum += num

    if nums_max < num: # 4-1. 최댓값 구하기
        nums_max = num
    if nums_min > num: # 4-2. 최솟값 구하기
        nums_min = num

nums_range = nums_max - nums_min # 4. 범위 구하기

nums_avg = round(nums_sum/N) # 1. 산술평균 구하기

freq_list = []
freq_max = -1
for i in range(offset*2 + 1):
    if freq_max < count_arr[i]:
        freq_list = []
        freq_list.append(i - offset)
        freq_max = count_arr[i]
    elif freq_max == count_arr[i]:
        freq_list.append(i - offset)

nums_freq = 0 # 3. 최빈값 구하기
if len(freq_list) == 1:
    nums_freq = freq_list[0]
else:
    nums_freq = freq_list[1]


idx = 0
for i in range(offset*2 + 1):
    for j in range(count_arr[i]):
        sorted_arr[idx] = i - offset
        idx += 1

nums_med = sorted_arr[N//2] # 2. 중앙값 구하기

print(nums_avg, nums_med, nums_freq, nums_range, sep="\n")