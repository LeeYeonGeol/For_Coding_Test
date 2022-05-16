import copy
answer = []
def solution(n, info):
    global answer

    def dfs(level, grade):
        global answer
        appeach = 0
        lion = 0
        for k in range(11):
            if info[k] == grade[k] == 0:
                continue
            if info[k] >= grade[k]:
                appeach += (10-k)
            else:
                lion += (10-k)

        if lion > appeach:
            ngrade = copy.deepcopy(grade)
            ngrade[-1] += (n-level)

            if not answer:
                answer = [lion-appeach, ngrade]
            else:
                sub_answer = []
                sub_answer.append(answer)
                sub_answer.append([lion-appeach, ngrade])
                sub_answer.sort(key = lambda x : (-x[0], -x[1][10], -x[1][9], -x[1][8], -x[1][7], -x[1][6], -x[1][5], -x[1][4], -x[1][3], -x[1][2], -x[1][1], -x[1][0]))
                answer = sub_answer[0]


        for k in range(11):
            if info[k] < grade[k]:
                continue

            if n-level > info[k]:
                grade[k] += (info[k]+1)
                dfs(level+(info[k]+1), grade)
                grade[k] -= (info[k]+1)

    dfs(0, [0]*11)

    if not answer:
        return [-1]
    else:
        return answer[-1]
