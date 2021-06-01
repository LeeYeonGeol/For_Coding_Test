from collections import deque
import sys

input = sys.stdin.readline

s = int(input())


# 클립보드 여부
ans = [[-1]*1001 for _ in range(1001)]

q = deque()

ans[1][0] = 0

# 화면 이모티콘 개수 / 클립보드 개수
q.append((1,0))

cnt = 1

while q:
    now, clib = q.popleft()

    # 1번
    if ans[now][now] == -1:
        ans[now][now] = ans[now][clib]+1
        q.append((now, now))
    # 2번

    if 2 <= now+clib <= 1000 and ans[now+clib][clib] == -1:
        ans[now+clib][clib] = ans[now][clib]+1
        q.append((now+clib, clib))
    # 3번
    if 2 <= now-1 and ans[now-1][clib] == -1:
        ans[now-1][clib] = ans[now][clib]+1
        q.append((now-1, clib))

ans2 = ans[s]

ans2.sort()
cnt = 0
while 1:
    if ans2[cnt] != -1:
        print(ans2[cnt])
        break
    cnt += 1