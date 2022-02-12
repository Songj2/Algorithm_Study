n, m= map(int, input().split())
tteok= list(map(int, input().split()))
tteok.sort()
h= 0
rest= 0

if tteok[n-1]- tteok[0]>= m:
    h= tteok[n-1]- tteok[0]
else:
    h= tteok[n-1]-m

for i in range(n):
    temp= tteok[i]- h
    if temp< 0:
        tteok[i]= 0
    else:
        tteok[i]= temp
    rest+= tteok[i]

while rest>= m:
    if rest== m:
        break
    h+= 1
    for i in range(n):
        temp= tteok[i]-1
        if temp< 0:
            tteok[i]= 0
        else:
            tteok[i]= temp
            rest-= 1


print(h)