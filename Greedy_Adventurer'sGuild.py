n= int(input())
x= list(map(int, input().split()))
x.sort()
ind= 0
t= x[ind] #현재 인덱스의 공포도
group= 0

while ind<n:
    temp= x[ind:ind+t] #현재 인덱스의 공포도의 수만큼의 인원의 공포도
    
    if max(temp)== t and len(temp)>= t: #공포도가 가장 높은 사람의 공포도와 그룹 인원 확인
        group+= 1 #생성된 그룹 추가
        ind+=t #생성된 그룹의 인원만큼 인덱스 이동
        if n> ind+t:
            t= x[ind]
        else:
            break
    else:
        t+=1

print(group)

