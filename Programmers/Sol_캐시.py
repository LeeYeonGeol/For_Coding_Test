from collections import deque
def solution(cacheSize, cities):
    cache = deque()
    answer = 0
    for i in cities:
        i = i.lower()
        # 캐쉬에 있는지 검사
        if i in cache:
            del cache[cache.index(i)]
            cache.append(i)
            answer += 1
        else:
            cache.append(i)
            answer += 5

        # 캐쉬 빼주기
        if len(cache) > cacheSize:
            cache.popleft()

    return answer