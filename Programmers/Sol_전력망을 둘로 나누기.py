from collections import deque
def solution(n, wires):
    answer = 1e9

    # graph 생성
    graph = [[] for _ in range(n+1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    # 각 wire별 경우의 수 따지기
    for a, b in wires:
        cnt1 = 0
        cnt2 = 0

        visited = [False]*(n+1)
        # a 따지기
        q = deque()
        q.append(a)
        visited[a] = True
        while q:
            now = q.popleft()
            cnt1 += 1
            for next_v in graph[now]:
                if next_v != b and visited[next_v] == False:
                    q.append(next_v)
                    visited[next_v] = True

        # b 따지기
        q = deque()
        q.append(b)
        visited[b] = True
        while q:

            now = q.popleft()
            cnt2 += 1
            for next_v in graph[now]:
                if next_v != a and visited[next_v] == False:
                    q.append(next_v)
                    visited[next_v] = True

        answer = min(answer, abs(cnt1-cnt2))



    return answer