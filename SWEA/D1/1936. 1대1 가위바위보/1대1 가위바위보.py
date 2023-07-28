A, B = map(int, input().split())

table = {(1,2):"B", (2,1):"A", (1,3):"A",(3,1):"B", (2,3):"B",(3,2):"A"}

print(table[(A,B)])