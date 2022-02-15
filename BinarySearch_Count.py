from bisect import bisect_left, bisect_right

n, x= map(int, input().split())
data= list(map(int, input().split()))

left= bisect_left(data, x)
right= bisect_right(data, x)

result= right- left

if result> 0:
    print(result)
else:
    print(-1)

########################################################
#직접 구현ver
def search(data, x, start, end):
    if start> end:
        return
    mid= (start+ end)//2

    if data[mid]> x:
       return search(data, x, start, mid) 
    elif data[mid]== x:
        if data[start]!= x and data[end-1]!= x:
            return search(data, x, start, mid), search(data, x, mid+1, end)
        
        return mid
    else:
        return search(data, x, mid+1, end)
ss, ee=  search(data, x, 0, n)
if ee-ss>0:
    result= ee-ss+1
else:
    result= -1
print(result)

########################################################
#lectureCode
from bisect import bisect_left, bisect_right

#값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def countByRange(array, left_value, right_value):
    right_index= bisect_right(array, right_value)
    left_index= bisect_left(array, left_value) 
    return right_index- left_index

n, x= map(int, input().split())
array= list(map(int, input().split()))

#범위에 있는 데이터의 개수 계산
count= countByRange(array, x, x)

if count== 0:
    print(-1)
else:
    print(count)
