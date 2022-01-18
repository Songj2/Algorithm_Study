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