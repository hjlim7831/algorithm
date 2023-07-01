def solution(phone_book):
    phone_book.sort()
    answer = True
    for i in range(len(phone_book)-1):
        num1, num2 = phone_book[i], phone_book[i+1]
        l1, l2 = len(num1), len(num2)
        if l1 < l2 and num1 == num2[:l1]:
            answer = False
            break
    return answer