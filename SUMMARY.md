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

# 정렬 알고리즘
- 데이터를 특정 기준에 따라 순서대로 나열한 것

## 1. 선택 정렬
  - 처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 것과 바꿈
  ``` python
  #myCode#############################################################################
  data=[7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
  for i in range(len(data)-1):
    minValue= data[i]
    minIndex= i
    for j in range(i+ 1, len(data)):
      if minValue> data[j]:
        minValue= data[j]
        minIndex= j
    data[i], data[minIndex]= minValue, data[i]

  #lectureCode########################################################################
  for i in range(len(data)):
    min_index= i
    for j in range(i+1, len(data)):
      if array[min_index]> data[j]:
        min_index= j
    data[i], data[min_indx]= data[min_index], data[i]
    
  ```
  - n번만큼 가장 작은 수를찾아서 맨 앞으로 보냄
  - 전체 연산 횟수는 (N^2+ N -2)/2,  시간 복잡도는 O(N^2)
  
## 2. 삽입정렬
  - 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입
    - 두번째 데이터부터 앞쪽에 있는 원소와 비교하여 왼쪽으로 이동
  - 선택 정렬과 비교하여 구현이 어렵지만 더 효율적으로 동작
  ```python
  data= [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
  #myCode#############################################################################
  for i in range(1, len(data)):
    for j in range(i-1, -1, -1):
      if data[i]> data[j]:
        iValue= data.pop(i)
        data.insert(j+1, iValue)
        break
      elif data[i]<data[0]:
        iValue= data.pop(i)
        data.insert(0, iValue)
        break
  #lectureCode########################################################################
  for i in range(1, len(data)):
    for j in range(i, 0, -1):
      if data[j]<data[j-1]>:
        data[j], data[j-1]= data[j-1], data[j]
      else:
        break
  ```
  - 시간 복잡도는 O(N^2)
  - 현재 리스트의 데이터가 거의 정렬되어 있는 경우, 매우 빠르게 동작함
    - 전부 정렬되어 있는 경우, O(N)임_ 왼쪽 원소만 비교하기 때문에 

## 3. 퀵 정렬
  - 기준 데이터를 설정한 뒤, 해당 데이터보다 큰 데이터와 작은 데이터의 위치를 변경
  - 일반적인 상황에서 가장 많이 사용됨
  
    - 첫번째 데이터를 기준 데이터(Pivot)으로 설정
    - 왼쪽에서부터 Pivot보다 큰 값 선택, 오른쪽에서부터 Pivot보다 작은 값 선택해서 서로 위치 변경
    - 위치가 엇갈리는 경우, Pivot과 작은 데이터의 위치를 서로 변경_ Pivot값 기준으로 오른쪽은 값이 크고 왼쪽은 값이 작음: 분할(Pivot을 기준으로 데이터 묶음을 나누는 작업)
    - 각 묶음을 다시 퀵정렬 수행
  ```python
  data= [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
  #myCode#############################################################################
  #lectureCode########################################################################
  def quick_sort(data, start, end):
    if start>= end:
      return

    pivot= start
    left= start+ 1
    right= end

    while(left<= right):
      while(left<= end and data[left]<= data[pivot]): #PIVOT보다 큰 값을 찾을 떄까지
        left+= 1
      while(right> start and data[right]>= data[pivot]): #PIVOT보다 작은 값을 찾을 떄까지
        right_= 1
      if (left> right): #엇갈렸으면 작은 값과 PIVOT 교체
        data[right], data[pivot]= data[pivot], data[right]
      else: # 작은 값과 큰 값 교체
        data[left], data[right]= data[right], data[left]

    # 분할 후 왼쪽과 오른쪽부분에서 정렬 수행
    quick_sort(data, start, right- 1)
    quick_sort(data, right+ 1, end)

    
    #PYTHON의 장점을 살린 CODE#############################################################
    def quick_sort(data):
      if len(data)<= 1:
        return data
      pivot= data[0]
      tail=[1:]

      left_side= [x for x in tail if x<= pivot]
      right_side= [x for x in tail if x> pivot]

      return quock_sort(left_side)+ [pivot]+ quick_sort(right_side)Sz
  ```
  - 이상적인 경우, 분할이 절반씩 일어나고 전체 연산 횟수는 O(NlogN)
  - 평균의 경우, 시간복잡도: O(NlogN) 최악의 경우, O(N^2)
    - 첫번째 원소를 Pivot으로 설정하고 이미 정렬되 배열에 대해 퀵 정렬을 수행시,  매번 오른쪽 데이터만 남기 때문에 매번 선형 탐색을 수행함
  
## 4. 계수 정렬
  - 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용 가능
  - 조건이 부합하는 경우에만 사용가능, 매우 빠르게 동작
    - 데이터의 개수가 N, 데이터(양수) 중 최댓값이 K일 때, 촤악의 경우에도 수행시간 O(N+K) 보장
```python
  data= [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
  #myCode#############################################################################
  check=[0]* 10
  for i in data:
    check[i]+= 1

  for i in range(len(check)):
    print(str(i)*check[i], end="")

  #lectureCode########################################################################
  #모든 범위를 포함하는 리스트 선언
  count= [0]*(max(data)+1)

  for i in range(len(data)):
    count[data[i]]+= 1 #각 데이터에 해당하는 인덱스의 값 증가

  for i in range(len(count)): #리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
      print(i. end=" ")
```
- 가장 작은 값부터 큰 값까지 포함하는 배열을 생성해 공간 복잡도가 높지만, 퀵정렬과 비교하여 조건만 맞는다면 더 빨리 작동함
- 정렬 정보를 확인하는 이중반복문에서 j반복문은 전체 수행 횟수가 N이므로 이중 반복문의 수행횟수가 O(N+K)임
  - 시간 복잡도와 공간 복잡도: O(N+K)
- 동일한 값을 가지는 데이터가 여러 개 등장할 때 효과적으로 사용할 수 있음

## 5. 정렬 알고리즘 비교
  | 정렬 알고리즘|  평균 시간 복잡도| 공간 복잡도|  특징|
  |-------------|-----------------|-----------|-----|
  |선택 정렬| O(N^2)| O(N)| 아이디어가 매우 간단함|
  |삽입 정렬| O(N^2)| O(N)| 데이터가 거의 정렬되어 있을 떄는 가장 빠름|
  |퀵 정렬| O(NlogN)| O(N)| 대부분의 경우에 가장 적합하며, 충분히 빠름|
  |계수 정렬| O(N+K)| O(N+K)| 데이터의 크기가 한정되어 있는 경우에만 사용가능하지만, 매우 빠르게 동작|


# 이진 탐색
  - 순차 탐색: 리스트 안에 특정 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는 방식
  - 이진 탐색: 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방식
    - 시작점과 중간점, 끝점을 이용해 탐색 범위 설정
    - 1. 중간점은 끝점/2 소수점 이하 제거하여 찾음
    - 2. 중간점의 값이 탐색 값보다 크면, 끝점을 중간점 왼쪽으로 옮기고 새로운 중간점 찾음
    - 2. 중간점의 값이 탐색 값보다 작으면, 시작점을 중간점 오른쪽으로 옮기고 새로운 중간점 찾음
    ```python
    data=[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    #myCode#############################################################################
    def sech(start, end, target):
        mid= int((end-start)//2)+ start

        if data[mid]== target:
            return mid
        elif data[mid]> target:
            return sech(start, mid-1, target)
        elif data[mid]< target:
            return sech(mid+1, end, target)
    #lectureCode######################################################################
    ## 재귀함수 ver
    def binary_search(array, target, start, end):
      if start> end:
        return None
      mid= (start+end)//2
      if array[mid]== target:
        return mid

      elif array[mid]> tagrget:
        return binary_search(array, target, start, mid- 1)
      else:
        return binary_search(array, target, mid+1, end)

    ## 반복문 ver
    def binary_search(array, target, start, end):
      while start<= end:
        mid= (start+ end)//2
        if array[mid]== target:
          return mid
        elif array[mid]> target:
          end= mid- 1
        else:
          start= mid+ 1
      return None


    n, target= list(map(int, input().split()))
    array= list(map(int, input().split()))

    result= binary_search(array, target, 0, n-1)
    if result== None:
      print("원소가 존재하지 않습니다.")
    else:
      print(reslut+ 1)
    #추가사항#########################################################################
    from bisect import bisect_left, bisect_right

    bisect_left(a, x) # 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스 반환
    bisect_right(a, x) # 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스 반환
    ```
  - 단계마다 탐색 범위를 2로 나누는것과 동일함: 연산횟수는 log2의 ㅍN에 비례
  - 시간복잡도: O(logN)
  ## 파라메트릭 서치(Parametric Search)
  - 최적화 문제를 결정(Y/N) 문제로 바꾸어 해결하는 기법
    - 특정 조건을 만족하는 가장 알맞는 값을 빠르게 찾는 최적화 문제 등
  - 일반적으로 코딩 테스트에서 이진 탐색을 이용하여 해결


 

# 다이나믹프로그래밍(Dynamic Programming)_ 동적 계획법
- 메모리를 적절히 사용하여 수행 시간 효율성을 비약적으로 향상시키는 방법
- 이미 계산된 결과는 별도의 메모리 영역에 저장하여 다시 계산하지 않음
- 탑다운(하향식) or 보텀업(상향식) 방식
- 다이나믹 프로그래밍에서 다이나믹은 별다른 의미 없이 사용된 단어임
- 다이나믹 프로그래밍 사용 조건
  
  1. 최적 부분 구조(Optimal Substructure): 큰 문제를 작은 문제로 나눌 수 있고, 작은 문제의 답을 모아 큰 문제를 해결하는 방식
  2. 중복되는 부분 문제(Overlapping Subproblem): 동일한 작은 문제를 반복적으로 해결

- 대표적인 예시: 피보나치 수열
  ```python
    #myCode#############################################################################
    def fibonacci(n):
      if n<=2:
        return 1
      return fibonacci(n-1)+ fibonacci(n-2)
    #lectureCode######################################################################
    ## 
    def fibo(x):
      if x== 1 or x== 2:
        return 1
      return fibo(x-1)+ fibo(x-2)
  ```
  - 재귀함수로 피보나치 수열을 해결하면 지수 시간 복잡도O(N^2)를 가짐_ f(2)가 여러번 호출되는 중복되는 부분 발생
  ## 메모이제이션(Memoization)
  - 다이나믹 프로그래밍을 구현하는 방법 중에 하나
  - 한번 계산한 결과를 메모리 공간에 메모하는 방식
    - 같은 문제를 다시 호출하면 메모했던 결과를 가져옴
    - 값을 기록해 놓은 점에서 캐싱(Caching)이라고 함
  - 이전에 계산된 결과를 일시적으로 기록해 놓는 넓은 개념을 의미
    - 다이나믹 프로그래밍에만 국한된 개념이 아님 

  ## 탑다운 Vs 보텀업
  - 다이나믹 프로그래밍의 전형적인 형태_ 보텀업
    - 결과 저장용 리스트를 DP테이블이라 함
  
  ```python 
  #탑다운 방식으로 재귀함수로 피보나치 구현#########################################################
  #메모제이션 하기 위한 리스트 초기화
  d= [0]* 100
  def fibo(x):
    #종료 조건
    if x== 1 or x== 2:
      return 1
    #계산한 적 있는 문제라면 반환
    if d[x]!= 0:
      return d[x]
    #아직 계산하지 않은 문제라면 점화식에 따라 피보나치 결과 반환
    d[x]= fibo(x-1)+ fibo(x-2)
    return d[x]
  #보텀업 방식으로 반복문으로 피보나치 구현#########################################################
  d= [0]* 100
  d[1]=1
  d[2]=1
  n= int(input())
  for i in range(3, n+ 1):
    d[i]= d[i-1]+ d[i-2]
  ```
  - 이미 계산된 결과를 메모리에 저장하면 더 적게 호출됨
  - 시간 복잡도는 O(N)

## 다이나믹 프로그래밍 Vs 분할 정복
  - 최적 부분 구조를 가질 때 사용할 수 있음
    |분할 정복| 다이나믹 프로그래밍|
    |-------------------|---------------------------------------------------|
    | 동일한 부분 문제가 반복적으로 계산되지 않음 | 각 부분 문제들이 서로 영향을 미치며 부분 문제가 중복됨|
  - 퀵 정렬의 경우,<br> 한번 Pivot이 자리르 변경해서 자리를 잡으면 기준 원소의 위치는 바뀌지 않음. <br>분할 이후에 해당 피벗을 다시 처리하는 부분 문제는 호출하지 않음. =>  분할 정복 
