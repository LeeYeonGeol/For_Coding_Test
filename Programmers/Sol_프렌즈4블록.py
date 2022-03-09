import copy

def solution(m, n, board):
    answer = 0

    n_board = []
    for b in board:
        n_board.append(list(b))


    while 1:
        check = True
        visited = set()
        for x in range(m-1):
            for y in range(n-1):
                if n_board[x][y] == 'X':
                    continue
                if n_board[x][y] == n_board[x+1][y] == n_board[x][y+1] == n_board[x+1][y+1]:
                    visited.add((x, y))
                    visited.add((x+1, y))
                    visited.add((x, y+1))
                    visited.add((x+1, y+1))

        # visited가 없으면 break
        if not visited:
            break

        # 제거
        for x, y in visited:
            n_board[x][y] = ''
            answer += 1

        # 떨어지기
        for y in range(n):
            sub = ""
            for x in range(m):
                sub += n_board[x][y]

            sub = (m-len(sub))*'X'+sub


            # update
            for x in range(m):
                n_board[x][y] = sub[x]



    return answer