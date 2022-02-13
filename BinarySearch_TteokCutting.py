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
######################################################################
n, m= map(int, input().split())
tteok= list(map(int, input().split()))
tteok.sort()

def cutting(data, m, start, end):
    if start> end:
        return None

    mid= (start+end)//2
    temp= 0
    for i in range(mid, end):
        if data[i]-data[mid]>0:
            temp+= data[i]-data[mid]
    
    if temp<m:
        return start, mid
    else:
        return cutting(data, m, mid+1, end)

ss, mm= cutting(tteok, m, 0, n)
h= tteok[ss]
result= tteok[-1]

while result>m:
    h+=1
    result= 0
    
    for i in range(ss, n):
        if tteok[i]-h> 0:
            result+=tteok[i]- h

print(h)      
