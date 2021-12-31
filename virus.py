n, m = map(int, input().split())
data = [] # 초기 리스트
temp = [[0] * m for _ in range(n)] # 벽을 설치한 뒤의 리스트

for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

def virus(x, y):
    for i in range(4): # 4가지 경우
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m: # 상,하,좌,우 바이러스가 전파 될수 있는 경우
            if temp[nx][ny] == 0:

                temp[nx][ny] = 2
                virus(nx, ny)

def safe_score(): # 안전한 영역을 계산하는 함수
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

def dfs(count): # dfs 알고리즘을 통해서 안전한 영역 계산
    global result

    if count == 3: # 울타리가 3개 설치된 경우
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]

        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)

        result = max(result, safe_score()) #  최대값 계산
        return

    for i in range(n):
        for j in range(m):
            if data[i][j] == 0: # 빈 공간에
                data[i][j] = 1 #울타리를 설치
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1
dfs(0)
print(result)