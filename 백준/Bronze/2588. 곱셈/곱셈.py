import sys
input = sys.stdin.readline

num1 = int(input())
num2 = input()

ans1 = num1 * int(num2[2])
ans2 = num1 * int(num2[1])
ans3 = num1 * int(num2[0])
ans4 = num1 * int(num2)

print(ans1)
print(ans2)
print(ans3)
print(ans4)