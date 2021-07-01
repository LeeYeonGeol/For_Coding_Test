import heapq
def solution(scoville, K):
    answer = 0
    n = len(scoville)
    heapq.heapify(scoville)

    while scoville:
        a, b = -1, -1
        a = heapq.heappop(scoville)
        if scoville:
            b = heapq.heappop(scoville)

        if a >= K:
            return answer
        else:
            answer += 1

            if a != -1 and b == -1:
                return -1
            else:
                heapq.heappush(scoville, (a+(b*2)))
