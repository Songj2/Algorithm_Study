n, m= map(int, input().split())
frame= []
for i in range(n):
    frame.append(list(map(int, input().split())))

count= 0
way= [(0, 1), (1, 0), (0, -1), (-1, 0)]
visited= frame

def check(x, y, frame, visited, count):
    if frame[x][y]== 0:
        visited[x][y]= 3 #방문 처리
        # print("Count", count, x, y)
        
        for i in way:
            nx= x+i[0]
            ny= y+i[1]
            if 0<= nx< n and 0<= ny< m: #주변 확인
                check(nx, ny, frame, visited, count)
    else:
        return 0

    return 1  

for i in range(n):
    for j in range(m):
        if visited[i][j]== 0: #방문하지 않은 칸이면 주변 확인
            count+= check(i, j, frame, visited, count)
    
print(count)
################################################################
n, m= map(int, input().split())
graph= []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    #주어진 범위를 벗어나는 경우에 종료
    if x<= -1 or x>= n or y<= -1 or y>m:
        return False
    
    #현재 노드를 아직 방문하지 않았다면
    if graph[x][y]== 0:
        #해당 노드 방문 처리
        graph[x][y]= 1
        #상하좌우의 위치를 재귀적으로 호출
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

#모든 노드에 대하여 음료수 채우기
result= 0
for i in range(n):
    for j in range(m):
        #현재 위치에서 dfs수행
        if dfs(i, j)== True:
            result+= 1

print(result)
