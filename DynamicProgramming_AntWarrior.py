n= int(input())
food= list(map(int, input().split()))

result= [0]*2
for i in range(0, 2):
    for j in range(i, n, 2):
        result[i]+= food[j]

print(max(result))
################################################
# dp 아이디어 참고
dp=[0]*n
dp[0]= food[0]
dp[1]= food[1]

for i in range(2, n):
    dp[i]= dp[i-2]+food[i]

print(max(dp))
################################################
n= int(input())
array= list(map(int, input().split()))
#dp테이블 초기화
d= [0]*100
#bottom-up방식
d[0]= array[0]
d[1]= max(array[0], array[1])
for i in range(2, n):
    d[i]= max(d[i-1], d[i-2]+ array[i])

print(d[n-1])
