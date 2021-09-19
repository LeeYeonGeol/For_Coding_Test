t = int(input())


for _ in range(t):
    plan = []
    target_w, n = map(int, input().split())
    for _ in range(n):
        x_i, w_i = map(int, input().split())
        plan.append([x_i, w_i])

    w = 0
    now = 0
    ans = 0
    for d, ww in plan:
        # 일단 직진
        ans += d-now
        w += ww
        now = d

        # 용량 상황에 따라 해결
        if w == target_w:
            # 비우기
            ans += now
            now = 0
            w = 0
        elif w > target_w:
            # 비우기
            ans += now
            now = 0
            w = 0
            # 돌아오기
            now = d
            ans += d
            w += ww

    # 마지막 쓰레기
    ans += now
    print(ans)