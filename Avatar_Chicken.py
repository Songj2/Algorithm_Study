n, m= map(int, input().split())
city= []
for i in range(n):
    city.append(list(map(int, input().split())))
# print(city)
chicken= []
home= []
answer= 0

for i in range(n):
    for j in range(n):
        if city[i][j]== 2:
            chicken.append((i,j))
        elif city[i][j]== 1:
            home.append((i,j))

chickenLen= [[] for i in range(len(chicken))]
close= m-len(chicken)
# 치킨집 폐업X
if len(chicken)<= m:
    for i in home:
        length= []
        for j in chicken:
            length.append(abs(i[0]-j[0])+ abs(i[1]-j[1]))
        answer+= min(length)
        # print("length", length)

# 치킨집 폐업O
else:
    length= [[] for i in range(len(home))]
    for i in range(len(home)):
        for j in range(len(chicken)):
            cal= abs(home[i][0]-chicken[j][0])+ abs(home[i][1]-chicken[j][1])
            length[i].append(cal)
            chickenLen[j].append(cal)
        # print("length", length)
        
    # print("chickenLen", chickenLen)
    temp=[]
    # 폐업할 집의 수
    for n in range(close):
        for k in chickenLen:
            temp.append(sum(k))
        getInd= temp.index(max(temp))
        temp.pop(getInd)
        print("getInd", getInd, temp, sum(temp))

        for k in range(len(length)):
            length[k].pop(getInd)
            
    for m in range(len(length)):
        answer+= min(length[m])
print(answer)
# # 도시 확인용
# for i in range(n):
#     print(city[i])
