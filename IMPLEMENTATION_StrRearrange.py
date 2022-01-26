strData= input()
temp=[]
num= 0
for i in strData:
    t= ord(i) #대문자 문자이면
    if t>=65:
        temp.append(i) #temp에 추가
    else: #숫자이면
        num+=int(i) #더하기

temp.sort() #오름차순으로 정렬
print("".join(temp)+ str(num)) #정렬한 순서대로 출력한뒤, 숫자합 출력
#################################################################
#입력된 문자열을 하나씩 확인하여 숫자인 경우 따로 합계 계산, 알파벳인 경우는 별도의 리스트에 저장
#리스트에 저장된 알파벳을 정렬해 출력하고 합계를 뒤에 붙여 출력
data= input()
result=[]
value=   0
for x in strData:
    # 알파벳인 경우, 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    # 숫자는 따로 더하기
    else: 
        value+= int(x) 

# 알파벳을 오름차순으로 정렬
result.sort() 
#숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value!= 0:
    result.append(str(value))

print("".join(result)) 
