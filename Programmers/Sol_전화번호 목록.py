def solution(phone_book):

    answer = True

    dic = dict()
    for phone_number in phone_book:
        dic[phone_number] = 1

    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in dic and temp != phone_number:
                answer = False
    return answer