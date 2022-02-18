n= int(input())
food= list(map(int, input().split()))

result= [0]*2
for i in range(0, 2):
    for j in range(i, n, 2):
        result[i]+= food[j]

print(max(result))