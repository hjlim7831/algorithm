N = int(input())
word = [""]*N
for i in range(N):
    word[i] = input()
word.sort()
sword = sorted(word,key=lambda x:len(x))
#print(sword) # 중복 제거하기
s = ""
for i in sword:
    if s != i:
        print(i)
    s = i
