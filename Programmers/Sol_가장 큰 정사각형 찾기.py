def solution(board):
    answer = 0
    n = len(board)
    m = len(board[0])
    for x in range(n):
        for y in range(m):
            px1, py1 = x-1,y-1
            px2, py2 = x-1,y
            px3, py3 = x, y-1
            if board[x][y] == 1:
                if 0 <= px1 < n and 0 <= py1 < m:
                    if board[px2][py2] > 0 and board[px3][py3] > 0 and board[px1][py1] > 0:

                        board[x][y] =  min(board[px1][py1], board[px2][py2], board[px3][py3])+1
            answer = max(answer, board[x][y]**2)


    return answer


