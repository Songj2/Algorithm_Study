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

