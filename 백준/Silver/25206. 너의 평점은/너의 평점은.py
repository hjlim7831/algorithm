import sys
input = sys.stdin.readline

grade_dict = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0.0}

grade_sum = 0
num_sum = 0

for _ in range(20):
    subject_name, num, grade = input().rstrip().split()
    num = float(num)
    if grade == "P": # P일 땐, 평점 계산에 들어가지 않음
        continue
    grade_sum += grade_dict[grade] * num
    num_sum += num

print(grade_sum / num_sum)