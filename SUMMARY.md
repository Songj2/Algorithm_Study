##### 이코테 강의 정리 (https://www.youtube.com/playlist?list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC)
# GREEDY ALGORITHM
- 현재 상황에서 지금 당장 좋은 것만 고르는 방법
- 일반적인 그리디 알고리즘은 문제를 풀기 위한 최소한의 아이디어를 떠올릴 수 있는 능력을 요구
- 정당성 분석이 중요

    :가장 좋아 보이는 것만 선택해도 최적의 해를 구할 수 있는지
  - 일반적으로 그리디 해법이 최적의 해를 보장하지 않을 때가 많음
  - BUT 코딩테스트의 경우, 탐욕법으로 얻은 해가 최적의 해가 되는 상황으로 출제

+ 거스름돈 문제 (대표적인 greedy 문제)
    ```python
    change= int(input())

    coin= [500, 100, 50, 10]
    count= 0

    for i in coin:
        count+= change// i
        change%= i

    print(count)
    ```
    + 장당성 분석 <br>
    : 가지고 있는 동전 중에서 큰 단위는 항상 작은 단위의 배수이므로 작은 단위의 동전을 종합해 다른 해가 나올 수 없다. 
    
    + 시간 복잡도 분석 <br>
    : 화페의 종류가 K라고 할 때, 시간복잡도는 O(K). <br> - 전체 동전의 종류에만 영향을 받음

# 구현_Implementation
- 머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정
- 일반적으로, 문제에서 요구하는 내용이 구현에 초점이 맞춰져 있거나 구현이 어려운 문제를 지칭함
  
  - 간단한 알고리즘이지만 코드가 긴 문제
  - 실수 연산을 다루고, 특정 소수점 자리까지 출력하는 문제
  - 문자열을 특정 기준에 따라 끊어 처리하는 문제
  - 적절한 라이브러리를 찾아서 사용하는 문제
    - Ex) 모든 순열과 모든 조합을 찾는 문제(이터투스 라이브러리 사용시 간결해짐)

  - 2차원 공간은 행렬(Matrix)로 표현
  - 시뮬레이션 및 완전 탐색의 경우, 2차원 공간에서의 방향벡터가 자주 활용됨
     ```python
    # 동 북 서 남 
     dx= [0, -1, 0, 1]
     dy= 1, 0, -1, 0]

     x, y= 2, 2 #현재 위치, ㅌ는 새ㅔ로축
     for i in range(4): #이동
       nx= x+ dx[i]
       ny= y+dy[i]
       print(nx, ny)
     ```
# 그래프 탐색 알고리즘_ DFS/BFS
- 탐색(Search)이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 것
- 코딩테스트에서 자주 등장하는 유형
- 알아 두어야할 자료구조
  
  - 스택 (Stack)
    - 선입후출의 자료구조
    - 입구==출구의 형태로 시각화
    - 삽입.append()과 삭제.pop()로 구성
    - 최하단부터 출력시 차례로, 최상단부터 출력시 역순으로
  - 큐 (Queue)
    - 선입선출의 자료구조
    - 입구와 출구가 모두 뚫려있는 터널과 같은 형태로 시각화
    - deque라이브러리 이용시. 삽입.append() 식제.popleft() 이용 
      - deque이용이 list로 구현한 것보다 시간복잡도가 적음
      - 

- 재귀함수 (Recursive Function)
  - 자기 자신을 다시 호출하는 함수
  - 최대 재귀 깊이 제한
  
    - 문제풀이에는 재귀함수의 종료 조건을 반드시 명시
    - 종료 조건을 명시하지 않으면 함수가 무한히 호출될 수 있음 
      ```python
      def recursive_function(i):
        if i== 199:
          return print(i, '번째 재귀함수에서 ', i+1, '번째 재귀함수를 호출합니다.')
        return print(i, '번째 재귀함수를 종료합니다.')
      ```
    ```python
    #factorial
    def factorial(n):
      if n<=1:
        return 1
      return n* factorial(n- 1)

    #유클리드 호제법
    def gcd(a, b):
    if a% b== 0:
        return b
    else:
      return gcd(b, a% b)
    ```
    - 점화식을 그대로 이용해여 반복문에 비해 코드가 간결함
    - pc가 함수를 연속적으로 호출하면 메모리 내부에 스택 프레임이 쌓임
      - 스택을 사용해야 할 때 구현상 스택 라이브려리 대신 재귀함수를 이용하는 경우가 있음
  
  ## DFS(Depth-First Search)
    - 깊이 우선탐색, 그래프에서 깊은 부분을 우선적으로 탐색
    - 스택 자료구조(혹은 재귀 함수)를 이용
       1. 탐색 시작 노드를 스택에 삽입하고 방문 처리
       2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 해당 노드를 스택에 넣고 방문 처리, 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄
       3. 2과정을 수행할 수 없을 때까지 반복
    ```python
    def dfs(graph, v, visited):
      visited[v]= True
      print(v)

      for i in graph[v]:
        if not visited[i]:
          dfs(graph, i, visited)
    ```
  ## BFS(Breadth-First Search)
  - 너비 우선 탐색, 그래프에서 가까운 노드부터 우선적으로 탐색
  - 큐 자료구조를 이용
    1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
    2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드르 모둥 큐에 삽입하고 방문 처리
    3. 2과정을 수행할 수 없을 떄까지 반복
  ``` python
   from collections import deque
      def bfs(graph, start, visited):
        visited[start]= True

        queue= deque([start])
        while queue:
          v= queue.popleft()
          print(v)

          for i in graph[v]:
            if not visited[i]:
              visited[i]= True
              queue.append(i)
    ```
