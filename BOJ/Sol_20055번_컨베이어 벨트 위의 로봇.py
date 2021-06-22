# n = 컨베이어 벨트 길이, k = 내구도 0이 k개 이상이면 종료
n, k = map(int, input().split())

belt = list(map(int, input().split()))
robot = [0]*n

ans = 1

while(1):

    # 1. 한 칸 회전
    belt = [belt[-1]] + belt[:-1]
    robot= [0]+robot[:-1]
    robot[n-1] = 0

    # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 이동.
    for i in range(n-2, -1, -1):
        if robot[i] == 1:
            if robot[i+1] == 0 and belt[i+1] > 0:
                robot[i] = 0
                robot[i+1] = 1
                belt[i+1] -= 1

    # 3. 로봇 올리기
    if belt[0] > 0 and robot[0] == 0:
        robot[0] = 1
        belt[0] -= 1

    # 4. 종료
    if belt.count(0) >= k:
        print(ans)
        break

    ans += 1