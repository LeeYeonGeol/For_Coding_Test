from itertools import combinations
from collections import Counter
def solution(orders, course):
    res = []
    for x in course:
        ans = []
        for order in orders:
            sub = list(order)
            sub.sort()
            combos = list(combinations(sub,x))
            for combo in combos:
                ans.append(combo)

        ans2 = Counter(ans)
        ans3 = ans2.most_common()
        if ans3:
            best = ans3[0][1]
            for x in ans3:
                subcombo, cnt = x
                if cnt == best and best >= 2:
                    subcombo2 = ""
                    for sub in subcombo:
                        subcombo2 += sub
                    res.append(subcombo2)
                else:
                    break
    res.sort()
    return res