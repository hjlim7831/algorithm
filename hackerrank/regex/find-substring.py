# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import sys
input = sys.stdin.readline

n = int(input()) # number of sentences
words = []
for _ in range(n):
    sentence = input().rstrip()
    word = ""
    for s in sentence:
        if re.match(r"[\w_]", s):
            word += s
        else:
            words.append(word)
            word = ""
    if word:
        words.append(word)

q = int(input())
for _ in range(q):
    cnt = 0
    query = input().rstrip()
    matching = fr"[\w_]{query}[\w_]"
    # print(matching)
    for word in words:
        # print(word)
        if re.search(matching, word):
            cnt += 1
    print(cnt)
