from collections import defaultdict
def solution(words):
    answer = 0

    visited = [False]*len(words)

    level = 0

    while 1:
        # 종료 조건
        if visited.count(True) == len(words):
            break

        db = defaultdict(list)
        for idx, word in enumerate(words):

            if visited[idx] == False:

                # 모두 입력해야되는 경우
                if level == len(word)-1:
                    answer += (level+1)
                    visited[idx] = True
                    db[word[:level+1]].append(idx)

                elif level < len(word)-1:
                    db[word[:level+1]].append(idx)

        for d in db:
            if len(db[d]) == 1 and visited[db[d][0]] == False:
                answer += (level+1)
                visited[db[d][0]] = True

        level += 1

    return answer