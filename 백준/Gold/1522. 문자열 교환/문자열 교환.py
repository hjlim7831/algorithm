import sys
input = sys.stdin.readline

word = input().rstrip()
a_cnt = word.count("a")

word += word[0:a_cnt-1]

b_cnt = len(word)
for i in range(len(word) - (a_cnt - 1)):
    b_cnt = min(b_cnt, word[i:i+a_cnt].count("b"))
print(b_cnt)