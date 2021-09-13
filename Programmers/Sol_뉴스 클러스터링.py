import math
def solution(str1, str2):
    # 소문자 대문자 차이 무시
    str1 = str1.lower()
    str2 = str2.lower()

    # 집합 나누기
    a1 = []
    for k in range(len(str1)-1):
        if str1[k:k+2].isalpha():
            a1.append(str1[k:k+2])

    b1 = []
    for k in range(len(str2)-1):
        if str2[k:k+2].isalpha():
            b1.append(str2[k:k+2])

    # 자카드 유사도 계산
    # 교집합 구하기
    kyo = 0

    if len(a1) > len(b1):
        a1, b1 = b1, a1

    visited1 = [False]*len(a1)
    visited2 = [False]*len(b1)
    for idx1, a in enumerate(a1):
        for idx2, b in enumerate(b1):
            if a == b and visited2[idx2] == False:
                visited1[idx1] = True
                visited2[idx2] = True
                kyo += 1
                break
    # 합집합 구하기
    hap = kyo + visited1.count(False) + visited2.count(False)


    if hap == 0:
        return 65536

    return int(kyo/hap*65536)

