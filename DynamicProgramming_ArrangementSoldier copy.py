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
##########################################################
# 가장 긴 증가하는 부분 수열(Longest Incresing Subsequence, LIS)의 전형적인 다이나밍 프로그램이 문제\
# 가장 긴 감소하는 부분 수열을 찾는 문제
# 점화식: D[i]= max(D[i], D[j]+ 1) if array[j]< array[i]
n= int(input())
array= list(map(int, input().split()))
# 순서를 오름차순으로 뒤집어, 최장 증가하는 부분 수열(LIS)로 해결
array.reverse()

dp= [1]*n

# LIS 수행
for i in range(1, n):
    for j in range(0, i):
        if array[j]< array[i]:
            dp[i]= max(dp[i], dp[j]+ 1)

print(n-max(dp))
