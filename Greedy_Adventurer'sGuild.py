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
####################################################################
n= int(input())
data= list(map(int, input().split()))
data.sort()

result= 0 #총 그룹의 수
count= 0 # 현재 그룹에 포함된 모험가의 수

for i in data: #공포도가 낮은 사람부터 확인
    count+=1 #현재 그룹에 해당 모험가 포함시키기
    if count>= i: #현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result+= 1 #총 그룹의 수 증가시키기
        count= 0 #현재 그룹에 포함된 모험가의 수 초기화

print(result) #총 그룹의 수 출력

#오름차순으로 정렬하여 공포도를 하나씩 확인
# 현재 그룹에 포함된 모험가의 수가 현재 확인하고 있는 공포도보다 크거나 같다면 같은 그룹으로 설정
# 오름차순으로 정렬되어 있으므로 항상 최소한의 모험가 수만 포함하여 그룹 결성
# 따라서 최대 그룹의 수를 알 수 있음
