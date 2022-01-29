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