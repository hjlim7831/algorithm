def solution(book_time):
    commands = []
    for book in book_time:
        st_hr, st_min = map(int, book[0].split(":"))
        st_tim = st_hr * 60 + st_min
        
        ed_hr, ed_min = map(int, book[1].split(":"))
        ed_tim = ed_hr * 60 + ed_min + 10
        
        commands.append((st_tim, 0))
        commands.append((ed_tim, 1))
        
    commands.sort(key=lambda x: (x[0], -x[1]))
    max_len = 0
    length = 0
    for tim, typ in commands:
        if typ == 0:
            length += 1
        else:
            max_len = max(max_len, length)
            length -= 1
        
    return max_len