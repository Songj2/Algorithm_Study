n, m= map(int, input().split())
money= []
for i in range(n):
    money.append(int(input()))

money.sort(reverse=True)

count= 0
for i in money:
    if m>i:
        count= m//i
        m= m% i
    else:
        break

if m!= 0:
    print("-1")
else:
    print(count)
######################################################
n, m= map(int, input().split())
array= []
for i in range(n):
    array.append(int(input()))

d=[10001]*(m+1)
#Bottom-up 방식
d[0]= 0
for i in range(n):
    for h in range(array[i], m+1):
        #(i- k)원을 만드는 방법이 존재하는 경우
        if d[j-array[i]]!= 10001:
            d[j]= min(d[j], d[j-array[i]]+ 1)

if d[m]== 10001:
    print(-1)
else:
    print(d[m])
