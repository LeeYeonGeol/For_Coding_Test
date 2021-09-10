from itertools import combinations
from collections import defaultdict
import copy
from bisect import bisect_left, bisect_right

def solution(info, query):
    answer = []
    db = defaultdict(list)

    for i in info:                   # info에 대해 반복
        temp = i.split()
        conditions = temp[:-1]
        score = int(temp[-1])
        for n in range(5):
            combi = list(combinations(range(4), n))
            for c in combi:
                conditions2 = conditions.copy()
                for v in c:
                    conditions2[v] = '-'
                db[" ".join(conditions2)].append(score)

    for value in db.values():
        #value.append(0)
        value.sort()

    for idx, q in enumerate(query):
        qry = [i for i in q.split() if i != 'and']
        q_start = " ".join(qry[:-1])
        q_score = int(qry[-1])
        if q_start in db:
            answer.append(len(db[q_start])-bisect_left(db[q_start], q_score))
        else:
            answer.append(0)
    return answer