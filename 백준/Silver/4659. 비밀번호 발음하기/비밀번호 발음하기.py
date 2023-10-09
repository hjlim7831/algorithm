import sys
input = sys.stdin.readline

vowels = set(["a", "e", "i", "o", "u"])

while True:
    pwd = input().rstrip()
    acceptable = False
    if pwd == "end":
        break
    for w in vowels:
        if pwd.count(w) != 0:
            acceptable = True
            break
    cnt, last_type = 0, ""
    for w in pwd:
        if w in vowels:
            typ = "v"
        else:
            typ = "x"
        if last_type == typ:
            cnt += 1
            if cnt == 3:
                acceptable = False
                break
        else:
            cnt = 1
            last_type = typ
    
    cnt, last_word = 0, ""
    for w in pwd:
        if last_word == w:
            cnt += 1
        else:
            cnt = 1
            last_word = w
        if cnt == 2 and w not in ["e", "o"]:
            acceptable = False
            break
        
    if acceptable:
        print(f"<{pwd}> is acceptable.")
    else:
        print(f"<{pwd}> is not acceptable.")