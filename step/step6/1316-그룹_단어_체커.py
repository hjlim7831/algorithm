N = int(input())
w = 0
for i in range(N):
    string = input()
    nn = 0
    for j in range(len(string)-1):
        if string[j] == string[j+1]:
            continue
        else:
            string = string.replace(string[j],chr(nn+65))
            nn += 1
            # 숫자는 10부터는 하나로 취급되기 어렵지..
            if j == len(string)-2:
                string = string.replace(string[j+1],chr(nn+65))
    if string == ''.join(sorted(string)):
        w += 1
print(w)

"""
처음엔 chr 대신 숫자를 넣었는데, 생각해보니 문자가 10개 이상이 되면 문자당 두자리씩 할당이 된다.. 예제로는 이걸 확인할 수 없었다는 것이 조금 아쉬웠다.

chr에는 숫자가 제한되어있다.. 무작정 j를 index로 넣으면 값이 아무것도 나오지 않을 수 있다. + sort가 불가능해진다.
-> 이걸로 인해 if문이 조금 더 복잡해졌다.

replace 함수는 개수 제한을 해주지 않는다면 한 번에 모든 문자를 원하는 문자로 바꿔버린다!
"""
