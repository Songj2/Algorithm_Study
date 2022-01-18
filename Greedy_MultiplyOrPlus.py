# 숫자로만 아루어진 문자열 S, 왼쪽에서부터 순서대로 연산(곱하기 혹은 더하기), 가장 큰 숫자 만들기
s= input()
result= 0

for i in s:
    i= int(i)
    if result== 0:
        result+= i

    elif i> 1:
        result*= i
    else:
        result+= i

print(result)
##############################
#강의 풀이
# 대게의 경우, 곱하기 연산이 더하기 보다 큼. 0이나 1인 경우는 더하기 연산이 곱하기 연산보다 값이 큼

data= input()
#첫번째 문자를 숫자로 변경하여 대입
result= int(data[0])

for i in range(1, len(data)):
    #두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다 더하기 수행
    num= int(data[i])
    if num<= 1 or result<= 1:
        result+= num
    else:     
        result*= num
      
print(result)    
#현재 상황에서 이러한 조건이 맞다면 곱하기를 수행하고 그렇지 않다면 더하기를 수행해 전형적인 그리디 알고리즘이다.
