def solution(scores):
    n = len(scores)
    answer = ''
    n_scores = [[0]*n for _ in range(n)]

    for a in range(n):
        for b in range(n):
            n_scores[a][b] = scores[b][a]

    for idx, score in enumerate(n_scores):
        mean = 0
        if score[idx] == max(score) or score[idx] == min(score):
            # 유일성
            if score.count(score[idx]) == 1:
                mean = (sum(score)-score[idx]) / (len(score)-1)
            else:
                mean = sum(score) / len(score)

        else:
            mean = sum(score) / len(score)

        if mean >= 90:
            answer += 'A'
        elif 80 <= mean < 90:
            answer += 'B'
        elif 70 <= mean < 80:
            answer += 'C'
        elif 50 <= mean < 70:
            answer += 'D'
        elif mean < 50:
            answer += 'F'

    return answer