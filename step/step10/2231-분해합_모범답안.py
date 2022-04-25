N = int(input())

for i in range(1,N+1):
    num = sum(map(int,str(i)))
    num_sum = i + num
    if num_sum == N:
        print(i)
        break
    if i == N:
        print(0)

"""
브루트 포스 부분은 정말 그냥 처음부터 끝까지 싸그리 고민하는 방식으로 문제를 푸는 게 정답인가보다.. 더 효율적인 방법을 찾으려고 하지 않는 느낌
"""