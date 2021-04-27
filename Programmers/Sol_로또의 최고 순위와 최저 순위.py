def solution(lottos, win_nums):
    answer = []
    sub1 = 0
    sub2 = 0
    for lo in lottos:
        if lo in win_nums:
            sub1 += 1
        if lo == 0:
            sub2 += 1

    answer = [6 if 7 - sub1 - sub2 >= 6 else 7 - sub1 - sub2, 6 if 7 - sub1 >= 6 else 7 - sub1  ]

    return answer