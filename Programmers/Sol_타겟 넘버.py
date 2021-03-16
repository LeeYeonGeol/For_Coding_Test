from collections import deque
def solution(numbers, target):
    answer = 0
    q = deque()
    q.append((numbers[0], 0))
    q.append((-numbers[0], 0))

    while q:
        score, cnt = q.popleft()
        ncnt = cnt + 1
        if ncnt >= len(numbers):
            continue
        if ncnt == len(numbers)-1:
            if score+numbers[ncnt] == target:
                answer += 1
            if score-numbers[ncnt] == target:
                answer += 1
        q.append((score+numbers[ncnt], ncnt))
        q.append((score-numbers[ncnt], ncnt))
    return answer