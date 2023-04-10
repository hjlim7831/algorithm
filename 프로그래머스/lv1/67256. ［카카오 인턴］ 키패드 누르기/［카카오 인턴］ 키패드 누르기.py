def solution(numbers, hand):
    keypad = {"*": (-1, 0), 0: (0, 0), "#": (1, 0), 7: (-1, 1),
              8: (0, 1), 9: (1, 1), 4: (-1, 2), 5: (0, 2),
              6: (1, 2), 1: (-1, 3), 2: (0, 3), 3: (1, 3) }
    left_now = keypad["*"]
    right_now = keypad["#"]
    
    left_nums, right_nums = set([1, 4, 7]), set([3, 6, 9])
    center_nums = set([2, 5, 8, 0])
    
    order  = ''
    
    for num in numbers:
        if num in left_nums:
            order += "L"
            left_now = keypad[num]
        elif num in right_nums:
            order += "R"
            right_now = keypad[num]
        else:
            i, j = keypad[num]
            l_len = abs(left_now[0] - i) + abs(left_now[1] - j)
            r_len = abs(right_now[0] - i) + abs(right_now[1] - j)
            if l_len > r_len:
                order += "R"
                right_now = keypad[num]
            elif r_len > l_len:
                order += "L"
                left_now = keypad[num]
            else:
                if hand[0] == 'l':
                    order += "L"
                    left_now = keypad[num]
                else:
                    order += "R"
                    right_now = keypad[num]
    return order