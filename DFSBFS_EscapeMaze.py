#괴물: 0    없음: 1
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
n, m= map(int, input().split())

maze= []
for i in range(n):
    maze.append(list(map(int, input())))

way= [(0, 1), (1, 0), (0, -1), (-1, 0)]

def escape(x, y):
    if x==n-1 and y== m-1: #끝점이면 종료
        return 1
    # print(x,y)
    maze[x][y]= 0 #방문 처리

    for i in way:
        nx= x+i[0]
        ny= y+i[1]
        if 0<= nx<n and 0<= ny<m and maze[nx][ny]== 1: #괴물이 없는곳이면 이동
            return 1+ escape(nx, ny)
    
print(escape(0, 0))
######################################################################################
#BFS를 이용해 가장 가까운 노드부터 탐색
from collections import deque   

def bfs(x, y):
    queue= deque()
    queue.append((x, y))

    while queue:
        x, y= queue.popleft()

        # 현재 위치에서 4방향으로 확인
        for i in range(4):
            nx= x+ dx[i]
            ny= y+ dy[i]

            #공간을 벗어나는 경우 무시
            if nx< 0 or nx>=n or ny<0 or ny>= m:
                continue
            #벽인 경우 무시
            if graph[nx][ny]==0:
                continue
            #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny]== 1:
                graph[nx][ny]= graph[x][y]+ 1
                queue.append((nx, ny))
    #가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]

n, m= map(int, input().split())

graph= []
for i in range(n):
    graph.append(list(map(int, input())))

dx= [-1, 1, 0, 0 ]
dy= [0, 0, -1, 1 ]

print(bfs(0, 0))
