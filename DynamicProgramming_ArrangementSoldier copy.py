n= int(input())
soldier= list(map(int, input().split()))
dp= [1e9]*n
dp[0]= soldier[0]
count= 0
i= 1
while i< n:
    if i== n-1 and dp[i-1]> soldier[i]: 
        dp[i]= soldier[i]
    elif dp[i-1]> soldier[i] and soldier[i]> soldier[i+1]:
        dp[i]= soldier[i]
    else:
        count+=1
    i+= 1
print(count)
