n,m = map(int, input().split()) # 세로의 길이 n과 가로의 길이 m 입력

graph = []
for i in range(n):
    graph.append(list(map(int, input()))) # 2차원 리스트이 맵정보 입력

def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m: # 범위를 벗어나는 경우
        return False
    if graph[x][y] == 0: # 방문하지 않았을경우
        graph[x][y] = 1 # 방문처리

        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)

        return True
    return False
        # 상하좌우 호출

result = 0

# 모든 위치에 대해서 음료수 채우고
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True: # true면
            result += 1 # result값 증가
print(result)




