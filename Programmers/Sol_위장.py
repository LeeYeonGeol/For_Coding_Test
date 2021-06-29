from collections import defaultdict

def solution(clothes):
    answer = 1

    dic = defaultdict(list)

    for cloth in clothes:
        x, y = cloth
        dic[y].append(x)

    for value in list(dic.values()):
        answer *= len(value)+1


    return answer-1