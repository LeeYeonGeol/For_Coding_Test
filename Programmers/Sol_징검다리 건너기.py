def solution(stones, k):
    answer = 0

    start, end = min(stones), max(stones)

    # 못건너면 True, 건너면 False
    def checking(value):
        cnt = 0

        for stone in stones:
            if stone - value <= 0:
                cnt += 1
            else:
                cnt = 0

            if cnt >= k:
                return True

        return False

    answer = 200000000

    # 이분 탐색
    while start <= end:
        mid = (start+end) // 2

        # 건널 수 있는 경우
        if checking(mid) == False:
            start = mid+1
        else:
            answer = min(answer, mid)
            end = mid-1

    return answer
