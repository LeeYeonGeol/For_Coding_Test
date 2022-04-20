from collections import defaultdict
def solution(gems):
    idx1 = 0
    idx2 = 0

    target = len(set(gems))

    db = defaultdict(int)

    dist = 1e9

    answer = [0,0]

    while 1:

        # 현재위치 담기
        db[gems[idx2]] += 1


        # 답에 해당하면 리턴
        if len(db) == target:
            while 1:
                db[gems[idx1]] -= 1

                if db[gems[idx1]] == 0:
                    db[gems[idx1]] += 1
                    break

                idx1 += 1

            if dist > idx2-idx1:

                dist = idx2-idx1
                answer = [idx1+1, idx2+1]


        idx2 += 1
        if idx2 == len(gems):
            break


    return answer