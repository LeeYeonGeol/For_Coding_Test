def solution(brown, yellow):
    answer = []
    summ = brown+yellow

    for a in range(1, summ):
        if summ % a == 0:
            b = summ // a
            # a가 가로 b는 세로
            if a < b:
                a, b = b, a
            if yellow == summ - (2*a+2*b-4):
                return  [a, b]

