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
# 배열에서 가장 큰 숫자를 k만큼 더한 뒤, 두번째로 큰 숫자를 더하고 반복하면 가장 큰 수를 만들 수 있음
