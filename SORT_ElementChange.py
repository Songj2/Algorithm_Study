# 배열 A와 배열 B_ 각 N개의 원소로 구성_원소는 모두 자연수
#최대 K번 바꿔치기 연산 수행_ A의 합이 최대가 되도록
# 배열 A의 모든 워소의 합의 최댓값 출력
n, k= map(int, input().split())

a= list(map(int,input().split()))
b= list(map(int,input().split()))

a.sort() #오름차순 정렬
b.sort(reverse=True) #내림차순 정렬

for i in range(k):
    if a[i]<b[i]: #배열 a의 작은 수와 배열 b의 큰 수 비교하여 
        a[i], b[i]= b[i], a[i] #큰 수로 교체

print(sum(a))