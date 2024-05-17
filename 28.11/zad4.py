x=str(input())
h=int
lst=list(x)
z=0
a=(lst[0])

for y in x:
    if y==a:
        z+=1
    else:
        break
if z==len(lst):
    print('tak')
else:
    print('nie')
