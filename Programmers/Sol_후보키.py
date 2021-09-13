from itertools import combinations
def solution(relation):
    answer = []
    column = len(relation)
    row = len(relation[0])

    for k in range(1, row+1):
        combo = list(combinations(range(row), k))
        for com in combo:
            # 후보키 찾기
            sublist = [[] for _ in range(column)]
            for c in com:
                for k in range(column):
                    sublist[k].append(relation[k][c])
            # hashable하게 바꿔주기
            newlist = []
            for sub in sublist:
                newlist.append(" ".join(sub))

            #print(newlist)
            # 유일성 확인
            if len(newlist) == len(set(newlist)):
                # 최소성 확인 - 답 중에 부분집합이 하나라도 있으면 추가 x
                if answer:
                    new_com = list(com)
                    mark = True
                    for ans in answer:
                        cnt = 0
                        for a in ans:
                            if a in new_com:
                                cnt += 1
                        if cnt == len(ans):
                            mark = False

                    if mark == True:
                        answer.append(new_com)

                else:
                    answer.append(list(com))

    return len(answer)