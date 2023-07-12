dictionary = []
def solution(word):
    for l in range(1, 6):
        make_word("", 0, l)
    
    dictionary.sort()
    return dictionary.index(word) + 1

def make_word(word:str, d:int, l:int):
    global dictionary
    if d == l:
        dictionary.append(word)
        return
    for a in ["A", "E", "I", "O", "U"]:
        make_word(word+a, d+1, l)
        
    