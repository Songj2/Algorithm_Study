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
result= ee-ss+1
print(result)
