# 나누기 5/3/2, 빼기 1
x= int(input())
count= 0
dp= [0]*100
while x>1:
    if x% 5== 0:
        x/= 5        
    elif x% 3== 0:
        x/= 3
    elif x% 5== 1 or x% 3== 1 or x%2== 1:
        x-= 1
    else:
        x/= 2
    count+= 1
    dp[int(x)]= count

print(dp[1])
###################################################
x= int(input())
d= [0]*30001
#bottom-up 방식
for i in range(2, x+1):
    #현재의 수에서 1을 빼는 경우
    d[i]= d[i-1]+ 1
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i% 2== 0:
        d[i]= min(d[i], d[i//2]+ 1)
    #현재의 수가 3으로 나누어 떨어지는 경우
    if i% 3== 0:
        d[i]= min(d[i], d[i//3]+ 1)
    #현재의 수가 5로 나누어 떨어지는 경우
    if i% 5== 0:
        d[i]= min(d[i], d[i//5]+ 1)

print(d[x])
