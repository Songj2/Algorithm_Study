import secrets


n, m, k= map(int, input().split())
array= list(map(int, input().split()))
array.sort(reverse=True)

lNum= array[0];
mNum= array[1];
result= 0

while m> 0:
    if m>=k+1:        
        result+= lNum* k+ mNum
        m-= (k+1)
    else:
        result+= lNum* m
        break
    
print(result)
# 14분 40초
#####################################################
# 1 단순하게 푸는 방식_이코테 풀이
n, m, k= map(int, input().split())
data= list(map(int, input().split()))

data.sort()
first= data[n-1]
second= data[n-2]

result= 0

while True:
    for i in range(k):
        if m== 0:
            break
        m-= 1
    if m== 0:
        break
    result+= second
    m-= 1

print(result)
#####################################################
# 2 파이썬 식 답안_이코테
n, m, k= map(int, input().split())
data= list(map(int, input().split()))

data.sort()
first= data[n-1]
second= data[n-2]

count= int(m/ (k+ 1))* k
count+= m% (k+ 1)

result= 0
result+=(count)* first
result+=(m-count)* second

print(result)