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
    