import sys
n = int(sys.stdin.readline())
cnt = n

# 반복문을 통해 단어를 확인
for _ in range(n):
    word = list(map(str, sys.stdin.readline().strip()))
    
    # 반복문을 통해 현재 문자와 다음 문자를 비교
    for i in range(len(word) - 1):
        
        # 현재 문자와 다음 문자가 같으면 패스
        if word[i] == word[i + 1]:
            pass
        # 현재 문자가 다음 문자중에 있으면 그룹 단어가 될 수 없다.
        elif word[i] in word[i + 1:]:
            cnt -= 1
            break

print(cnt)