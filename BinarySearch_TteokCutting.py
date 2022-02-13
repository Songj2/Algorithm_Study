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
######################################################################
n, m= list(map(int, input().split(" ")))
array= list(map(int, input().split()))

#시작점과 끝점 설정
start= 0
end= max(array)

#이진 탐색 수행
result= 0
while(start<= end):
    total= 0
    mid=(start+end)//2
    for x in array:
        #잘랐을 때의 떡의 양 계산
        if x> mid:
            total+= x- mid
    #떡의 양이 부족한 경우 더 자르기_ 왼쪽 탐색
    if total< m:
        end= mid- 1
    #떡의 양이 충분한 경우 덜 자르기_ 오른쪽 탐색
    else:
        result= mid #최대한 덜 자른 값을 구하므로 result에 기록
        start= mid+ 1

print(result)
