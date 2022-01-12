n,m= map(int,input().split())
minValue= -1
card= []

for i in range(n):
    card.append(list(map(int,(input().split()))))

for i in card:
    if minValue< min(i):
        minValue= min(i)

print(minValue)