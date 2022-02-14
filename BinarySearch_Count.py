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

######################################################
n, x= map(int, input().split())
data= list(map(int, input().split()))

def search(data, x, start, end):
    if start> end:
        return
    mid= (start+end)//2

    if data[mid]> x:
        search(data, x, start, end)