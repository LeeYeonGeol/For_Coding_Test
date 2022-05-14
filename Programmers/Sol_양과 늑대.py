from collections import deque

def solution(info, edges):
    answer = 1

    n = len(info)

    graph = [[] for _ in range(n)]

    for a, b in edges:
        graph[a].append(b)

    q = deque()

    # 양 개수, 늑대 개수, visited
    q.append((1, 0, [0]))

    while q:
        yang, wolf, visited = q.popleft()
        answer = max(answer, yang)

        for leaf in visited:
            for next_vertex in graph[leaf]:
                if next_vertex in visited:
                    continue
                # 양이라면?
                if info[next_vertex] == 0:
                    q.append((yang+1, wolf, visited+[next_vertex]))
                # 늑대라면?
                else:
                    if yang > wolf+1:
                        q.append((yang, wolf+1, visited+[next_vertex]))


    return answer