n= 5
build_frame=[[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]

def solution(n, build_frame):
    answer = []
    wall= [[0]*(n+1) for i in range(n+1) ] # 벽면

    for i in build_frame:
        y= i[0]
        x= i[1]
        a= i[2]
        b= i[3]
        if a== 0: #구조물이 기둥일 경우
            if b== 1: # 설치
                if x== 0 or wall[x][y]==2 or wall[x][y-1]>= 2 or wall[x-1][y]%2==1:   # 기둥 설치 조건 바닥/ 기둥 위/ 보 
                    wall[x][y]+= 1
                    answer.append([y, x, a])                  
                    
                        
            else: # 삭제   
                # 해당 기둥 위에 기둥이 없거나 해당 기둥과 연결된 보의 양옆에 보가 존재할 때
                print(i)
                if wall[x][y]== 3: # 기둥과 보가 같이 있을 때
                    # x-1에 1/3(홀수)이거나 y+-1에 2/3이거나
                    print(3)
                    if wall[x-1][y]%2== 1 or wall[x][y-1]>=2 or wall[x][y+1]>=2:
                        wall[x][y]-= 1
                        print(wall[x][y])
                        answer.remove([y, x, a])
                else: # 기둥만 존재할 때
                    print(1)
                    # x+1에 연결된 보가 자립할 수 있거나/ 기둥이 없거나
                    if wall[x+1][y]== 0 or (wall[x+1][y-1]>1 and wall[x+1][y]>1)  :
                        wall[x][y]-= 1
                        print(wall[x][y])
                        answer.remove([y, x, a])
                

        else: #구조물이 보일 경우
            if b== 1: # 설치
                if wall[x-1][y]==1 or wall[x-1][y+1]== 1 or (wall[x][y-1]>1 and  wall[x][y+1]>1):  # 보 설치 조건: 기둥 위/ 양옆으로 보와 연결
                    wall[x][y]+= 2
                    answer.append([y, x, a])
            
            else: # 삭제  
             # 해당 보의 끝에 기둥이 새워져 있거나 양쪽으로 보가 연결되있을 경우
                if wall[x][y]== 3: #보와 기둥이 같이 있을 때
                    #x-1에 1/3이거나 y-1에 2/3이거나 
                    if wall[x-1][y]%2== 1 or (wall[x][y-1]> 1 and wall[x-1][y-1]%2==1):
                        wall[x][y]-= 2
                        answer.remove([y, x, a])
                        
                    #y+1에 보가 있다면 자립할 수 있거나 
                    elif wall[x][y+1]%2==1:
                        if wall[x-1][y+1]%2== 1 or wall[x-1][y+2]%2== 1:
                            wall[x][y]-= 2
                            answer.remove([y, x, a])
                
                else: #보만 존재할 때
                    # 양옆의 보가 기둥이랑 연결되어 있거나
                    if (wall[x-1][y-1]%2==1 or wall[x-1][y]%2==1) and (wall[x-1][y+1]%2==1 or wall[x-1][y+2]%2==1):
                        wall[x][y]-= 2
                        answer.remove([y, x, a])

    # 구조물 확인용
    for i in range(n):
        print(wall[i])

    answer.sort()

    return answer


print(solution(n, build_frame))
