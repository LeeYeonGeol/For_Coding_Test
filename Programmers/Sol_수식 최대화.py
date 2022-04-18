from itertools import permutations
from collections import defaultdict
import copy
def solution(expression):
    answer = 0
    s = ""
    arr = []

    sub = ""
    for ex in expression:
        if ex.isdigit():
            sub += ex
        else:
            arr.append(int(sub))
            sub = ""
            arr.append(ex)

    if sub:
        arr.append(int(sub))

    def operator(a, b, c):
        if c == '+':
            return a+b
        elif c == '*':
            return a*b
        else:
            return a-b

    for purm in list(permutations(['+',"*",'-'], 3)):
        narr = copy.deepcopy(arr)
        for idx in range(3):
            while 1:
                if purm[idx] in narr:
                    idx2 = narr.index(purm[idx])
                    narr = narr[:idx2-1]+ [operator(narr[idx2-1], narr[idx2+1], purm[idx])] +narr[idx2+2:]
                else:
                    break

        answer = max(answer, abs(narr[0]))

    return answer