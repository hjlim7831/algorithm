import re

def solution(new_id):
    # 1
    rec_id = new_id.lower()
    # 2
    rec_id = re.sub("[^a-zA-Z0-9-_.]", "", rec_id)
    rec_id = re.sub("\^", "", rec_id)
    # 3
    rec_id = re.sub("\.*\.", ".", rec_id)
    # 4
    rec_id = re.sub("(^\.|\.$)", "", rec_id)
    # 5
    if not rec_id:
        rec_id = "a"
    # 6
    if len(rec_id) >= 16:
        rec_id = rec_id[:15]
    rec_id = re.sub("\.$", "", rec_id)
    # 7
    if len(rec_id) <= 2:
        while len(rec_id) != 3:
            rec_id += rec_id[-1]
    
    return rec_id