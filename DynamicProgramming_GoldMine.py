#nXm크기의 금광, 첫번째 열부터 출발,  
# m-1에 걸쳐 오른쪽 위, 오른쪽, 오른쪽 아래중 하나로 이동했을 때, 
# 얻을 수 있는 최대의 금
array= []
t= int(input())
for i in range(t):
    n, m= map(int, input().split())
    temp= list(map(int, input().split()))
    mine= []
    for i in range(n):
        mine.append(temp[0+(4*i):4+(4*i)])
    result= []
    for i in range(m):
        maxGold= 0
        for j in range(n):
            if  not result or j-1<= result[-1][0]<=j+1:
                if maxGold< mine[j][i]:
                    maxGold= mine[j][i]
                    maxInd= j
        
        result.append((maxInd, maxGold))
    print(mine, "\n", result)
    gold= 0
    for i in result:
        gold+= i[1]
    array.append(gold)
    # print(gold)
for i in range(t):
    print(array[i], end="\n")

# 2 
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7
# 4 4
# 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2