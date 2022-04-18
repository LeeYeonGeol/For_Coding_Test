from itertools import combinations
def solution(places):
    answer = []

    for id, place in enumerate(places):
        sub_list = []
        for x in range(5):
            for y in range(5):
                if place[x][y] == 'P':
                    sub_list.append((x, y))

        for sub in list(combinations(sub_list, 2)):
            x1, y1 = sub[0]
            x2, y2 = sub[1]
            # 1은 ㄴㄴ
            if abs(x1-x2)+abs(y1-y2) == 1:
                answer.append(0)
                break
            # 2는 case나눠서 보기
            elif abs(x1-x2)+abs(y1-y2) == 2:
                if x1 == x2:
                    if place[x1][(y1+y2)//2] != 'X':
                        answer.append(0)
                        break

                elif y1 == y2:
                    if place[(x1+x2)//2][y1] != 'X':
                        answer.append(0)
                        break

                else:
                    if place[x1][y2] == 'O' or place[x2][y1] == 'O':
                        answer.append(0)
                        break

        else:
            answer.append(1)

    return answer