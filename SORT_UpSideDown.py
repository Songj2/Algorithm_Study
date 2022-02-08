n= int(input())
data=[]
for i in range(n):
    data.append(int(input()))

# 정렬 구현
## 선택 정렬
for i in range(n):
    maxInd= i
    for j in range(i, n):
        if data[i]<data[j]:
            maxInd= j
    data[i],data[maxInd]= data[maxInd], data[i]

## 삽입 정렬
for i in range(1, n):
    for j in range(i, 0, -1):
        if data[j]>data[j-1]:
            data[j], data[j-1]= data[j-1], data[j]

## 퀵 정렬_ 암기 실패
def quick(data, start, end):
    pivot= data[0]



#python 라이브러리 이용
# data.sort(reverse=True)
for i in data:
    print(i, end=" ")
#########################################################
n= int(input())
array=[]

for i in range(n):
    array.append(int(input()))

array= sorted(array, reverse=True)

for i in array:
    print(i, end=" ")
