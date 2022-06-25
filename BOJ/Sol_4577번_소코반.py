import sys
input = sys.stdin.readline

game = 0
while 1:
    game += 1
    # 가로, 세로
    R, C = map(int, input().split())
    
    if R == 0 and C == 0:
        break
    
    # 초기화
    sokoban = [list(input().rstrip()) for _ in range(R)]

    # 캐릭터 위치
    cx, cy = 0, 0

    # 현재 박스 상태 & 박스 목표
    box_state, box_target = 0, 0
    targets = []

    # 현재 상태로 초기화
    for a in range(R):
        for b in range(C):
            if sokoban[a][b] == 'w':
                cx, cy = a, b
            elif sokoban[a][b] == 'W':
                targets.append((a, b))
                cx, cy = a, b
                box_target += 1
            elif sokoban[a][b] == 'B':
                targets.append((a, b))
                box_state += 1
                box_target += 1    
            elif sokoban[a][b] == '+':
                targets.append((a, b))
                box_target += 1
                sokoban[a][b] = '.'

    # 입력 키
    keys = list(input().rstrip())

    # 방향 설정
    direction = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

    # for 문 돌리기
    for key in keys:
        add_x, add_y = direction[key]
        ncx, ncy = cx+add_x, cy+add_y

        # 빈칸이라면 그 칸으로 이동
        if sokoban[ncx][ncy] == '.':
            sokoban[cx][cy] = '.'
            sokoban[ncx][ncy] = 'w'
            cx, cy = ncx, ncy
            
        # 지시한 방향에 박스가 있다면 
        elif sokoban[ncx][ncy].lower() == 'b':
            # 비어있는 경우 -> 이동 u, b, .
            if sokoban[ncx+add_x][ncy+add_y] == '.':
                sokoban[cx][cy] = '.'
                sokoban[ncx][ncy] = 'w'
                sokoban[ncx+add_x][ncy+add_y] = 'b'
                cx, cy = ncx, ncy
                # 타겟 처리
                if (ncx, ncy) in targets:
                    box_state -= 1
                if (ncx+add_x, ncy+add_y) in targets:
                    box_state += 1

            # 막혀있는 경우 -> 이동 x
            else:
                pass
        

        # 지시한 방향이 벽 -> 이동 x
        elif sokoban[ncx][ncy] == '#':
            pass

        # 모든 박스가 목표점 이동하면, break
        if box_state == box_target:
            # 타겟 처리.
            for x, y in targets:
                sokoban[x][y] = 'B'
            print("Game "+str(game)+": complete")
            for soko in sokoban:
                print("".join(soko))  
            break

    else:
        # 타겟 처리.
        for x, y in targets:
            if sokoban[x][y] == '.':
                sokoban[x][y] = '+'
            elif sokoban[x][y] == 'b':
                sokoban[x][y] = 'B'
            elif sokoban[x][y] == 'w':
                sokoban[x][y] = 'W'

        print("Game "+str(game)+": incomplete")
        for soko in sokoban:
            print("".join(soko))    





