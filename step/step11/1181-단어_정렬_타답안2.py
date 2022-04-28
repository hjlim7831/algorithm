# 앞의 문제들에서 썼던 방법을 이어서 쓴다면, 이게 제일 정석적인 방식일 듯

n = int(input())

word = []
for i in range(n):
    word.append(input())

set_word = list(set(word))

sort_word = []
for i in set_word:
    sort_word.append((len(i),i))

result = sorted(sort_word)

for len_word, word in result:
    print(word)