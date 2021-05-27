n = int(input())
tri = []
for _ in range(n):
    tri.append(list(map(int,input().split())))

for i in range(1,n):
     for j in range(i+1):
     # 바깥쪽애들은 그대로 더해주기
        if j == 0:
            tri[i][j] += tri[i-1][j]
        elif j == i:
            tri[i][j] += tri[i-1][j-1]
     # 안쪽애들은 max사용.
        else:
            tri[i][j] += max(tri[i-1][j-1],tri[i-1][j])

print(max(tri[n-1]))