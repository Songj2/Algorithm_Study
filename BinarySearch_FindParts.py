n= int(input())
parts= list(map(int, input().split()))
parts.sort()
m= int(input())
needs= list(map(int, input().split()))

def search(data, x, start, end):
    if start>end:
        return None

    mid= (start+ end)//2
    if data[mid]== x:
        return mid
    elif data[mid]> x:
        return search(data, x, start, mid-1)
    else:
        return search(data, x, mid+1, end)
result=[]

for i in needs:
    result.append(search(parts, i, 0, n))

for i in result:
    if i== None:
        print("No", end=" ")
    else:
        print("Yes", end=" ")
######################################################################
##Lecture
#이진 탐색 반복문 ver
def binary_search(array, target, start, end):
    while start<= end:
        mid= (start+ end)// 2
        if array[mid]== target:
            return mid

        elif array[mid]> target:
            end= mid- 1
        else:
            start= mid+ 1
    return None

n= int(input())
array= list(map(int, input().split()))
array.sort()
m= int(input())
x= list(map(int, input().split()))

for i in x:
    result= binary_search(array, i, 0, n-1)
    if result!= None:
        print("yes", end=" ")
    else:
        print("no", end=" ")
########################################
#계수 정렬 ver        
n= int(input())
array= [0]*1000001

#가게에 있는 전체 부품 번호를 입력받아서 기록
for i in input().split():
    array[int(i)]= 1

m= int(input())
x= list(map(int, input().split()))

#손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    #해당 부품이 존재하는지 확인
    if array[i]== 1:
        print("yes", end=" ")
    else:
        print("no", end=" ")
########################################
#집합 자료형 ver 
#set()은 집합 자료형을 초기화 할 때 사용, 단순히 특정한 데이터가 존재하는지 검사할 떄 매우 효과적으로 사용
n= int(input())
array= set(map(int, input().split()))

m= int(input())
x= list(map(int, input().split()))

for i in x:
    if i in array:
        print("yes", end=" ")
    else:
        print("no", end=" ")
