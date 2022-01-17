# 1. n-1
# 2. n/k
#최소 횟수
n, k= map(int, input().split())
count= 0

while n> 1:
    if n%k==0:
        n//= k

    else:
        n-=1
    count+= 1
    
print(count)
#################################
#강의 버전__반복문이 반복될 때마다 바로 n 이 k로 나눠지는 연산이 이뤄지며 시간복잡도가 log()임, 숫자의 범위가 커져도 빠르게 해결 가능함
n, k= map(int, input().split())
result= 0

while True:
    # n이 k로 나누어 떨어는 수가 될 때까지 빼기
    target= (n// k)* k # n이 k로 나누어 떨어지지 않을 떄, 가장 가까운 k로 나누어 떨어지는 수 찾음
    result+= (n- target) # 1빼는 연산 횟수
    n= target

    #더이상 나눌 수 없을 때(n이 k보다 작을 때), 반복문 탈출
    if n<k:
        break

    result+= 1
    n//= k

# 마지막으로 남은 수에 대하여 1씩 뺴기
result+= (n- 1)
print(result)
