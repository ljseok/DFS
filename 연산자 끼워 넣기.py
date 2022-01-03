n = int(input()) # 연산의 개수 입력
oper_num = list(map(int, input().split())) # 연산 데이터 입력받기
add, sub, mul, div = map(int,input().split())

min_val = 1e9
max_val = -1e9

def dfs(i, now):
    global min_val, max_val, add, sub, mul, div

    if i == n : # 모든 연산자를 다 사용했을 경우
        min_val = min(min_val, now)
        max_val = max(max_val, now)
    else:
        if add > 0:
            add -= 1
            dfs(i+1, now + oper_num[i])
            add += 1
        if sub> 0:
            sub -= 1
            dfs(i + 1, now - oper_num[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * oper_num[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, now / oper_num[i])
            div += 1

dfs(1, oper_num[0])

print(max_val)
print(min_val)
