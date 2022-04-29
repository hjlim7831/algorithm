input = int(input())
square = 2
while True:
    if (input == 1 or input == 2):
        print(input)
        break
    square *= 2
    if (square >= input):
        print((input - (square // 2)) * 2)
        break

# 아예 결과값을 규칙성을 찾아내신 분도 계신다.. 이렇게도 풀 수 있구만