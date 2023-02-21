import sys
input = sys.stdin.readline

word_dict = {"c=":0, "c-":1, "dz=":2, "d-":3, "lj":4, "nj":5, "s=":6, "z=":7}

word = input().rstrip()

for k in word_dict.keys():
    word = word.replace(k, str(word_dict[k]))

# print(word)
print(len(word))