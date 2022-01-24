#00시00분00초 부터 N시 59분 59초까사이 3이 포함된 경우 카운트
n= int(input())
scount= 0
result= 0
#초에서 구하기
for i in range(60):
    if '3' in str(i):
        print(str(i))
        scount+= 1

for i in range(n+1):
    if '3' not in str(i):      
        for j in range(60):
            if '3' not in str(j):
                result+= scount
            else:
                result+=60
    else:
        result+=3600

print(result)

##########################################
# 3중 반복문 ver.
for i in range(n+1):
    if '3' not in str(i):      
        for j in range(60):
            if '3' not in str(j):
                for k in range(60):
                    if '3' in str(k):
                        result+= 1
            else:
                result+=60
    else:
        result+=3600


