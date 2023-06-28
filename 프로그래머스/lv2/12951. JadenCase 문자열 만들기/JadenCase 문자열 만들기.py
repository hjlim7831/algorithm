def solution(s):
    new_s = ""
    first_word = True
    for token in s.lower():
        if token != " ":
            if first_word:
                first_word = False
                if not token.isdigit():
                    token = token.upper()
        else:
            first_word = True
        new_s += token

    return new_s
    
    
    