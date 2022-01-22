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