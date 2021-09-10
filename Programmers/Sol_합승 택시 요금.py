import heapq
def solution(n, s, a, b, fares):
    INF = 1e9
    # n = 지점의 개수, s = 시작 지점, a = a의 도착 지점, b = b의 도착 지점, fares = 요금
    answer = 0

    # 그래프 생성
    graph = [[] for _ in range(n+1)]
    for fare in fares:
        aa, bb, price = fare
        graph[aa].append((bb, price))
        graph[bb].append((aa, price))

    # a, b에 대해 각각 최단 거리 구하기

    distance1 = [INF]*(n+1)
    distance1[s] = 0
    q = [(s, 0)]

    while q:
        v, dist = heapq.heappop(q)
        for v2, price in graph[v]:
            cost = dist + price
            if distance1[v2] > cost:
                distance1[v2] = cost
                heapq.heappush(q, (v2, cost))
    answer += distance1[a]
    answer += distance1[b]

    # 모든 경우에 대해서 탐색
    for k in range(1, n+1):

        if k == s:
            continue
        # 탑승해서 간게 크면 패스
        if distance1[k] > answer:
            continue
        # 다익스트라 적용
        distance2 = [INF]*(n+1)
        distance2[k] = 0
        q = [(k, 0)]

        subanswer = distance1[k]
        while q:
            v, dist = heapq.heappop(q)
            for v2, price in graph[v]:
                cost = dist + price
                if distance2[v2] > cost:
                    distance2[v2] = cost
                    heapq.heappush(q, (v2, cost))
        subanswer += distance2[a]
        subanswer += distance2[b]
        answer = min(answer, subanswer)

    return answer