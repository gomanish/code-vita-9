x,y=map(int,input().split())
length = int(input())
stock = [float(x) for x in input().split()]
a = 0
b = 0
X=[]
Y=[]
for i in range(length):
    a = sum(stock[i:i+2])/2
    X.append(a)
for i in range(length-3):
    b = sum(stock[i:i+4])/4
    Y.append(b)


count = 0

for i in range(1, len(Y)):
    if X[i] > Y[i] and X[i-1] < Y[i-1]:
        count += 1
    elif X[i] < Y[i] and X[i-1] > Y[i-1]:
        count += 1

print(count)