from collections import deque

c = int(input())


for _ in range(c):
    s, t = map(int, input().split())

    ans = t-s

    q = deque()

    q.append((s, t, 0)) # 내 점수, 상대 점수, 발차기 횟수

    while q:
        my, enemy, cnt = q.popleft()

        # 최소인 경우 정답 갱신
        if my == enemy and cnt < ans:
            ans = cnt

        # 갈 필요 없을 경우 pruning
        if cnt >= ans:
            continue

        if 2*my <= enemy+3:
            q.append((2*my, enemy+3, cnt+1))

        if my+1 <= enemy:
            q.append((my+1, enemy, cnt+1))



    print(ans)

