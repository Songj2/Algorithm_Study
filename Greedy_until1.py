# 1. n-1
#2. n/k
#최소 횟 수
n, k= map(int, input().split())
count= 0

while n> 1:
    if n%k==0:
        n//= k

    else:
        n-=1
    count+= 1
print(count)
