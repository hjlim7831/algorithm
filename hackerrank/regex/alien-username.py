# Enter your code here. Read input from STDIN. Print output to STDOUT
import re, sys
input = sys.stdin.readline

match = r"[_\.]\d+[a-zA-Z]*_?"

n = int(input())
for _ in range(n):
    string = input().rstrip()
    # if re.search(match, string):
    if re.fullmatch(match, string):
            print("VALID")
    else:
        print("INVALID")