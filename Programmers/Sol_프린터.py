from collections import deque
def solution(priorities, location):
    answer = 1
    q = deque()

    for idx, p in enumerate(priorities):
        q.append((p, idx))

    while q:
        pr, locc = q.popleft()

        if q:
            if pr >= max(q)[0]:
                if locc == location:
                    return answer
                else:
                    answer += 1
            else:
                q.append((pr, locc))
        else:
            return answer