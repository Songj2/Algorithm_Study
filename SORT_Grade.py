n= int(input())
data= []
for i in range(n):
    tn, tg= input().split()
    data.append((tn, int(tg)))

data.sort(key= lambda x:x[1])

for i in range(n):
    print(data[i][0], end=" ")

##########################################
n= int(input())
array= []
for i in range(n):
    input_data= input().split()
    array.append((input_data[0], int(input_data[1])))

array= sorted(array, key= lambda stuednt:stuednt[1])

for student in array:
    print(student[0], end=" ")   
