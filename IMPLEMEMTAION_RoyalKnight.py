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
