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