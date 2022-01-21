n, m= map(int, input().split())
card= []

for i in range(n):
    card.append(list(map(int, input().split())))

result= 0

for i in range(n):
    minValue= min(card[i]) #각 행에서 가장 작은 값 저장
    if minValue>result: #이전 행의 값이랑 비교
        result= minValue #더 큰값 저장
    
print(result)
#######################################################
# 각 행마다 가장 작은 수를 찾은 뒤, 그 수 중에서 가장 큰 수 찾기
# min()함수나 2중 반복문 구조를 이용할 수 있어야 함
#min() ver.
n, m= map(int, input().split())

result= 0
for i in range(n):
    data= list(map(int,input().split()))
    #현재 줄에서 가장 작은 수 찾기
    min_Value= min(data) 
    #가장 작은 수들 중에서 가장 큰 수 찾기
    result= max(result, min_Value)

print(result)

#2중 반복문 ver.
n, m= map(int, input().split())

result= 0
for i in range(n):
    data= list(map(int,input().split()))
    #현재 줄에서 가장 작은 수 찾기
    min_Value= 10001 #입력 조건에서 입력으로 들어오는 수는 10000이하의 수 이므로
    for a in data:
        min_Value= min(min_Value, a)
    #가장 작은 수들 중에서 가장 큰 수 찾기
    result= max(result, min_Value)

print(result)
