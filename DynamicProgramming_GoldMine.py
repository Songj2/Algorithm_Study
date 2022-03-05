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
    
    gold= 0
    for i in result:
        gold+= i[1]
    array.append(gold)
    # print(gold)
for i in range(t):
    print(array[i], end="\n")
#######################################################################
for tc in range(int(input())):
    # 금광 정보 입력
    n, m= map(int, input().split())
    array=list(map(int, input().split()))
    
    # DP테이블 초기화
    dp= []
    index= 0
    for i in range(n):
        dp.append(array[index:index+m])
        index+= m

    # 다이나믹 프로그래밍 진행
    for j in range(1, m):
        for i in range(n):
            # 완쪽 상단에서 오는 경우
            if i== 0: left_up= 0
            else: left_up= dp[i-1][j-1]
            # 왼쪽 하단에서 오는 경우
            if i== n-1: left_down= 0
            else: left_down= dp[i+1][j-1]
            # 왼쪽에서 오는 경우
            left= dp[i][j-1]
            dp[i][j]= dp[i][j]+ max(left_up, left_down, left)
    result= 0
    for i in range(n):
        result= max(result, left_up, left_down, left)
    print(result)
