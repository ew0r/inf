x=str(input())
y=list(x)
a=0
i=0

for u in range(0,10):
    if a>2:
        print(i)
    for i in y:
        if u==int(i):
            a+=1