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
###########################################################################################
# 방향백터를 이용하는 것이 효과적
# #리스트 컴프리헨션 문법을 사용해 2차원 리스트를 초기화_2차원 리스트를 선언할 때 컴프리헨션을 이용하는 것이 효율적
# 왼쪽으로 회전: turn_left()에서 global키워드 사용_ 정수형 번수인 direction변수가 함수 바깥에서 선언된 전역 변수이기 때문
#     
n,m= map(int, input().split())
#방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d= [[0]*m for _ in range(n)]

x, y, direction= map(int, input().split())
d[x][y]= 1 #현재 좌표 방문 처리
array= []
#전체 맵 정보 입력받기
for i in range(n):
    array.append(list(map(int, input().split())))
#북 ,동, 남, 서 방향 정의
dx= [-1, 0, 1, 0]
dy= [0, 1, 0, -1]

#왼쪽으로 회전
def turn_left():
    global direction
    direction-= 1
    if direction== -1:
        direction= 3

#시물레이션
count= 1
turn_time= 0
while True:
    #왼쪽 회전
    turn_left()
    nx= x+ dx[direction]
    ny= y+ dy[direction]
    #회전한 후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny]== 0 and array[nx][ny]== 0:
        d[nx][ny]= 1
        x= nx
        y= ny
        count+= 1
        turn_time= 0
        continue
    #회전한 후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time+= 1
    if trun_time== 4:
        nx= x-dx[direction]
        ny= y-dy[direction]

        if array[nx][ny]== 0:
            x= nx
            y= ny
        #뒤가 바다로 막혀 있는 경우
        else:
            break
        turn_time= 0

print(count)    
