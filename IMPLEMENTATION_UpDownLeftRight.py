n= int(input())
plan= input().split()
 # 우 상 좌 하
dx= [0, -1, 0, 1]
dy= [1, 0, -1, 0]

x, y= 0, 0

for i in plan:
    if i== "R" and y <n-1:
        x+= dx[0]
        y+= dy[0]
    elif i== "U" and x> 0:
        x+= dx[0]
        y+= dy[0]
    elif i== "L" and y> 0:
        x+= dx[2]
        y+= dy[2]
    elif i== "D" and x< n-1:
        x+=dx[3]
        y+=dy[3]

print(x+1, y+1)
##################################################
n= int(input())
x, y= 0, 0
plans= input().split()
 
#  L, R, U, D에 따른 이동 방향
dx= [0, 0, -1, 1]
dy= [-1, 1, 0, 0]
move_types= ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    #이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan== move_types[i]:
            nx= x+ dx[i]
            ny= y+ dy[i]
    #공간을 벗어나는 경우 무시
    if nx<1 or ny<1 or nx>n or ny>n:
        continue
    #이동 수행
    x, y= nx, ny
    
print(x, y)
