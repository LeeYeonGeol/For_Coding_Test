from collections import deque

def solution(begin, target, words):
    answer = 0
    if not target in words:
        return answer

    visited = [False]*len(words)

    q = deque()
    q.append((begin, 0))

    while q:
        begin, ans = q.popleft()
        if begin == target:
            return ans

        for idx, word in enumerate(words):
            cnt = 0
            if visited[idx] == False:
                for k in range(len(begin)):
                    if begin[k] != word[k]:
                        cnt += 1
                    if cnt >= 2:
                        break
                else:
                    print(cnt)
                    visited[idx] = True
                    q.append((word, ans+1))