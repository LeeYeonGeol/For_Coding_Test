from collections import defaultdict

def solution(genres, plays):
    answer = []

    # 1번
    dict1 = defaultdict(int)
    dict2 = defaultdict(list)
    for idx, genre in enumerate(genres):
        dict1[genre] += plays[idx]
        dict2[genre].append((plays[idx], idx))

    n1 = []
    for dict in dict1:
        n1.append((dict1[dict],dict))

    n1.sort(reverse=True)
    # 2번, 3번
    for n in n1:
        if len(dict2[n[1]]) == 1:
            answer.append(dict2[n[1]][0][1])
        else:
            tmp = dict2[n[1]]
            tmp.sort(key = lambda x : (-x[0],x[1]))

            answer.append(tmp[0][1])
            answer.append(tmp[1][1])

    return answer