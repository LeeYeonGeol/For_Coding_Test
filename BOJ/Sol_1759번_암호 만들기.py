l, c = map(int, input().split())

arr = list(map(str, input().split()))

# 사전식으로 출력해야하므로 정렬
arr.sort()

# dfs결과를 저장할 리스트 생성
ans = []

# dfs 선언 start = 순서대로 출력하기 위한 변수 / v = 트리 depth / a, b = 모음, 자음 개수
def dfs(start, v, a, b):
    # v가 l가 같고 모음이 한 개이상 자음이 2개 이상이라면 결과 출력
    if v == l and a >= 1 and b >= 2:
        print("".join(ans))
        return
    else:
        for i in range(start,c):
            # 중복 제외
            if not arr[i] in ans:
                ans.append(arr[i])
                # 자음 모음 개수 세기
                if arr[i] in "aeiou":
                    dfs(i+1,v+1, a+1, b)
                else:
                    dfs(i+1,v+1, a, b+1)
                ans.pop()
dfs(0, 0, 0, 0)