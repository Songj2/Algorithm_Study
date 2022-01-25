x, y= input()
x= ord(x)- 97 #아스키코드 이용_x의 입력값은 소문자이므로 
y= int(y)- 1
move= [[-2,-1],[-2,1], [-1,2], [1,2], [2, 1], [2, -1], [1, -2], [-1, -2]] #방향벡터
count= 0

for i in move:
    if 0<=x+ i[1]<8 and 0<=y+ i[0]<8: #범위를 벗어나지 않는다면
        count+= 1
        # print(i, chr(x+ i[1]+ 97), y+ +i[0]+ 1)

print(count)
###################################################################################
input_data= input()
row= int(input_data[1])
column= int(ord(input_data[0]))- int(ord('a'))+1

# 나이트가 이동할 수 있는 방향 정의
steps= [(-2,-1),(-2,1), (-1,2), (1,2), (2, 1), (2, -1), (1, -2), (-1, -2)]

result= 0
#이동하고자 하는 위치 확인
for step in steps:
    next_row= row+ step[0]
    next_column= column+ step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row>= 1 and next_row<= 8 and next_column>= 1 and next_column<= 8:
        result+= 1
print(result)
