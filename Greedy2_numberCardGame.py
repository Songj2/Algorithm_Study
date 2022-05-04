n, m= map(int, input().split())
num= 0
array=[]
for i in range(n):
    array.append(list(map(int, input().split())))
    mNum= min(array[i])
    if num< mNum:
        num= mNum

print(num)
#9분 9초
#####################################################
# 1 min()함수 이용_이코테 답안
n, m= map(int, input().split())
result= 0
for i in range(n):
    data= list(map(int, input().split()))
    min_value= min(data)
    result= max(result, min_value)
print(result)
#####################################################
# 2 2중 반복문_이코테 답안
n, m= map(int, input().split())
result= 0
for i in range(n):
    data= list(map(int, input().split()))
    min_value= 10001
    for a in data:
        min_value= min(min_value, a)
    result= max(result, min_value)
print(result)