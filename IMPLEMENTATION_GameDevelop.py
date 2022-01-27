#0-육자1-바다   /   0:북 1:동 2:남 3:서
#현재 방향기준 반시계 방향, 가보지 않은 칸이 존재한다면 회전후 이동/존재하지 않으면 회전만
# 네방향모두 가보거나 바다로 되어있다면 바라보는 방향유지한 채 뒤로이동/바다 칸인 경우 중지
# 방문 칸수 출력
n,m= map(int, input().split())
x, y, d= map(int, input().split())

mapData= []
for i in range(n):
    mapData.append(list(map(int, input().split())))
 
direction= [(-1,0), (0, 1), (1, 0), (0, -1)]
count= 0

while True:
    for i in range(1,5): #각 방향 확인
        move= False
        nd= d-i
        if nd<0:
            nd+= 4
        nx= x+ direction[nd][0]
        ny= y+ direction[nd][1]

        if mapData[nx][ny]== 0: #가보지 않은 육지가 있다면
            mapData[nx][ny]= 3 #방문 처리
            x, y= nx, ny # 이동
            count+=1 
            d= nd #전환된 방향 유지
            move= True
            break
    #이동이 방문하지 않은 육지가 없고, 뒷칸이 방문할 육지일 경우 뒷칸으로 이동
    if not move and mapData[x+ direction[d-2][0]][y+ direction[d-2][1]]== 3: 
        x+= direction[d-2][0]
        y+= direction[d-2][1]

    #뒷칸이 바다이면 while문 탈출
    elif not move:
        break
        
print(count)
    