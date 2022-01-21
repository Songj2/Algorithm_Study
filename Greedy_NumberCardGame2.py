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