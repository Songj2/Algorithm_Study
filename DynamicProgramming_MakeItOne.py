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