n= int(input())
data= []
for i in range(n):
    tn, tg= input().split()
    data.append((tn, int(tg)))

data.sort(key= lambda x:x[1])
for i in range(n):
    print(data[i][0], end=" ")