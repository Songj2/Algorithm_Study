#n개의 수가 들어있는 배열에서, m번 더해서 가장 큰 수 만들기. 같은 인덱스의 수는 k번이상 연속 불가 
n, m, k= map(int, input().split())

numList= list(map(int, input().split()))
numList.sort(reverse=True)

result= 0 
kCount= k #반복문에서 사용할 연속 횟수

for i in range(m):
    if kCount>0: #같은 인덱스의 수가 k만큼 반복되지 않았으면
        result+=numList[0] #가장 큰 수 더함
        kCount-=1 #연속 횟수 빼줌

    else: #같은 인덱스의 수가 k만큼 반복됬으면
        result+=numList[1] #두번째로 큰 수를 더함
        kCount= k #연속 횟수 초기화

print(result)
# 배열에서 가장 큰 숫자를 k만큼 더한 뒤, 두번째로 큰 숫자를 한번 더하기를 반복하면 가장 큰 수를 만들 수 있음
#####################################################################
# 반복되는 수열에 대해 파악하여 시간복잡도를 줄일 수 있음
n, m, k= map(int, input().split())
data= list(map(int, input().split()))

data.sort() 
first= data[n-1] #가장 큰 수
second= data[n-2] # 두 번째로 큰 수

#가장 큰 수가 더해지는 횟수 계산
count= int(m/(k+ 1))* k #(K+ 1)의 반복
count+= m% (k+ 1) #m이 (k+ 1)로 나눠 떨어지지 않는 경우도 계산

result= 0
result+= (count)* first #가장 큰 수 더하기
result++ (m- count)* second #두 번째로 큰 수 더하기

print(result)
