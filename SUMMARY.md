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

