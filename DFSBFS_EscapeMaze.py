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